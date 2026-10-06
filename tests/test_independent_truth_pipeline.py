"""Evidence pipeline (2026-10-07): independent truth advances when results are published, never from Kalshi, and nothing
already written is rewritten; ESPN refresh is incremental and lossless; the capture conductor neither slows down nor
overwrites the day's external evidence."""
import gzip
import hashlib
import json
import os
import subprocess
import sys
from datetime import date, datetime, timedelta, timezone

import pandas as pd
import pytest

from tennis_edge.ledger import truth_freshness as tf
from tennis_edge.ledger.sports_truth import (AMBIGUOUS, NOT_COVERED, NOT_FOUND, PENDING_RESULT, RESOLVED, ResultsIndex,
                                              reconcile_match_winner)

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(ROOT, "scripts", "data"))


def _rows(rows):
    base = {"canonical_id_status": "MAPPED", "outcome_type": "COMPLETED", "score_raw": "6-4 6-4", "games_w": 12,
            "games_l": 8, "sets_w": 2, "sets_l": 0, "match_key": "k", "tourney_name": "T"}
    return pd.DataFrame([{**base, **r} for r in rows])


SACKMANN_OLD = {"tour": "WTA", "tourney_date": "2026-04-27", "canonical_winner_id": "s1", "canonical_loser_id": "s2",
                "source_label": "sackmann_WTA_main", "level_canonical": "MASTERS_1000"}
ESPN_OLD = {"tour": "WTA", "tourney_date": "2026-10-04", "canonical_winner_id": "e1", "canonical_loser_id": "e2",
            "source_label": "espn_WTA", "level_canonical": "TOUR_500_250"}
ESPN_NEW = {"tour": "WTA", "tourney_date": "2026-10-06", "canonical_winner_id": "221012", "canonical_loser_id": "221406",
            "source_label": "espn_WTA", "level_canonical": "TOUR_500_250"}


# ------------------------------------------------------------------------------------------- status semantics
def test_newly_published_espn_result_resolves_an_existing_prediction():
    """WTA Beijing (Kalshi level MASTERS_1000; ESPN codes it 'P' = TOUR_500_250). Before the publish the result is
    PENDING (ESPN is live); after it, RESOLVED -- by canonical ids, with the source recorded."""
    before = ResultsIndex(_rows([SACKMANN_OLD, ESPN_OLD]), since=date(2026, 8, 1), as_of=date(2026, 10, 6))
    t0 = before.resolve("WTA", "221012", "221406", "MASTERS_1000", date(2026, 10, 5))
    assert t0.status == PENDING_RESULT
    after = ResultsIndex(_rows([SACKMANN_OLD, ESPN_OLD, ESPN_NEW]), since=date(2026, 8, 1), as_of=date(2026, 10, 7))
    t1 = after.resolve("WTA", "221012", "221406", "MASTERS_1000", date(2026, 10, 5))
    assert t1.status == RESOLVED and t1.winner_id == "221012" and t1.source_label == "espn_WTA"


def test_espn_coverage_is_by_family_so_a_wta_1000_miss_is_not_found_not_uncovered():
    idx = ResultsIndex(_rows([SACKMANN_OLD, ESPN_NEW]), since=date(2026, 8, 1), as_of=date(2026, 10, 7))
    assert idx.coverage("WTA", "MASTERS_1000") == date(2026, 10, 6)
    assert idx.resolve("WTA", "x", "y", "MASTERS_1000", date(2026, 10, 1)).status == NOT_FOUND
    # a match the day before ESPN's newest board: inside the rain-delay window, so not yet conclusive
    assert idx.resolve("WTA", "x", "y", "MASTERS_1000", date(2026, 10, 5)).status == PENDING_RESULT
    # ESPN has no ATP Challenger or ITF board, and carries only part of WTA 125 (below)
    assert idx.coverage("WTA", "WTA_125") is None
    assert idx.coverage("ATP", "CHALLENGER") is None and idx.coverage("WTA", "ITF") is None


