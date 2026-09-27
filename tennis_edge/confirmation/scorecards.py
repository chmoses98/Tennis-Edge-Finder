"""Descriptive prospective scorecards: strict CLV by family, the external-market board, settlement.

These are MONITORING tables. None of them is a candidate, none of them selects anything, and the
"model-directed" CLV view below uses the side the ledger row itself named when it was written -- it is a
description of the Gen-1 lane's direction, not a rule and not evidence for any frozen candidate.
"""
from __future__ import annotations

import glob
import os
from collections import Counter, defaultdict
from statistics import median

from tennis_edge.confirmation import sources as src
from tennis_edge.confirmation import stats
from tennis_edge.firstball.classify import STRICT_PREGAME, classify
from tennis_edge.ledger.close import Quote, canonical_close
from tennis_edge.ledger.clv import clv_record
from tennis_edge.pricing.fees import FeeSchedule

FAMILY_ORDER = ("MATCH_WINNER", "SET_WINNER", "EXACT_SET_SCORE", "TOTAL_GAMES", "GAME_SPREAD")
#: families whose YES contracts come in complementary pairs on one physical question (A wins / B wins)
PAIRED_FAMILIES = ("MATCH_WINNER", "SET_WINNER")


def ledger_rows(data_root: str) -> list[dict]:
    return [r for _f, _h, r in src.iter_jsonl(os.path.join(data_root, "research", "ledger", "*.jsonl"))]


def recompute_clv(ctx, rows: list[dict]) -> list[tuple[dict, object]]:
    """(ledger row, ClvRecord) for every ledger row, against the LATEST first-ball truth and the full
    capture quote timeline (market records, order books, candles). Same engine as the settle job."""
    qmap = ctx.quotes({r["ticker"] for r in rows})
    out = []
    for r in rows:
        truth = ctx.truths.get(r["match_id"])
        gen = src.iso(r["generated_at_utc"])
        tc = classify(gen, truth)
        cc = canonical_close(qmap.get(r["ticker"], []), truth)
        dq = r.get("market_quote") or {}
        entry = Quote(gen, dq.get("yes_bid"), dq.get("yes_ask"), no_bid=dq.get("no_bid"), no_ask=dq.get("no_ask"))
        rec = clv_record(prediction_id=r["prediction_id"], ticker=r["ticker"], match_id=r["match_id"],
                         family=r["family"], entry=entry, close=cc, truth=truth, timing=tc,
                         tour=r.get("tour", ""), level=r.get("level", ""),
                         model_prob=(r.get("models") or {}).get("ELO_DP_FAIR"),
                         data_quality_grade=(r.get("quality") or {}).get("grade", ""),
                         fee_schedule=FeeSchedule(fee_type=r.get("fee_type") or "quadratic"))
        out.append((r, rec))
    return out


def _family_key(r: dict) -> str:
    fam = r.get("family") or "UNKNOWN"
    if fam == "MATCH_WINNER" and (r.get("model_version") or "").startswith("doubles"):
        return "MATCH_WINNER (doubles)"
    return fam if fam in FAMILY_ORDER else f"other: {fam}"


def _cell(recs: list, clv_of=lambda rec, r: rec.clv_executable) -> dict:
    exe = [clv_of(rec, r) for r, rec in recs]
    mid = [rec.clv_midpoint for _r, rec in recs]
    ci = stats.mean_ci(exe)
    hz = [rec.seconds_entry_to_first_ball for _r, rec in recs if rec.seconds_entry_to_first_ball is not None]
    return {"n": len(recs), "mean_exec_clv": ci["mean"], "median_exec_clv": ci["median"],
            "ci95": [ci["ci_low"], ci["ci_high"]], "excludes_zero": ci["excludes_zero"],
            "share_positive": (sum(1 for x in exe if x > 0) / len(exe)) if exe else None,
            "mean_mid_clv": stats.mean_ci(mid)["mean"],
            "mean_entry_spread": (sum(rec.entry_spread for _r, rec in recs if rec.entry_spread is not None) / len(recs)) if recs else None,
            "mean_entry_fee": (sum(rec.entry_taker_fee_per_contract or 0 for _r, rec in recs) / len(recs)) if recs else None,
            "median_hours_entry_to_first_ball": (median(hz) / 3600) if hz else None}


