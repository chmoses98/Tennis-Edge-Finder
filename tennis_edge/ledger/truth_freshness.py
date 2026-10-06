"""Independent-truth bookkeeping around the sports-truth snapshots (2026-10-07): which snapshot is current, how fresh the
independent sources are, how long a result takes to become independent truth, and how far the prospective V2-vs-incumbent
study has come. Reads and appends only; no snapshot, settlement or ledger row is ever rewritten.

Why the ordering matters. A sports-truth snapshot is written by every RUN TENNIS and by the bounded truth refresh that
follows an ESPN publish. Ordering them by run time alone let a RUN TENNIS that had pulled its sources BEFORE the ESPN
publish -- but finished after the refresh -- become "current" with older evidence. Snapshots are therefore ordered by
(source stamp, run id): the newest ESPN snapshot + canonical build wins, and run time only breaks ties.
"""
from __future__ import annotations

import glob
import gzip
import json
import os
from collections import Counter
from datetime import date, datetime

from tennis_edge.ledger.sports_truth import LEVEL_FAMILY, LEVEL_GROUP, ticker_date

#: a tour-level result ESPN normally publishes within a day (841 of 842 new rows over 23 daily snapshots appeared 0-1 day
#: after the match, 2026-09-13..10-06). Unresolved beyond this while ESPN is live is an operational warning.
TOUR_PUBLICATION_WINDOW_DAYS = 3
FIRST_V2_RUN = "2026-10-05T15:45:00+00:00"          # first production run carrying projection_v2.0 (PREREGISTRATION §6)
ESPN_FAMILIES = {("ATP", "TOUR"), ("WTA", "TOUR"), ("WTA", "CHALLENGER")}


def source_stamp(manifest: dict) -> str:
    """Comparable stamp of the evidence a canonical build used: the newest source run id it read (ESPN is the only daily
    source, so in practice the ESPN snapshot id), then the build time."""
    runs = sorted(str(v.get("run")) for v in (manifest.get("sources") or {}).values() if isinstance(v, dict) and v.get("run"))
    return f"{runs[-1] if runs else ''}|{manifest.get('built_at') or ''}"


def snapshot_order(meta: dict) -> tuple:
    return (meta.get("source_stamp") or "", meta.get("run_id") or "")


def current_snapshot(truth_dir: str) -> str | None:
    """Path of the current sports-truth snapshot: newest source evidence first, run id second. Snapshots written before
    2026-10-07 have no sidecar and rank below any that do (their source is no newer)."""
    snaps = sorted(glob.glob(os.path.join(truth_dir, "*.jsonl.gz")))
    if not snaps:
        return None
    best, key = None, None
    for p in snaps:
        meta_p = p.replace(".jsonl.gz", ".meta.json")
        meta = json.load(open(meta_p)) if os.path.exists(meta_p) else {}
        k = (meta.get("source_stamp") or "", os.path.basename(p).split(".")[0])
        if key is None or k > key:
            best, key = p, k
    return best


def read_snapshot(path: str) -> list[dict]:
    with gzip.open(path, "rt") as fh:
        return [json.loads(line) for line in fh if line.strip()]


def family_of(level: str | None) -> str:
    return LEVEL_FAMILY.get(LEVEL_GROUP.get(str(level), "O"), "TOUR")


LEVEL_BUCKETS = {("ATP", "TOUR"): "ATP tour", ("ATP", "CHALLENGER"): "ATP Challenger", ("ATP", "ITF"): "ATP ITF",
                 ("WTA", "TOUR"): "WTA tour", ("WTA", "CHALLENGER"): "WTA 125", ("WTA", "ITF"): "WTA ITF"}