def test_wta_125_is_partial_coverage_so_a_miss_is_pending_then_not_covered_never_not_found():
    """ESPN's WTA boards carry some WTA 125 events and some of their rounds (2026-09-13..17: Antalya 11 matches, Montreux
    10, several 125s none). Production 2026-10-06 read 46 September 125 misses as NOT_FOUND; a source that skips events
    cannot say a match was not played."""
    idx = ResultsIndex(_rows([SACKMANN_OLD, ESPN_NEW]), since=date(2026, 8, 1), as_of=date(2026, 10, 7))
    assert idx.partial_horizon[("WTA", "CHALLENGER")] == date(2026, 10, 6)
    old = idx.resolve("WTA", "x", "y", "WTA_125", date(2026, 9, 14))
    assert old.status == NOT_COVERED and "partly covered" in old.reason
    assert idx.resolve("WTA", "x", "y", "WTA_125", date(2026, 10, 5)).status == PENDING_RESULT
    # a 125 result ESPN does carry still resolves (ESPN rows say TOUR_500_250 for a 125 match)
    hit = idx.resolve("WTA", "221012", "221406", "WTA_125", date(2026, 10, 6))
    assert hit.status == RESOLVED and hit.source_label == "espn_WTA"
    # ESPN gone quiet: no PENDING, and the freshness block names the families that are not live
    stale = ResultsIndex(_rows([SACKMANN_OLD, ESPN_NEW]), since=date(2026, 8, 1), as_of=date(2026, 10, 20))
    assert stale.resolve("WTA", "x", "y", "WTA_125", date(2026, 10, 18)).status == NOT_COVERED
    fr = tf.freshness(stale, {"sources": {}}, date(2026, 10, 20))
    assert fr["horizons"]["WTA 125"]["coverage"] == "partial"
    assert set(fr["espn_families_not_live"]) == {"ATP tour", "WTA tour", "WTA 125"}
    assert tf.freshness(idx, {"sources": {}}, date(2026, 10, 7))["espn_families_not_live"] == ["ATP tour"]


def test_source_horizon_separates_not_covered_pending_and_not_found():
    tml = {"tour": "ATP", "tourney_date": "2026-09-29", "canonical_winner_id": "a", "canonical_loser_id": "b",
           "source_label": "tml_ATP_challenger", "level_canonical": "CHALLENGER"}
    m = _rows([tml])
    # stale source (newest result 7 days before the run): the level is not covered for this match
    idx = ResultsIndex(m, since=date(2026, 8, 1), as_of=date(2026, 10, 6))
    assert idx.resolve("ATP", "c", "d", "CHALLENGER", date(2026, 10, 5)).status == NOT_COVERED
    # live source (newest result yesterday): the result simply is not out yet
    idx = ResultsIndex(m, since=date(2026, 8, 1), as_of=date(2026, 9, 30))
    assert idx.resolve("ATP", "c", "d", "CHALLENGER", date(2026, 9, 30)).status == PENDING_RESULT
    # match inside the covered range with no result: genuinely not found
    assert idx.resolve("ATP", "c", "d", "CHALLENGER", date(2026, 9, 20)).status == NOT_FOUND
    # without a run date the original behaviour is kept exactly
    assert ResultsIndex(m, since=date(2026, 8, 1)).resolve("ATP", "c", "d", "CHALLENGER", date(2026, 10, 5)).status == NOT_COVERED


def test_exact_canonical_ids_only_and_ambiguity_stays():
    idx = ResultsIndex(_rows([ESPN_NEW, {**ESPN_NEW, "tourney_date": "2026-10-07"}]), since=date(2026, 8, 1),
                       as_of=date(2026, 10, 8))
    assert idx.resolve("WTA", "221012", "221406", "MASTERS_1000", date(2026, 10, 6)).status == AMBIGUOUS
    one = ResultsIndex(_rows([ESPN_NEW]), since=date(2026, 8, 1), as_of=date(2026, 10, 7))
    # a namesake id (another 'Qinwen Zheng' record) never matches: ids, not names
    assert one.resolve("WTA", "221012x", "221406", "MASTERS_1000", date(2026, 10, 5)).status != RESOLVED


def test_kalshi_outcome_cannot_masquerade_as_independent_truth():
    """The exchange said YES; with no independent row the prediction is not RESOLVED and nothing is reconciled."""
    idx = ResultsIndex(_rows([ESPN_OLD]), since=date(2026, 8, 1), as_of=date(2026, 10, 6))
    t = idx.resolve("WTA", "221012", "221406", "MASTERS_1000", date(2026, 10, 5))
    assert t.status != RESOLVED
    assert reconcile_match_winner(t, {"result": "yes"}, "221012")["status"] == "NOT_RECONCILED"