def _physical_key(r: dict) -> tuple:
    return ((r["match_id"].split("-") + [""])[1], r["family"], r.get("set_index"), r.get("line"),
            tuple(r["exact_score"]) if r.get("exact_score") else None)


def clv_scorecard(pairs: list) -> dict:
    strict = [(r, rec) for r, rec in pairs if rec.strict]
    out = {"ledger_rows": len(pairs), "strict_rows": len(strict),
           "timing_classes": dict(Counter(rec.timing_class for _r, rec in pairs)),
           "close_basis": dict(Counter(rec.close_basis for _r, rec in pairs)),
           "views": {}}
    # A. every strict observation: both sides of every binary pair, every re-pricing of a contract
    by = defaultdict(list)
    for r, rec in strict:
        by[_family_key(r)].append((r, rec))
    out["views"]["A_all_strict_observations"] = {
        "label": "every strict row; BOTH sides of each binary pair and every re-pricing run are included, so "
                 "the mean is the average cost of crossing the spread in both directions, not a strategy",
        "by_family": {k: _cell(v) for k, v in sorted(by.items())}}
    # B. one row per physical decision: earliest strict observation of each physical question, canonical side
    first = {}
    for r, rec in sorted(strict, key=lambda x: x[0]["generated_at_utc"]):
        if r["family"] in PAIRED_FAMILIES and r.get("subject") != r.get("player_a"):
            continue                                   # keep side A only: one question, one row
        k = _physical_key(r) + ((r["ticker"],) if r["family"] not in PAIRED_FAMILIES else ())
        first.setdefault(k, (r, rec))
    by = defaultdict(list)
    for r, rec in first.values():
        by[_family_key(r)].append((r, rec))
    out["views"]["B_one_row_per_physical_decision"] = {
        "label": "earliest STRICT_PREGAME observation of each physical question; for paired families only the "
                 "side-A contract is kept, so each question counts once; a YES-at-the-ask entry",
        "by_family": {k: _cell(v) for k, v in sorted(by.items())}}

    # C. the direction the ledger row itself named (ev.best_side), on the same one-per-question rows
    def directed(rec, r):
        side = (r.get("ev") or {}).get("best_side")
        if side == "NO":
            return rec.entry_yes_bid - rec.close_yes_ask       # bought NO at 1-bid, NO bid at close = 1-ask
        return rec.clv_executable
    by = defaultdict(list)
    for r, rec in first.values():
        if (r.get("ev") or {}).get("best_side") in ("YES", "NO"):
            by[_family_key(r)].append((r, rec))
    out["views"]["C_model_directed_descriptive"] = {
        "label": "DESCRIPTIVE ONLY: the side the Gen-1 ledger row named at capture (ev.best_side), whatever its "
                 "EV; not a selection rule, not a candidate, and not evidence for any frozen claim",
        "by_family": {k: _cell(v, directed) for k, v in sorted(by.items())}}
    return out


