#!/usr/bin/env python3
"""Harvest and score the prospective evidence for every frozen edge candidate.

    python scripts/research/harvest_candidate_evidence.py [--data-root data]

Reads (never writes):
  <data-root>/research/edge_candidates/*.json    the frozen definitions (fingerprints re-verified)
  <data-root>/research/external/...              dislocation ledger + external venue store
  <data-root>/research/ledger, opportunities     prediction streams
  <data-root>/firstball/store                    first-ball truth
  <data-root>/kalshi/capture                     quotes, books, candles, settlements

Writes a DERIVED layer only:
  data/research/candidate_evidence/<id>.evidence.jsonl            append-only, hash-chained evidence rows
  data/research/candidate_evidence/<id>.exclusions.<run>.jsonl.gz why every other post-freeze row failed
  data/research/candidate_evidence/harvest_runs.jsonl             one line per harvest: inputs, counts, statuses
  research/candidate_confirmation/*.json, *.md                    scoring reports (regenerated each run)

The candidate definition files are hashed before and after the harvest; if a single byte changed, the run
fails. Nothing here fits, tunes or re-specifies anything. Real-money authority is OFF.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.confirmation import candidates as C          # noqa: E402
from tennis_edge.confirmation import scorecards as SC         # noqa: E402
from tennis_edge.confirmation import sources as src           # noqa: E402
from tennis_edge.confirmation.evidence import EvidenceStore   # noqa: E402


def _hash_files(paths):
    return {os.path.basename(p): hashlib.sha256(open(p, "rb").read()).hexdigest() for p in sorted(paths)}


def _fmt(x, pct=False, nd=4):
    if x is None:
        return "--"
    if isinstance(x, float):
        return f"{x * 100:+.2f}c" if pct else f"{x:.{nd}f}"
    return str(x)


def _ci(m, pct=True):
    if not m or m.get("mean") is None:
        return "n/a"
    lo, hi = m.get("ci_low"), m.get("ci_high")
    s = f"{_fmt(m['mean'], pct)} (n={m['n']}"
    if lo is not None:
        s += f", 95% CI [{_fmt(lo, pct)}, {_fmt(hi, pct)}]"
    return s + ")"


STATUS_FILE = "HARVEST_STATUS.json"


def record_status(report_out: str, *, success: bool, run: str, detail: str = "", statuses: dict | None = None):
    """Keep the last success and the last failure side by side. A failure never erases the last success,
    and a success never erases the record of the last failure: TENNIS-15 compares the two."""
    os.makedirs(report_out, exist_ok=True)
    path = os.path.join(report_out, STATUS_FILE)
    try:
        st = json.load(open(path))
    except (OSError, ValueError):
        st = {}
    now = datetime.now(timezone.utc).isoformat()
    st["last_attempt"] = now
    if success:
        st["last_success"] = now
        st["last_success_run"] = run
        st["statuses"] = statuses or {}
    else:
        st["last_failure"] = now
        st["last_failure_detail"] = detail[-2000:]
    json.dump(st, open(path, "w"), indent=1)
    return st


def main():
    import traceback
    ap_ = argparse.ArgumentParser(add_help=False)
    ap_.add_argument("--report-out", default=os.path.join(PROJ, "research", "candidate_confirmation"))
    ap_.add_argument("--record-failure", default=None)
    known, _ = ap_.parse_known_args()
    if known.record_failure is not None:
        record_status(known.report_out, success=False, run="", detail=known.record_failure)
        return 0
    try:
        return _main()
    except BaseException as e:                                       # noqa: BLE001
        if isinstance(e, SystemExit) and e.code in (0, None):
            raise
        record_status(known.report_out, success=False, run="", detail=traceback.format_exc())
        raise


def _main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--record-failure", default=None)
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--candidates", default=None, help="frozen candidate dir (default <data-root>/research/edge_candidates)")
    ap.add_argument("--discovery", default=None, help="discovery snapshot for the settled-market fallback")
    ap.add_argument("--evidence-out", default=os.path.join(PROJ, "data", "research", "candidate_evidence"))
    ap.add_argument("--report-out", default=os.path.join(PROJ, "research", "candidate_confirmation"))
    ap.add_argument("--source-label", default=os.environ.get("EVIDENCE_SOURCE_LABEL", ""),
                    help="where the evidence came from, e.g. tennis-data@<sha>; recorded in the harvest log")
    a = ap.parse_args()

    run = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    cand_dir = a.candidates or os.path.join(a.data_root, "research", "edge_candidates")
    cand_files = glob.glob(os.path.join(cand_dir, "*.json"))
    before = _hash_files(cand_files)
    cands = src.load_candidates(cand_dir)
    bad_fp = [cid for cid, c in cands.items() if not c["_fingerprint_ok"]]
    if bad_fp:
        raise SystemExit(f"frozen definition fingerprint mismatch (edited after freeze?): {bad_fp}")

    capture = os.path.join(a.data_root, "kalshi", "capture")
    disc = a.discovery
    if disc is None:
        runs = sorted(glob.glob(os.path.join(a.data_root, "kalshi", "discovery", "*", "summary.json")))
        disc = os.path.dirname(runs[-1]) if runs else None
    ctx = C.Context(data_root=a.data_root, candidates=cands,
                    truths=src.first_ball_truths(os.path.join(a.data_root, "firstball", "store")),
                    settlements=src.settlements(capture, disc), capture_root=capture)

    store = EvidenceStore(a.evidence_out)
    os.makedirs(a.report_out, exist_ok=True)
    results = {}
    for cid in sorted(cands):
        h = C.HARVESTERS.get(cid)
        if h is None:
            print(f"{cid}: no harvester (not one of the seven audited candidates)")
            continue
        res = h(ctx, cands[cid])
        written = store.append_new(cid, res.evidence_rows, run)
        if res.exclusions:
            C.write_exclusions(os.path.join(a.evidence_out, f"{cid}.exclusions.{run}.jsonl.gz"), res.exclusions)
        rep = res.report()
        caps = [r.captured_at for r in res.evidence_rows if r.captured_at]
        rep.update(harvest_run=run, evidence_rows_this_run=len(res.evidence_rows), evidence_rows_appended=written,
                   last_evidence_at=max(caps) if caps else None,
                   harvest_run_at=datetime.now(timezone.utc).isoformat(),
                   evidence_chain_violations=store.verify_chain(cid),
                   frozen_definition={k: cands[cid][k] for k in (
                       "frozen_at", "confirmation_start", "minimum_n", "inclusion_rule",
                       "required_accuracy_condition", "required_clv_condition", "required_after_fee_condition",
                       "model_version", "status")},
                   frozen_definition_fingerprint=cands[cid]["_fingerprint_recomputed"])
        json.dump(rep, open(os.path.join(a.report_out, f"{cid}.json"), "w"), indent=1, default=str)
        results[cid] = res
        print(f"{cid:36s} {res.status:38s} {res.status_reason}")

    # ---------------------------------------------------------------- descriptive scorecards
    ledger = SC.ledger_rows(a.data_root)
    pairs = SC.recompute_clv(ctx, ledger)
    clv = SC.clv_scorecard(pairs)
    published = sorted(glob.glob(os.path.join(a.data_root, "research", "clv", "*.jsonl")))
    if published:
        n_pub = sum(1 for _f, _h, r in src.iter_jsonl(published[-1]) if r.get("strict"))
        clv["published_clv_run"] = os.path.basename(published[-1])
        clv["published_strict_rows"] = n_pub
    json.dump(clv, open(os.path.join(a.report_out, "CLV_SCORECARD.json"), "w"), indent=1, default=str)

    w4 = cands.get("W4-2026-001-KALSHI-LONE-OUTLIER")
    ext = SC.external_scorecard(a.data_root, w4["confirmation_start"] if w4 else "",
                                results["W4-2026-001-KALSHI-LONE-OUTLIER"].evidence_rows if w4 else None)
    json.dump(ext, open(os.path.join(a.report_out, "EXTERNAL_SCORECARD.json"), "w"), indent=1, default=str)

    audit = SC.settlement_audit(a.data_root, ctx.settlements, ledger)
    from tennis_edge.health.gates import settlement_stats
    st = settlement_stats(os.path.join(a.data_root, "research")) or {}
    st.pop("_strict_research_rows", None)
    audit["health_layer_view_after_fix"] = st
    json.dump(audit, open(os.path.join(a.report_out, "SETTLEMENT_AUDIT.json"), "w"), indent=1, default=str)

    # ---------------------------------------------------------------- immutability check, then the log
    after = _hash_files(cand_files)
    if before != after:
        raise SystemExit("a frozen candidate definition changed during the harvest -- refusing to record the run")
    log = {"harvest_run": run, "evidence_source": a.source_label or "unspecified",
           "data_root": os.path.relpath(os.path.abspath(a.data_root), PROJ) if os.path.abspath(a.data_root).startswith(PROJ)
           else "external checkout of the evidence branch",
           "discovery": os.path.basename(disc) if disc else None,
           "candidate_definition_sha256": before,
           "inputs": {"first_ball_truths": len(ctx.truths), "settlement_records": len(ctx.settlements),
                      "ledger_rows": len(ledger)},
           "statuses": {cid: r.status for cid, r in results.items()},
           "eligible_n": {cid: (r.summary.eligible_n if r.summary else None) for cid, r in results.items()},
           "authority": "RESEARCH_ONLY_NO_REAL_MONEY"}
    with open(os.path.join(a.evidence_out, "harvest_runs.jsonl"), "a") as f:
        f.write(json.dumps(log, default=str) + "\n")

    # versioned derived view: strict CLV through a sibling event of the same canonical physical match
    sib = SC.sibling_join_clv(ctx, ledger, pairs)
    sib_rows = sib.pop("rows")
    sib_dir = os.path.join(os.path.dirname(os.path.abspath(a.evidence_out)), "clv_physical_join")
    os.makedirs(sib_dir, exist_ok=True)
    with open(os.path.join(sib_dir, f"{run}.jsonl"), "w") as f:
        for d in sib_rows:
            f.write(json.dumps(d, default=str) + "\n")
    json.dump(sib, open(os.path.join(a.report_out, "CLV_SIBLING_JOIN.json"), "w"), indent=1, default=str)
    json.dump(SC.weekly_match_winner_clv(pairs), open(os.path.join(a.report_out, "MATCH_WINNER_WEEKLY_CLV.json"), "w"),
              indent=1, default=str)

    write_summary(os.path.join(a.report_out, "SUMMARY.md"), run, results, clv, ext, audit)
    record_status(a.report_out, success=True, run=run, statuses={cid: r.status for cid, r in results.items()})
    return 0


def write_summary(path, run, results, clv, ext, audit):
    L = [f"# Prospective candidate confirmation -- harvest {run}", "",
         "Generated by `scripts/research/harvest_candidate_evidence.py`. Real-money authority is OFF.", "",
         "| candidate | status | eligible N | min N | settled | strict CLV | reason |", "|---|---|---|---|---|---|---|"]
    for cid, r in results.items():
        s = r.summary
        L.append(f"| {cid} | **{r.status}** | {s.eligible_n} | {s.minimum_n} | {s.settled_n} | {s.strict_clv_n} | {r.status_reason} |")
    w4 = results.get("W4-2026-001-KALSHI-LONE-OUTLIER")
    if w4:
        m = w4.metrics
        L += ["", "## W4-2026-001 (the one fully scorable trade candidate)", "",
              f"* first qualifying observations: {w4.universe.get('first_qualifying_observations')} "
              f"(by timing {w4.universe.get('first_qualifying_by_timing')})",
              f"* eligible (STRICT_PREGAME first observations): {m['eligible_n']}; settled {m['settled_n']}; strict CLV {m['strict_clv_n']}",
              f"* Brier external - Kalshi mid: {_ci(m['brier_diff_external_minus_mid'], pct=False)}",
              f"* strict executable CLV: {_ci(m['strict_executable_clv'])}",
              f"* after-fee P&L per contract: {_ci(m['after_fee_pnl_per_contract'])}"]
    L += ["", "## Strict CLV (view B: one row per physical decision)", "",
          "| family | n | mean exec CLV | median | 95% CI | mean mid CLV | mean spread | mean fee | median h to first ball |",
          "|---|---|---|---|---|---|---|---|---|"]
    for fam, c in clv["views"]["B_one_row_per_physical_decision"]["by_family"].items():
        L.append(f"| {fam} | {c['n']} | {_fmt(c['mean_exec_clv'], True)} | {_fmt(c['median_exec_clv'], True)} | "
                 f"[{_fmt(c['ci95'][0], True)}, {_fmt(c['ci95'][1], True)}] | {_fmt(c['mean_mid_clv'], True)} | "
                 f"{_fmt(c['mean_entry_spread'], True)} | {_fmt(c['mean_entry_fee'], True)} | {_fmt(c['median_hours_entry_to_first_ball'], nd=1)} |")
    L += ["", f"External board since the W4 freeze: {ext['dislocation_rows']} rows, {ext['matched_matches']} matches, "
          f"{ext['matched_contracts']} contracts, triangulation {ext['triangulation_rows']}.", "",
          f"Settlement: {audit['settlement_rows_unique']} unique settled rows covering {audit['ledger_rows_settled']} of "
          f"{audit['ledger_rows']} ledger rows ({audit['settlement_rows_not_in_ledger']} settlement rows not in the ledger); "
          f"{audit['settlement_vs_capture_result_conflicts']} conflicts with the capture settlement stream."]
    open(path, "w").write("\n".join(L) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