# ------------------------------------------------------------------------------------ end-to-end, append-only
def _ledger_row(pid, generated, models=True):
    return {"prediction_id": pid, "ticker": "KXWTAMATCH-26OCT05CHAZHE-ZHE", "match_id": "KXWTAMATCH-26OCT05CHAZHE",
            "event_ticker": "KXWTAMATCH-26OCT05CHAZHE", "family": "MATCH_WINNER", "tour": "WTA", "level": "MASTERS_1000",
            "player_a": "Qinwen Zheng", "player_b": "Alina Charaeva", "subject": "Qinwen Zheng",
            "player_a_id": "221012", "player_b_id": "221406", "generated_at_utc": generated,
            "models": {"V2": 0.75, "INCUMBENT": 0.72} if models else {}}


def _setup(tmp, matches_rows, espn_run):
    research = tmp / "research"
    (research / "ledger").mkdir(parents=True, exist_ok=True)
    (research / "settlements").mkdir(parents=True, exist_ok=True)
    (research / "ledger" / "2026-10-05.jsonl").write_text(json.dumps(_ledger_row("p1", "2026-10-05T18:00:00+00:00")) + "\n")
    (research / "settlements" / "1.jsonl").write_text(json.dumps(
        {"prediction_id": "p1", "gradeable": True, "exchange": {"result": "yes"},
         "sports": {"source": "kalshi_result", "winner_id": "221012"}}) + "\n")
    proc = tmp / f"processed_{espn_run}"
    proc.mkdir(exist_ok=True)
    m = _rows(matches_rows)
    m.to_parquet(proc / "matches.parquet")
    json.dump({"matches_sha256": hashlib.sha256(espn_run.encode()).hexdigest(), "build_version": "canonical_v2.3",
               "built_at": f"2026-10-06T{espn_run[-7:-1]}+00:00",
               "sources": {"espn_WTA": {"status": "OK", "run": espn_run}, "sackmann_WTA_main": {"status": "OK", "run": "20261005T123711Z"}}},
              open(proc / "build_manifest.json", "w"))
    return research, proc


def _digest(d):
    h = hashlib.sha256()
    for root, _ds, fs in sorted(os.walk(d)):
        for f in sorted(fs):
            h.update(f.encode()); h.update(open(os.path.join(root, f), "rb").read())
    return h.hexdigest()


def _run_truth(research, proc, as_of):
    r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "ops", "sports_truth.py"), "--research", str(research),
                        "--matches", str(proc / "matches.parquet"), "--as-of", as_of], capture_output=True, text=True, cwd=ROOT)
    assert r.returncode == 0, r.stderr
    return r.stdout


def test_pending_prediction_becomes_resolved_on_a_later_snapshot_without_rewriting_anything(tmp_path):
    research, proc_a = _setup(tmp_path, [SACKMANN_OLD, ESPN_OLD], "20261005T124930Z")
    ledger_digest = _digest(research / "ledger"); settle_digest = _digest(research / "settlements")
    _run_truth(research, proc_a, "2026-10-06")
    tdir = research / "sports_truth"
    first = sorted(tdir.glob("*.jsonl.gz"))
    assert len(first) == 1
    first_bytes = first[0].read_bytes()
    s1 = json.load(open(str(first[0]).replace(".jsonl.gz", ".summary.json")))
    assert s1["prospective_v2"]["independently_settled_matches"] == 0
    assert s1["prospective_v2"]["by_status"] == {PENDING_RESULT: 1}
    import time; time.sleep(1.1)                                         # distinct run id
    _, proc_b = _setup(tmp_path, [SACKMANN_OLD, ESPN_OLD, ESPN_NEW], "20261006T121558Z")
    _run_truth(research, proc_b, "2026-10-07")
    snaps = sorted(tdir.glob("*.jsonl.gz"))
    assert len(snaps) == 2 and snaps[0].read_bytes() == first_bytes      # the earlier snapshot is untouched
    cur = tf.current_snapshot(str(tdir))
    assert cur == str(snaps[1])
    rows = tf.read_snapshot(cur)
    assert rows[0]["independent"]["status"] == RESOLVED and rows[0]["reconciliation"]["status"] == "AGREE"
    assert rows[0]["provenance"]["espn_runs"] == ["20261006T121558Z"]
    s2 = json.load(open(cur.replace(".jsonl.gz", ".summary.json")))
    assert s2["prospective_v2"]["independently_settled_matches"] == 1
    logs = sorted((tdir / "resolution_log").glob("*.jsonl"))
    assert len(logs) == 1 and json.loads(logs[0].read_text())["prediction_id"] == "p1"
    # no ledger or settlement row was rewritten
    assert _digest(research / "ledger") == ledger_digest and _digest(research / "settlements") == settle_digest