def prospective_summary(truth_rows: list[dict], ledger: dict, as_of: date, first_v2: str = FIRST_V2_RUN) -> dict:
    """The V2-vs-incumbent prospective study's settlement state. COUNTS ONLY: no probability is scored here, so nothing
    in this summary can feed back into the frozen model (PREREGISTRATION §6; readout at 1,500 independently settled).

    `ledger` = {prediction_id: ledger row} for the settled predictions in `truth_rows`."""
    study = {}
    for r in truth_rows:
        L = ledger.get(r["prediction_id"])
        if not L or L.get("family") != "MATCH_WINNER" or "|" in str(L.get("player_a_id") or ""):
            continue
        mo = L.get("models") or {}
        if mo.get("V2") is None or mo.get("INCUMBENT") is None or str(L.get("generated_at_utc")) < first_v2:
            continue
        study[r["prediction_id"]] = (r, L)
    status, rec, by_bucket = Counter(), Counter(), {}
    matches_all, matches_resolved, stale = set(), set(), []
    for pid, (r, L) in study.items():
        st = (r.get("independent") or {}).get("status")
        status[st] += 1
        rs = (r.get("reconciliation") or {}).get("status")
        rec[rs or "NONE"] += 1
        if (r.get("reconciliation") or {}).get("explained") and rs != "CONFLICT":
            rec["EXPLAINED_NOTE"] += 1
        b = LEVEL_BUCKETS.get((r.get("tour"), family_of(r.get("level"))), f"{r.get('tour')} other")
        by_bucket.setdefault(b, Counter())[st] += 1
        matches_all.add(L.get("match_id"))
        if st == "RESOLVED":
            matches_resolved.add(L.get("match_id"))
        on = ticker_date(L.get("event_ticker") or L.get("match_id"))
        if (st in ("NOT_FOUND", "PENDING_RESULT") and on and (r.get("tour"), family_of(r.get("level"))) in ESPN_FAMILIES
                and (as_of - on).days > TOUR_PUBLICATION_WINDOW_DAYS):
            stale.append({"prediction_id": pid, "match_id": L.get("match_id"), "match_day": str(on), "status": st})
    return {"first_v2_run": first_v2, "predictions_with_v2_and_incumbent": len(study),
            "matches_with_v2_and_incumbent": len(matches_all),
            "exchange_settled_predictions": len(study),
            "independently_resolved_predictions": status.get("RESOLVED", 0),
            "independently_settled_matches": len(matches_resolved),
            "by_status": dict(status), "reconciliation": dict(rec),
            "by_level": {k: dict(v) for k, v in sorted(by_bucket.items())},
            "stale_unresolved_tour_level": stale[:50], "n_stale_unresolved_tour_level": len(stale),
            "readout_at_independently_settled_matches": 1500}


def freshness(index, manifest: dict, as_of: date) -> dict:
    """Newest independent result date by tour/level family, the source snapshots behind them, and whether each is live."""
    out = {"as_of": str(as_of), "sources": {k: v.get("run") for k, v in (manifest.get("sources") or {}).items()
                                             if isinstance(v, dict) and v.get("run")},
           "canonical_matches_sha256": manifest.get("matches_sha256"), "build_version": manifest.get("build_version"),
           "horizons": {}}
    for (tour, fam), label in LEVEL_BUCKETS.items():
        full = index.family_horizon.get((tour, fam))
        part = getattr(index, "partial_horizon", {}).get((tour, fam))
        hz = max((x for x in (full, part) if x), default=None)
        out["horizons"][label] = {"newest_result": str(hz) if hz else None,
                                  "lag_days": None if not hz else (as_of - hz).days,
                                  "live": bool(hz and (as_of - hz).days <= 3),
                                  "coverage": "partial" if part and (not full or part > full) else ("full" if hz else "none")}
    out["espn_families_not_live"] = [LEVEL_BUCKETS[k] for k in sorted(ESPN_FAMILIES) if not out["horizons"][LEVEL_BUCKETS[k]]["live"]]
    return out


def update_resolution_log(log_dir: str, truth_rows: list[dict], ledger: dict, run_id: str, provenance: dict) -> dict:
    """Append-only first-resolution log, one file per run (`<log_dir>/<run_id>.jsonl`): a line the first time a
    prediction becomes independently RESOLVED, with the run and source that resolved it. Per-run files because two
    jobs write sports truth (RUN TENNIS and the truth refresh); a shared rolling file would let one overwrite the other.
    The lag from match day to that line is the independent-truth latency (the very first run is a backfill)."""
    seen = set()
    files = sorted(glob.glob(os.path.join(log_dir, "*.jsonl")))
    backfill = not files
    for fp in files:
        for line in open(fp):
            try:
                seen.add(json.loads(line)["prediction_id"])
            except (ValueError, KeyError):
                continue
    new, lags = [], []
    resolved_at = datetime.strptime(run_id, "%Y%m%dT%H%M%SZ")
    for r in truth_rows:
        if (r.get("independent") or {}).get("status") != "RESOLVED" or r["prediction_id"] in seen:
            continue
        L = ledger.get(r["prediction_id"]) or {}
        on = ticker_date(L.get("event_ticker") or L.get("match_id"))
        lag = None if not on else round((resolved_at - datetime(on.year, on.month, on.day)).total_seconds() / 86400, 2)
        new.append({"prediction_id": r["prediction_id"], "match_id": L.get("match_id"), "match_day": str(on) if on else None,
                    "first_resolved_run": run_id, "lag_days": lag, "backfill": backfill,
                    "source_label": (r.get("independent") or {}).get("source_label"), "provenance": provenance})
        if lag is not None and not backfill:
            lags.append(lag)
    if new:
        os.makedirs(log_dir, exist_ok=True)
        with open(os.path.join(log_dir, f"{run_id}.jsonl"), "w") as f:
            for x in new:
                f.write(json.dumps(x, default=str) + "\n")
    lags.sort()
    return {"newly_resolved": len(new), "first_resolutions_total": len(seen) + len(new), "backfill": backfill,
            "lag_days_median_new": lags[len(lags) // 2] if lags else None,
            "lag_days_max_new": lags[-1] if lags else None}