def external_scorecard(data_root: str, since: str, w4_rows: list | None = None) -> dict:
    rows = [r for _f, _h, r in src.iter_jsonl(os.path.join(data_root, "research", "external", "dislocations", "*.jsonl"))]
    post = [r for r in rows if (r.get("generated_at") or "") >= since]

    def srcs(r):
        return {s for s, p in (r.get("external_prices") or {}).items() if p is not None}
    tri_rows = Counter(r.get("triangulation") for r in post)
    tri_contracts = defaultdict(set)
    for r in post:
        tri_contracts[r.get("triangulation")].add(r.get("kalshi_ticker"))
    scans = glob.glob(os.path.join(data_root, "research", "external", "scans", "scan_*.json"))
    compact = since[:19].replace("-", "").replace(":", "")
    out = {"since": since, "scan_passes": sum(1 for p in scans if os.path.basename(p)[5:20] >= compact),
           "dislocation_rows": len(post),
           "matched_matches": len({r.get("physical_match_id") for r in post}),
           "matched_contracts": len({r.get("kalshi_ticker") for r in post}),
           "rows_with_reference": sum(1 for r in post if r.get("external_fair") is not None),
           "three_venue_observations": sum(1 for r in post if {"bovada", "smarkets"} <= srcs(r)),
           "three_venue_contracts": len({r.get("kalshi_ticker") for r in post if {"bovada", "smarkets"} <= srcs(r)}),
           "rows_by_source_set": dict(Counter("+".join(sorted(srcs(r))) or "none" for r in post)),
           "triangulation_rows": dict(tri_rows),
           "triangulation_contracts": {k: len(v) for k, v in tri_contracts.items()},
           "scanner_decisions": dict(Counter(r.get("decision") for r in post))}
    if w4_rows is not None:
        firsts = [r for r in w4_rows if r.extra.get("first_qualifying")]
        elig = [r for r in w4_rows if r.inclusion_result == "INCLUDED"]
        out["w4_first_qualifying_observations"] = len(firsts)
        out["w4_first_qualifying_by_timing"] = dict(Counter(r.timing_class for r in firsts))
        out["w4_eligible_strict_pregame"] = len(elig)
        out["w4_strict_clv_attached"] = sum(1 for r in elig if r.strict_clv_executable is not None)
        out["w4_settled_attached"] = sum(1 for r in elig if r.settlement_value is not None)
        pnl = [r.after_fee_pnl for r in elig if r.after_fee_pnl is not None]
        out["w4_after_fee_pnl"] = stats.mean_ci(pnl)
        out["w4_after_fee_pnl_sum"] = sum(pnl) if pnl else None
    return out


def settlement_audit(data_root: str, settlements: dict, ledger: list[dict]) -> dict:
    """Is settlement ingestion working, and does the health layer see it?"""
    files = sorted(glob.glob(os.path.join(data_root, "research", "settlements", "*.jsonl")))
    seen, dup, rows = set(), 0, []
    for _f, _h, r in src.iter_jsonl(os.path.join(data_root, "research", "settlements", "*.jsonl")):
        pid = r.get("prediction_id")
        if pid in seen:
            dup += 1
            continue
        seen.add(pid)
        rows.append(r)
    by_pid = {r["prediction_id"]: r for r in rows}
    ledger_ids = {r["prediction_id"] for r in ledger}
    orphans = [r for r in rows if r["prediction_id"] not in ledger_ids]
    missing = [r for r in ledger if r["prediction_id"] not in by_pid]
    miss_has_record = [r for r in missing if r["ticker"] in settlements]
    conflicts = 0
    for r in rows:
        cap = settlements.get(r.get("ticker"))
        ex = r.get("exchange") or {}
        if cap and ex.get("result") and cap.get("result") != ex.get("result"):
            conflicts += 1
    sports_src = Counter(((r.get("sports") or {}).get("source") or "none") for r in rows)
    embedded_strict = sum(1 for r in rows if (r.get("clv") or {}).get("strict"))
    return {"ledger_rows": len(ledger), "settlement_files": len(files), "settlement_rows_unique": len(rows),
            "settlement_rows_duplicate_prediction_ids": dup,
            "ledger_rows_settled": len(ledger) - len(missing),
            "settlement_rows_not_in_ledger": len(orphans),
            "settlement_rows_not_in_ledger_sample": [(r.get("ticker"), r.get("generated_at_utc")) for r in orphans[:5]],
            "ledger_rows_without_settlement_row": len(missing),
            "of_which_exchange_has_settled": len(miss_has_record),
            "of_which_not_yet_settled_or_not_swept": len(missing) - len(miss_has_record),
            "settlement_vs_capture_result_conflicts": conflicts,
            "results": dict(Counter(((r.get("exchange") or {}).get("result") or "none") for r in rows)),
            "gradeable_binary": sum(1 for r in rows if r.get("gradeable")),
            "sports_truth_sources": dict(sports_src),
            "strict_clv_embedded_in_settlement_rows": embedded_strict,
            "note": "the settle job embeds the CLV record as computed AT SETTLEMENT TIME; first-ball truth that "
                    "arrives later updates data/research/clv/<run>.jsonl but not the embedded copy"}