def test_a_run_on_older_sources_never_becomes_current(tmp_path):
    """Result-refresh sequencing: RUN TENNIS pulled its sources before the ESPN publish but finished after the truth
    refresh. Its snapshot has the later run id and must still not become current."""
    research, proc_new = _setup(tmp_path, [SACKMANN_OLD, ESPN_OLD, ESPN_NEW], "20261006T121558Z")
    _run_truth(research, proc_new, "2026-10-06")
    tdir = research / "sports_truth"
    refreshed = sorted(tdir.glob("*.jsonl.gz"))[0]
    import time; time.sleep(1.1)
    _, proc_old = _setup(tmp_path, [SACKMANN_OLD, ESPN_OLD], "20261005T124930Z")
    out = _run_truth(research, proc_old, "2026-10-06")
    assert "older sources" in out
    assert tf.current_snapshot(str(tdir)) == str(refreshed)
    assert json.load(open(tdir / "latest_summary.json"))["run_id"] == refreshed.name.split(".")[0]


def test_prospective_summary_counts_only_v2_era_predictions_with_both_probabilities():
    rows = [{"prediction_id": p, "tour": "WTA", "level": "MASTERS_1000", "independent": {"status": RESOLVED},
             "reconciliation": {"status": "AGREE"}} for p in ("a", "b", "c")]
    ledger = {"a": _ledger_row("a", "2026-10-05T18:00:00+00:00"),
              "b": _ledger_row("b", "2026-10-05T10:00:00+00:00"),                # before the first V2 run
              "c": _ledger_row("c", "2026-10-05T18:00:00+00:00", models=False)}  # no V2 / incumbent pair
    s = tf.prospective_summary(rows, ledger, as_of=date(2026, 10, 7))
    assert s["predictions_with_v2_and_incumbent"] == 1 and s["independently_settled_matches"] == 1
    assert s["by_level"] == {"WTA tour": {RESOLVED: 1}} and s["readout_at_independently_settled_matches"] == 1500
    assert not any(k in json.dumps(s) for k in ("brier", "log_loss", "auc"))          # counts only, no scoring


def test_stale_tour_level_prediction_raises_the_operational_warning():
    rows = [{"prediction_id": "a", "tour": "WTA", "level": "MASTERS_1000", "independent": {"status": NOT_FOUND},
             "reconciliation": {"status": "NOT_RECONCILED"}}]
    s = tf.prospective_summary(rows, {"a": _ledger_row("a", "2026-10-05T18:00:00+00:00")}, as_of=date(2026, 10, 12))
    assert s["n_stale_unresolved_tour_level"] == 1
    s = tf.prospective_summary(rows, {"a": _ledger_row("a", "2026-10-05T18:00:00+00:00")}, as_of=date(2026, 10, 7))
    assert s["n_stale_unresolved_tour_level"] == 0


def test_truth_refresh_triggers_on_unused_evidence_not_on_the_clock(tmp_path):
    """Delayed GitHub schedule: whenever the refresh finally runs, it rebuilds iff the newest ESPN snapshot is unused."""
    from scripts.ops.truth_refresh_needed import newest_espn, used_espn
    src = tmp_path / "sources" / "espn"
    for r in ("20261005T124930Z", "20261006T121558Z"):
        (src / r).mkdir(parents=True)
        (src / r / "espn_matches_WTA_2026.csv.gz").write_bytes(b"x")
    (src / "20261007T000000Z").mkdir()
    (src / "20261007T000000Z" / "espn_matches_WTA_2026.csv.gz").write_bytes(b"x")
    (src / "20261007T000000Z" / "QUARANTINED.md").write_text("bad")
    tdir = tmp_path / "research" / "sports_truth"; tdir.mkdir(parents=True)
    assert newest_espn(str(tmp_path / "sources")) == "20261006T121558Z"
    json.dump({"provenance": {"espn_runs": ["20261005T124930Z"]}}, open(tdir / "a.meta.json", "w"))
    run = lambda: subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "ops", "truth_refresh_needed.py"),
                                  "--data-root", str(tmp_path)], capture_output=True, cwd=ROOT).returncode
    assert run() == 0
    json.dump({"provenance": {"espn_runs": ["20261006T121558Z"]}}, open(tdir / "b.meta.json", "w"))
    assert run() == 10


# --------------------------------------------------------------------------------------------- ESPN refresh
def _espn(rows):
    return pd.DataFrame([{"tourney_id": t, "match_num": n, "winner_id": w, "loser_id": l, "score": "6-4 6-4",
                          "tourney_date": d, "round": "R32", "_tour": "WTA"} for t, n, w, l, d in rows])


def test_incremental_refresh_carries_forward_and_never_drops_a_row():
    from fetch_espn_results import consolidate
    base = _espn([("t1", "1", "a", "b", "20260614"), ("t2", "2", "c", "d", "20261001")])
    fetched = _espn([("t2", "2", "c", "d", "20261001"), ("t3", "3", "e", "f", "20261006")])
    out, audit = consolidate(base, fetched, date(2026, 9, 22), date(2026, 10, 6))
    assert set(out["tourney_id"]) == {"t1", "t2", "t3"} and len(out) == 3
    assert audit["added"] == 1 and audit["changed"] == 0 and audit["carried_forward"] == 1


def test_full_refresh_audits_changes_and_keeps_missing_rows():
    from fetch_espn_results import consolidate
    base = _espn([("t1", "1", "a", "b", "20261001"), ("t2", "2", "c", "d", "20261002")])
    fetched = _espn([("t1", "1", "b", "a", "20261001")])                        # winner corrected; t2 not listed
    out, audit = consolidate(base, fetched, date(2026, 4, 1), date(2026, 10, 6))
    assert audit["changed"] == 1 and audit["missing_in_refetch"] == 1
    assert set(out["tourney_id"]) == {"t1", "t2"}                               # flagged, never silently deleted
    assert out.set_index("tourney_id").at["t1", "winner_id"] == "b"             # the newest fetch wins its key


def test_refresh_mode_selection():
    from fetch_espn_results import choose_mode
    base = {"since": "2026-04-01", "until": "2026-10-05"}
    assert choose_mode("auto", base, date(2026, 10, 6), 14, 6) == "incremental"   # a Tuesday
    assert choose_mode("auto", base, date(2026, 10, 11), 14, 6) == "full"          # Sunday audit
    assert choose_mode("auto", {}, date(2026, 10, 6), 14, 6) == "full"             # no base
    assert choose_mode("auto", base, date(2026, 10, 6), 14, 6, explicit_since=True) == "full"
    assert choose_mode("incremental", {}, date(2026, 10, 6), 14, 6) == "full"      # nothing to carry forward


# ------------------------------------------------------------------------------------------- capture conductor
def test_tail_hash_matches_the_full_scan_and_rows_are_identical(tmp_path):
    from tennis_edge.external_market.dislocation import DislocationLedger, Dislocation
    from tennis_edge.external_market.tail_hash import TailHashLedger, full_scan_hash, last_row_hash
    import dataclasses
    fields = {f.name: None for f in dataclasses.fields(Dislocation)
              if f.default is dataclasses.MISSING and f.default_factory is dataclasses.MISSING}
    rows = [Dislocation(**{**fields, "generated_at": f"2026-10-06T10:{i:02d}:00+00:00", "kalshi_ticker": f"T{i}",
                           "external_sources": (), "external_prices": {}, "external_raw": {}, "decision": "PASS"}) for i in range(30)]
    a, b = DislocationLedger(str(tmp_path / "old")), TailHashLedger(str(tmp_path / "new"))
    for r in rows:
        a.append(r); b.append(r)
    old = (tmp_path / "old" / "2026-10-06.jsonl").read_bytes()
    assert old == (tmp_path / "new" / "2026-10-06.jsonl").read_bytes()
    p = str(tmp_path / "new" / "2026-10-06.jsonl")
    assert last_row_hash(p) == full_scan_hash(p) and b.verify_chain() == []
    assert last_row_hash(str(tmp_path / "absent.jsonl")) == "GENESIS"


def test_external_store_shards_per_pass_and_chains_continue(tmp_path):
    from tennis_edge.external_market.schema import ExternalStore
    s1 = ExternalStore(str(tmp_path), shard="20261006T100000Z")
    assert s1._path("2026-10-06").endswith("2026-10-06.20261006T100000Z.jsonl")
    assert ExternalStore(str(tmp_path))._path("2026-10-06").endswith("2026-10-06.jsonl")


def test_restore_continues_the_days_ledger_instead_of_replacing_it(tmp_path):
    """A new conductor used to start with an empty day file and replace the branch's (2026-10-06: the tip kept only
    rows from 13:50Z). restore_day_files copies the branch's copy first; an existing local copy is never touched."""
    from scripts.ci.restore_day_files import restore
    repo = tmp_path / "repo"; repo.mkdir()
    g = lambda *a: subprocess.run(["git", *a], cwd=repo, check=True, capture_output=True)
    g("init", "-q"); g("config", "user.email", "t@t"); g("config", "user.name", "t")
    p = repo / "tennis-edge-finder" / "data" / "research" / "external" / "dislocations"
    p.mkdir(parents=True)
    (p / "2026-10-06.jsonl").write_text('{"row_hash":"h1","prev_hash":"GENESIS"}\n')
    g("add", "-A"); g("commit", "-qm", "x"); g("branch", "-M", "tennis-data")
    g("update-ref", "refs/remotes/origin/tennis-data", "HEAD")
    work = repo  # restore() reads origin/<branch> in the given repo
    out = restore(str(work), "tennis-data", "tennis-edge-finder", ["research/external/dislocations"], "2026-10-06")
    local = work / "data" / "research" / "external" / "dislocations" / "2026-10-06.jsonl"
    assert "restored" in out["research/external/dislocations"] and "h1" in local.read_text()
    local.write_text(local.read_text() + '{"row_hash":"h2","prev_hash":"h1"}\n')
    out = restore(str(work), "tennis-data", "tennis-edge-finder", ["research/external/dislocations"], "2026-10-06")
    assert out["research/external/dislocations"] == "local copy kept" and "h2" in local.read_text()
    out = restore(str(work), "tennis-data", "tennis-edge-finder", ["research/external/dislocations"], "2026-10-07")
    assert "absent" in out["research/external/dislocations"]


def _bash(fn, *args):
    r = subprocess.run(["bash", "-c", f"source scripts/ci/conductor_clock.sh; {fn} {' '.join(map(str, args))}"],
                       cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip()


def test_conductor_cadence_is_start_to_start_and_an_overrun_starts_promptly():
    now, end = 10_000, 100_000
    assert _bash("conductor_sleep", now, end, 600, 240) == "360"     # 4 min of work -> sleep 6: one start per 10 min
    assert _bash("conductor_sleep", now, end, 600, 900) == "0"       # overran: next pass starts at once, never overlaps


def test_pass_record_measures_start_to_start_and_overrun():
    from scripts.ci.pass_record import build
    t0 = 1_760_000_000_000
    r = build(3, "run", t0, t0 - 600_000, 600, 360, {"fetch": 3.0, "external_scan": 150.0}, t0 + 240_000)
    assert r["start_to_start_s"] == 600 and r["work_s"] == 240 and r["overrun_s"] == 0
    r = build(4, "run", t0, t0 - 900_000, 600, 0, {"external_scan": 800.0}, t0 + 900_000)
    assert r["overrun_s"] == 300 and r["start_to_start_s"] == 900


def test_workflows_keep_single_writers():
    """No overlapping publishers: one capture conductor at a time, RUN TENNIS never re-publishes the conductor's tree,
    and the truth refresh publishes sports truth only."""
    import yaml
    cap = yaml.safe_load(open(os.path.join(ROOT, ".github", "workflows", "tennis-capture.yml")))
    assert cap["concurrency"]["group"] == "tennis-capture-conductor" and cap["concurrency"]["cancel-in-progress"] is False
    run = open(os.path.join(ROOT, ".github", "workflows", "tennis-run.yml")).read()
    assert "--src data/research --exclude external" in run
    tr = open(os.path.join(ROOT, ".github", "workflows", "tennis-truth-refresh.yml")).read()
    pubs = [ln for ln in tr.splitlines() if "publish_branch.py" in ln]
    assert len(pubs) == 1 and "--src data/research/sports_truth" in pubs[0]
    trw = yaml.safe_load(tr)
    on = trw.get(True) or trw.get("on")
    assert "workflow_call" in on and "push" not in on and "schedule" in on
    boot = yaml.safe_load(open(os.path.join(ROOT, ".github", "workflows", "tennis-bootstrap.yml")))
    job = boot["jobs"]["truth"]
    assert job["needs"] == "sources" and job["uses"].endswith("tennis-truth-refresh.yml")


def test_publish_exclude(tmp_path):
    from scripts.ci.publish_branch import plan
    (tmp_path / "external" / "market").mkdir(parents=True)
    (tmp_path / "external" / "market" / "x.jsonl").write_text("1")
    (tmp_path / "ledger").mkdir()
    (tmp_path / "ledger" / "y.jsonl").write_text("1")
    assert [r for r, _ in plan(str(tmp_path), ["external"])] == ["ledger/y.jsonl"]
    assert len(plan(str(tmp_path))) == 2


def test_small_publish_checks_out_only_the_files_it_writes(tmp_path):
    """The conductor's first pass spent 286 s of its 600 s interval because the publisher checked out whole directories
    (research/external/market ~1 GB, raw/ 4,397 payloads) to add five files. A small publish now matches exactly its
    own paths -- including names with glob characters -- and nothing else in those directories."""
    from scripts.ci.publish_branch import EXACT_SPARSE_MAX, sparse_patterns
    run = lambda *a: subprocess.run(["git", *a], cwd=tmp_path, check=True, capture_output=True, text=True).stdout
    run("init", "-q", "-b", "tennis-data")
    run("config", "user.email", "t@example.com"); run("config", "user.name", "t")
    d = tmp_path / "p" / "market"
    d.mkdir(parents=True)
    for n in ("2026-10-05.jsonl", "2026-10-06.a.jsonl", "we ird[1]*.json", "#x.json"):
        (d / n).write_text(n)
    run("add", "-A"); run("commit", "-q", "-m", "seed")
    pats = sparse_patterns("p", [("market/2026-10-06.a.jsonl", ""), ("market/we ird[1]*.json", ""), ("market/#x.json", "")])
    run("sparse-checkout", "init", "--no-cone")
    run("sparse-checkout", "set", "--no-cone", *pats)
    assert sorted(x.name for x in d.iterdir()) == ["#x.json", "2026-10-06.a.jsonl", "we ird[1]*.json"]
    many = [(f"market/f{i}.json", "") for i in range(EXACT_SPARSE_MAX + 1)]
    assert sparse_patterns("p", many) == ["/p/market/*"]


def test_espn_retirement_is_kept_not_quarantined():
    """STATUS_RETIRED used to come through as a bare partial score ('5-2') that the validator quarantined, so every
    ESPN retirement was missing from independent truth (Svrcina d. Nishioka 5-2 ret, Shanghai Q3, 2026-10-06)."""
    from tennis_edge.data.espn_results import parse_scoreboard
    def comp(cid, status, w, l, wls, lls, note):
        return {"id": cid, "date": "2026-10-06T05:00Z", "status": {"type": {"name": status, "state": "post", "completed": True,
                "description": status.title()}}, "notes": [{"text": note}], "round": {"displayName": "Qualifying Final"},
                "competitors": [{"id": w, "winner": True, "athlete": {"displayName": w}, "linescores": [{"value": v} for v in wls]},
                                {"id": l, "winner": False, "athlete": {"displayName": l}, "linescores": [{"value": v} for v in lls]}]}
    payload = {"events": [{"id": "1", "name": "Rolex Shanghai Masters", "groupings": [{"grouping": {"id": "g", "slug": "mens-singles"},
               "competitions": [comp("1", "STATUS_RETIRED", "Dalibor Svrcina", "Yoshihito Nishioka", [5], [2], "Svrcina bt Nishioka 5-2 ret"),
                                comp("2", "STATUS_FINAL", "A Player", "B Player", [6, 6], [4, 4], "A bt B 6-4 6-4")]}]}]}
    df = parse_scoreboard(payload, "atp").set_index("winner_name")
    assert df.at["Dalibor Svrcina", "score"] == "5-2 RET" and df.at["A Player", "score"] == "6-4 6-4"
    from tennis_edge.rules.score_parser import parse_score
    assert parse_score("5-2 RET").outcome_type == "RETIRED"
