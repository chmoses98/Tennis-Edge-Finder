"""Production health gates TENNIS-1 .. TENNIS-18. Each gate returns GateResult(status PASS|FAIL|UNKNOWN, detail).

UNKNOWN is a failure for production purposes (fail closed): a gate that cannot be evaluated because the
evidence is missing does not turn green. Gates read the artifacts the pipeline produces; none of them may
be weakened to pass -- change the pipeline, not the gate.
"""
from __future__ import annotations

import glob
import gzip
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


@dataclass
class GateResult:
    gate: str
    name: str
    status: str
    detail: dict

    def to_dict(self):
        return asdict(self)


def _latest_discovery(root=None):
    root = root or os.path.join(PROJ, "data", "kalshi", "discovery")
    runs = sorted(glob.glob(os.path.join(root, "*", "summary.json")))
    return os.path.dirname(runs[-1]) if runs else None



# ---------------------------------------------------------------------------------------------------
def first_ball_metrics(store_root=None, coverage_path=None, discovery_dir=None, now=None) -> dict:
    """Submetrics for gates TENNIS-8 and TENNIS-10, all derived from evidence on disk.

    Deliberately reports the levels WITHOUT a wired first-ball source separately rather than folding
    them into a ratio. ESPN reaches ATP and WTA main tour and the Grand Slams; Challenger, ITF and
    qualifying have no reachable source at all (see docs/FIRST_BALL_SOURCES.md). Averaging those levels
    into a coverage percentage would let a structural gap hide inside a number that drifts up when the
    tour calendar happens to be quiet.
    """
    from tennis_edge.firstball.store import FirstBallStore
    from tennis_edge.firstball.watchlist import SOURCE_COVERED_LEVELS
    now = now or datetime.now(timezone.utc)
    root = store_root or os.path.join(PROJ, "data", "firstball", "store")
    out = {"store": root, "truths": 0, "strict_truths": 0, "no_play": 0, "contradictions": 0,
           "contradiction_rate": None, "bracket_seconds_median": None, "bracket_seconds_p90": None,
           "by_confidence": {}, "chain_violations": [], "observations": 0, "matches_observed": 0}
    if not os.path.isdir(root):
        out["reason"] = "no first-ball store yet"
        return out
    store = FirstBallStore(root)
    truths = store.latest_truths()
    obs = store.observations()
    out["observations"] = len(obs)
    out["matches_observed"] = len({o.match_id for o in obs})
    out["truths"] = len(truths)
    out["strict_truths"] = sum(1 for t in truths.values() if t.strict_eligible)
    out["no_play"] = sum(1 for t in truths.values() if t.no_play)
    out["contradictions"] = sum(1 for t in truths.values() if t.contradiction_status == "MATERIAL")
    out["contradiction_rate"] = round(out["contradictions"] / len(truths), 4) if truths else None
    for t in truths.values():
        out["by_confidence"][t.confidence] = out["by_confidence"].get(t.confidence, 0) + 1
    widths = sorted(t.bracket_seconds for t in truths.values()
                    if t.strict_eligible and t.bracket_seconds is not None)
    if widths:
        out["bracket_seconds_median"] = widths[len(widths) // 2]
        out["bracket_seconds_p90"] = widths[min(len(widths) - 1, int(0.9 * len(widths)))]
    out["chain_violations"] = store.verify_chain()[:10]

    # how much of what we are currently watching is bound to a first-ball source at all
    d = discovery_dir or _latest_discovery()
    if d:
        try:
            from tennis_edge.firstball.watchlist import build_watchlist
            items, _ = build_watchlist(d, now=now)
            covered = [i for i in items if i.level in SOURCE_COVERED_LEVELS]
            seen = {o.match_id for o in obs}
            out["watchlist"] = {
                "total": len(items),
                "levels_with_a_wired_source": len(covered),
                "levels_without_any_source": len(items) - len(covered),
                "watched_and_observed": sum(1 for i in items if i.match_id in seen),
                "covered_and_observed": sum(1 for i in covered if i.match_id in seen),
                "pct_covered_with_source_mapping": round(
                    sum(1 for i in covered if i.match_id in seen) / len(covered), 4) if covered else None,
            }
        except Exception as e:                       # a metric must never take the gates down
            out["watchlist"] = {"error": f"{type(e).__name__}: {e}"[:200]}

    cov = coverage_path or os.path.join(PROJ, "data", "research", "segments", "coverage.json")
    if os.path.exists(cov):
        c = json.load(open(cov))
        tc = c.get("timing_classes", {})
        total = sum(tc.values()) or 0
        out["observations_classified"] = total
        out["timing_classes"] = tc
        out["pct_classifiable"] = round((total - tc.get("START_UNKNOWN", 0)) / total, 4) if total else None
        out["pct_strict_pregame"] = round(tc.get("STRICT_PREGAME", 0) / total, 4) if total else None
        out["executable_close_rows"] = c.get("executable_close_rows")
        out["strict_clv_rows"] = c.get("strict_clv_rows")
        out["horizons_populated"] = c.get("horizons_populated")
        out["horizons_total"] = c.get("horizons_total")
    return out


def gate_1_discovery(now=None) -> GateResult:
    """TENNIS-1: complete Kalshi tennis discovery -- latest snapshot complete, catalogue paginated fully, < 36h old."""
    d = _latest_discovery()
    if not d:
        return GateResult("TENNIS-1", "kalshi_tennis_discovery", "UNKNOWN", {"reason": "no discovery snapshot"})
    s = json.load(open(os.path.join(d, "summary.json")))
    started = datetime.fromisoformat(s["started_at"])
    age_h = ((now or datetime.now(timezone.utc)) - started).total_seconds() / 3600
    ok = s.get("complete") and s.get("series_complete") and not s.get("failures") and age_h < 36
    return GateResult("TENNIS-1", "kalshi_tennis_discovery", "PASS" if ok else "FAIL",
                      {"run": s["run_id"], "age_hours": round(age_h, 1), "complete": s.get("complete"), "failures": len(s.get("failures", [])), "series_tennis": s.get("series_tennis")})


def gate_2_taxonomy() -> GateResult:
    """TENNIS-2: every discovered tennis series maps to a known family and >= 99.5% of live markets parse or are explicitly unsupported."""
    from tennis_edge.kalshi.families import unknown_series
    from tennis_edge.kalshi.markets import parse_market
    d = _latest_discovery()
    if not d:
        return GateResult("TENNIS-2", "taxonomy_normalization", "UNKNOWN", {"reason": "no discovery snapshot"})
    series = json.load(open(os.path.join(d, "series_tennis.json")))
    unk = unknown_series([s["ticker"] for s in series])
    n = bad = 0
    for p in glob.glob(os.path.join(d, "markets", "*.json")):
        for st, blk in json.load(open(p)).items():
            for m in blk.get("markets") or []:
                n += 1
                if parse_market(m).status == "UNPARSED":
                    bad += 1
    rate = 1 - bad / n if n else 0
    ok = not unk and n > 0 and rate >= 0.995
    return GateResult("TENNIS-2", "taxonomy_normalization", "PASS" if ok else "FAIL", {"unknown_series": unk, "live_markets": n, "unparsed": bad, "parse_rate": round(rate, 5)})


def _run_snapshot_markets(proj_path, known: set, snapshots_root=None) -> list:
    """Open-market records from the full snapshot the latest projection run treated as authoritative, minus
    `known` tickers. Empty when the run had no authoritative snapshot (then discovery alone is the universe)."""
    if not os.path.exists(proj_path):
        return []
    lc = (json.load(open(proj_path)).get("lifecycle") or {})
    if not (lc.get("snapshot_authoritative") and lc.get("open_snapshot_run")):
        return []
    root = snapshots_root or os.path.join(PROJ, "data", "kalshi", "run_snapshots")
    hits = glob.glob(os.path.join(root, "*", f"{lc['open_snapshot_run']}.open_snapshot.jsonl.gz"))
    if not hits:
        return []
    out, seen = [], set(known)
    with gzip.open(hits[0], "rt") as fh:
        for line in fh:
            r = json.loads(line)
            if r.get("ticker") and r["ticker"] not in seen:
                out.append(r); seen.add(r["ticker"])
    return out


def gate_3_4_active_coverage(projections_path=None) -> tuple[GateResult, GateResult]:
    """TENNIS-3: every ACTIVE market is mapped (parsed or explicitly unsupported);
    TENNIS-4: every active PROJECTABLE market has a projection in the latest projection run."""
    from tennis_edge.kalshi.markets import parse_market
    d = _latest_discovery()
    if not d:
        u = GateResult("TENNIS-3", "active_market_mapping", "UNKNOWN", {"reason": "no discovery"})
        return u, GateResult("TENNIS-4", "active_market_projection", "UNKNOWN", {"reason": "no discovery"})
    active = []
    for p in glob.glob(os.path.join(d, "markets", "*.json")):
        for m in json.load(open(p)).get("open", {}).get("markets") or []:
            active.append(parse_market(m))
    proj_path = projections_path or os.path.join(PROJ, "data", "research", "projections", "latest.json")
    # markets listed after the daily discovery: the open snapshot the projection run priced from (2026-10-05;
    # 779 of 934 open markets on that day were absent from discovery and so invisible to this gate)
    late = _run_snapshot_markets(proj_path, {x.ticker for x in active})
    active += [parse_market(m) for m in late]
    unparsed = [x.ticker for x in active if x.status == "UNPARSED"]
    g3 = GateResult("TENNIS-3", "active_market_mapping", "PASS" if not unparsed and active else ("UNKNOWN" if not active else "FAIL"),
                    {"active": len(active), "listed_after_discovery": len(late), "unparsed": unparsed[:20],
                     "unsupported": sum(x.status == "UNSUPPORTED_FAMILY" for x in active)})
    if not os.path.exists(proj_path):
        return g3, GateResult("TENNIS-4", "active_market_projection", "UNKNOWN", {"reason": "no projection run", "projectable_active": sum(x.projectable and x.status == "PARSED" for x in active)})
    pj = json.load(open(proj_path))
    have = set(pj.get("projected_tickers", []))
    # the projection run already applied lifecycle (closed since discovery) and pregame exclusions, which are not
    # coverage failures; what counts is every still-open, pregame, projectable market that was NOT priced
    hard = [e for e in pj.get("excluded", []) if e.get("stage") in ("event", "identity", "format", "pricing", "doubles")]
    # identity gaps a rule or a person can close vs players absent from every reachable results source (2026-10-05)
    id_kinds: dict = {}
    for e in hard:
        if e.get("stage") == "identity":
            for k in (e.get("identity_kinds") or ["UNCLASSIFIED"]):
                id_kinds[k] = id_kinds.get(k, 0) + 1
    need = len(have) + len(hard)
    g4 = GateResult("TENNIS-4", "active_market_projection", "PASS" if not hard else "FAIL",
                    {"projectable_open_pregame": need, "projected": len(have), "not_projected": len(hard),
                     "not_projected_by_stage": {st_: sum(1 for e in hard if e.get("stage") == st_) for st_ in sorted({e.get("stage") for e in hard})},
                     "identity_gap_kinds": id_kinds, "alias_review_queue": len(pj.get("alias_review_queue") or []),
                     "missing_sample": [e["ticker"] + ": " + e["reason"][:60] for e in hard[:10]],
                     "excluded_by_policy": {k: v for k, v in pj.get("coverage", {}).items() if k in ("closed_since_discovery", "past_nominal_start", "unsupported_family", "tournament_scope_not_priced_tonight", "first_ball_already_observed")},
                     "projection_run": pj.get("run_id")})
    return g3, g4


#: TENNIS-5 thresholds. The 30-minute limit is the one this gate has always used (and the quote STALE bound in
#: scripts/run_tennis.py); it was not changed when the gate was split in two (2026-10-06).
GATE5_MAX_AGE_MIN = 30
GATE5_FRESH_QUOTE_MIN = 10          # reported only: run_tennis.py's FRESH band
GATE5_CADENCE_WINDOW_H = 6          # one RUN TENNIS interval (cron every 6 h)


def _pct(xs, q):
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(q * (len(xs) - 1))))] if xs else None


def _iso(x):
    try:
        return datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def pricing_quote_freshness(projections_dir=None, max_age_min=GATE5_MAX_AGE_MIN) -> dict:
    """Age, AT PRICING TIME, of the quote each row of the latest projection run was priced against.

    Read from the run's own rows (market_quote.quote_ts / priced_at, written by run_tennis.quote_provenance). This
    is the freshness that decides whether a model-vs-market comparison used current information. Every row counts;
    a row whose quote age cannot be established counts as over the threshold (fail closed)."""
    root = projections_dir or os.path.join(PROJ, "data", "research", "projections")
    latest = os.path.join(root, "latest.json")
    if not os.path.exists(latest):
        return {"status": "UNKNOWN", "reason": "no projection run"}
    lj = json.load(open(latest))
    run_path = os.path.join(root, f"{lj.get('run_id')}.json")
    if not os.path.exists(run_path):
        return {"status": "UNKNOWN", "reason": f"projection run file {lj.get('run_id')}.json missing"}
    pj = json.load(open(run_path))
    rows = pj.get("projections") or []
    lc = pj.get("lifecycle") or {}
    out = {"threshold_min": max_age_min, "pricing_run": pj.get("run_id"), "pricing_generated_at": pj.get("generated_at"),
           "open_snapshot_run": lc.get("open_snapshot_run"), "snapshot_authoritative": lc.get("snapshot_authoritative"),
           "open_snapshot_age_at_pricing_s": None if lc.get("open_snapshot_age_s") is None else round(float(lc["open_snapshot_age_s"]), 1),
           "n_priced": len(rows)}
    if not rows:
        out.update(status="UNKNOWN", reason="the latest projection run priced nothing")
        return out
    ages, unknown, by_src, quote_ts, priced_ts = [], 0, {}, [], []
    for r in rows:
        mq = r.get("market_quote") or {}
        by_src[mq.get("source") or "?"] = by_src.get(mq.get("source") or "?", 0) + 1
        q, pr = _iso(mq.get("quote_ts")), _iso(mq.get("priced_at") or r.get("generated_at_utc"))
        age = mq.get("quote_age_s")
        if age is None and q is not None and pr is not None:
            age = (pr - q).total_seconds()
        if age is None or q is None:
            unknown += 1
            continue
        if pr is None:
            pr = q + timedelta(seconds=float(age))
        ages.append(float(age)); quote_ts.append(q); priced_ts.append(pr)
    lim = max_age_min * 60
    over = sum(a > lim for a in ages) + unknown
    out.update({
        "quote_sources": by_src, "n_age_unknown": unknown,
        "median_age_s": None if not ages else round(_pct(ages, 0.5), 1),
        "p95_age_s": None if not ages else round(_pct(ages, 0.95), 1),
        "max_age_s": None if not ages else round(max(ages), 1),
        "n_over_threshold": over, "pct_over_threshold": round(over / len(rows), 4),
        "n_over_fresh_band": sum(a > GATE5_FRESH_QUOTE_MIN * 60 for a in ages) + unknown,
        "quote_ts_oldest": min(quote_ts).isoformat() if quote_ts else None,
        "quote_ts_newest": max(quote_ts).isoformat() if quote_ts else None,
        "priced_at_first": min(priced_ts).isoformat() if priced_ts else None,
        "priced_at_last": max(priced_ts).isoformat() if priced_ts else None})
    out["status"] = "PASS" if over == 0 else "FAIL"
    if over:
        out["reason"] = f"{over} of {len(rows)} rows were priced on a quote older than {max_age_min} min (or of unknown age)"
    return out


def background_capture_health(now=None, max_age_min=GATE5_MAX_AGE_MIN, max_trade_backlog_age_h=2.0,
                              window_h=GATE5_CADENCE_WINDOW_H, capture_root=None, pull_record=None) -> dict:
    """Operational health of the capture conductor, from its own pass manifests.

    * freshness: age of the newest capture pass when THIS RUNNER TOOK ITS COPY of the evidence branch (the pull
      record). Without a pull record the age at evaluation time is used instead -- stricter, and labelled so.
    * cadence: every interval between consecutive completed passes in the last `window_h`, including the interval
      from the newest pass to the pull. Any interval over `max_age_min` is a gap and fails.
    * the newest pass must have no incomplete stage, and the trade-tape backlog must be younger than
      `max_trade_backlog_age_h` (both exactly as before the split)."""
    now = now or datetime.now(timezone.utc)
    root = capture_root or os.path.join(PROJ, "data", "kalshi", "capture")
    mans = sorted(glob.glob(os.path.join(root, "*", "*.manifest.json")))
    if not mans:
        return {"status": "UNKNOWN", "reason": "no capture manifests"}
    passes = []
    for mp in mans[-400:]:
        try:
            m = json.load(open(mp))
        except ValueError:
            continue
        fin = _iso(m.get("finished_at"))
        if fin is None:
            continue
        passes.append((fin, _iso(m.get("started_at")), m))
    if not passes:
        return {"status": "UNKNOWN", "reason": "no readable capture manifests"}
    passes.sort(key=lambda x: x[0])
    latest_fin, latest_start, m = passes[-1]
    pr = pull_record
    if pr is None:
        pp = os.path.join(PROJ, "data", ".pull_record.json")
        pr = json.load(open(pp)) if os.path.exists(pp) else None
    pulled_at = _iso((pr or {}).get("pulled_at"))
    ref, ref_kind = (pulled_at, "pull") if pulled_at else (now, "evaluation (no pull record: stricter)")
    age_ref = (ref - latest_fin).total_seconds() / 60
    lo = ref - timedelta(hours=window_h)
    fins = [f for f, _s, _m in passes if lo <= f <= ref]
    prior = [f for f, _s, _m in passes if f < lo]
    if prior:
        fins = [prior[-1]] + fins                  # the interval that crosses into the window counts too
    cad = [(b - a).total_seconds() / 60 for a, b in zip(fins, fins[1:])]
    tail = (ref - fins[-1]).total_seconds() / 60 if fins else age_ref
    intervals = cad + [tail]
    gaps = [round(x, 1) for x in intervals if x > max_age_min]
    durs = [(f - s).total_seconds() for f, s, _m in passes[-50:] if s is not None]
    window_passes = [mm for f, _s, mm in passes if lo <= f <= ref]
    failed = sum(1 for mm in window_passes if mm.get("incomplete"))
    backlog = ((m.get("trades") or {}).get("backlog") or {})
    oldest = backlog.get("oldest_gap_age_s")
    backlog_ok = oldest is None or oldest <= max_trade_backlog_age_h * 3600
    ok = age_ref <= max_age_min and not gaps and not m.get("incomplete") and backlog_ok
    out = {"status": "PASS" if ok else "FAIL", "threshold_min": max_age_min,
           "latest_capture_run": m.get("run_id"), "latest_capture_finished_at": latest_fin.isoformat(),
           "measured_at": ref.isoformat(), "measured_at_kind": ref_kind,
           "capture_age_at_measurement_min": round(age_ref, 1),
           "cadence_window_h": window_h, "passes_in_window": len(window_passes),
           "cadence_median_min": None if not cad else round(_pct(cad, 0.5), 1),
           "cadence_max_min": None if not cad else round(max(cad), 1),
           "gaps_over_threshold_min": gaps,
           "pass_duration_median_s": None if not durs else round(_pct(durs, 0.5), 1),
           "latest_pass_duration_s": None if latest_start is None else round((latest_fin - latest_start).total_seconds(), 1),
           "failed_passes_in_window": failed, "latest_incomplete": (m.get("incomplete") or [])[:5],
           "trade_backlog": backlog or None, "trade_backlog_ok": backlog_ok}
    if not ok:
        why = []
        if age_ref > max_age_min:
            why.append(f"newest capture was {age_ref:.1f} min old at {ref_kind.split(' ')[0]}")
        if gaps:
            why.append(f"capture gaps over {max_age_min} min: {gaps}")
        if m.get("incomplete"):
            why.append("newest pass has an incomplete stage")
        if not backlog_ok:
            why.append("trade-tape backlog too old")
        out["reason"] = "; ".join(why)
    return out


def gate_5_capture_freshness(max_age_min=GATE5_MAX_AGE_MIN, now=None, max_trade_backlog_age_h=2.0,
                             projections_dir=None, pull_record=None) -> GateResult:
    """TENNIS-5: market data freshness, as TWO separately reported checks that must both PASS.

    1. pricing_quote_freshness -- the age, at pricing time, of the quote every row of the latest projection run was
       priced against. This is the "was the comparison made on current information" question.
    2. background_capture_health -- the capture conductor's operational freshness and cadence (newest pass at the
       moment this runner pulled the evidence, every gap in the last cadence window, incomplete passes, trade
       backlog).

    `pulled_capture_artifact_age_min` is reported beside them and is NOT a status: it is the age NOW of the newest
    capture in this runner's pulled copy, which grows while the run works (20-34 min by the time health runs). Until
    2026-10-06 the gate failed on that number alone, which said "the quote was stale" when the quote was seconds old.
    Neither threshold was changed by the split."""
    now = now or datetime.now(timezone.utc)
    cap = background_capture_health(now=now, max_age_min=max_age_min, max_trade_backlog_age_h=max_trade_backlog_age_h,
                                    pull_record=pull_record)
    if cap.get("status") == "UNKNOWN" and cap.get("reason") == "no capture manifests":
        return GateResult("TENNIS-5", "market_capture_freshness", "UNKNOWN", {"reason": "no capture manifests",
                                                                              "background_capture_health": cap})
    pq = pricing_quote_freshness(projections_dir, max_age_min=max_age_min)
    statuses = (pq.get("status"), cap.get("status"))
    status = "PASS" if statuses == ("PASS", "PASS") else ("FAIL" if "FAIL" in statuses else "UNKNOWN")
    latest_fin = _iso(cap.get("latest_capture_finished_at"))
    pulled_age = round((now - latest_fin).total_seconds() / 60, 1) if latest_fin else None
    return GateResult("TENNIS-5", "market_capture_freshness", status, {
        "pricing_quote_freshness": pq.get("status"), "background_capture_health": cap.get("status"),
        "pulled_capture_artifact_age_min": pulled_age,
        "pulled_capture_artifact_age_note": ("age at health-evaluation time of the newest capture pass in this runner's "
                                             "pulled copy; it grows while the run works and is NOT the age of any quote "
                                             "used for pricing (see pricing_quote) nor the conductor's freshness (see capture)"),
        "pricing_quote": pq, "capture": cap,
        # kept for readers of the old detail (same meanings as before the split)
        "run": cap.get("latest_capture_run"), "incomplete": cap.get("latest_incomplete"),
        "trade_backlog": cap.get("trade_backlog"), "trade_backlog_ok": cap.get("trade_backlog_ok")})


def gate_6_no_post_start_leakage(ledger_rows, starts: dict, strict_research_rows=None, quarantine: dict | None = None,
                                 quarantine_problems: list | None = None, settled_at: dict | None = None) -> GateResult:
    """TENNIS-6: every pregame prediction was generated strictly before the match's actual first ball
    (or, when unknown, before scheduled_start - 5 min, flagged).

    `starts` maps match_id -> (earliest possible first ball, scheduled_start[, latest possible first ball]).
    Any violation FAILS the gate, exactly as before. What changed on 2026-09-27 is that the detail no
    longer lets two different things read as one:

      post_start_confirmed      generated at/after the LATEST possible first ball (A/B truth): the row
                                really was priced in play. A pipeline defect.
      inside_first_ball_bracket generated between the earliest and latest possible first ball.
      schedule_fallback         no A/B truth; generated inside 5 minutes of the nominal start.
      no_start_information      no truth and no schedule at all (fail closed).
      start_unknown_passed      no A/B truth, generated safely before the nominal start. NOT a violation:
                                this is the conservative START_UNKNOWN accounting, reported as a count.

    A TRUE LEAK is a post-start row being USED as pregame evidence. `strict_research_rows` (CLV rows from
    the settle job) lets the gate check that directly: every row flagged strict must carry the
    STRICT_PREGAME timing class. That count is reported as `post_start_rows_in_strict_research`."""
    viol = []; unknown = 0
    cats = {"post_start_confirmed": 0, "inside_first_ball_bracket": 0, "schedule_fallback": 0,
            "no_start_information": 0}
    for r in ledger_rows:
        gen = datetime.fromisoformat(r["generated_at_utc"])
        st = starts.get(r["match_id"], (None, None))
        afb, sched = st[0], st[1]
        upper = st[2] if len(st) > 2 else None
        if afb is not None:
            if gen >= afb:
                viol.append(r["prediction_id"])
                cats["post_start_confirmed" if (upper is None or gen >= upper) else "inside_first_ball_bracket"] += 1
        elif sched is not None:
            unknown += 1
            if gen >= sched - timedelta(minutes=5):
                viol.append(r["prediction_id"])
                cats["schedule_fallback"] += 1
        else:
            viol.append(r["prediction_id"])
            cats["no_start_information"] += 1
    # 2026-10-05: a row generated AFTER THE EXCHANGE SETTLED its market was certainly priced post-start, whether
    # or not any first-ball source covers the level (ITF has none). Exchange settlement time is an upper bound on
    # the first ball. These were invisible here: 2,695 such rows, still being produced daily.
    if settled_at:
        cats["post_settlement"] = 0
        vset = set(viol)
        for r in ledger_rows:
            ts = settled_at.get(r["prediction_id"])
            if ts and r["prediction_id"] not in vset and datetime.fromisoformat(r["generated_at_utc"]) > ts:
                viol.append(r["prediction_id"])
                cats["post_settlement"] += 1
    detail = {"violations": viol[:20], "n_violations": len(viol), "violation_classes": cats,
              "n": len(ledger_rows), "start_unknown_used_schedule": unknown,
              "start_unknown_passed_schedule_check": unknown - cats["schedule_fallback"]}
    if strict_research_rows is not None:
        detail["post_start_rows_in_strict_research"] = sum(
            1 for c in strict_research_rows if c.get("strict") and c.get("timing_class") != "STRICT_PREGAME")
        detail["strict_research_rows_checked"] = sum(1 for c in strict_research_rows if c.get("strict"))
    leaked = detail.get("post_start_rows_in_strict_research", 0)
    # 2026-10-05: LEGACY vs ACTIVE. A violation counts as legacy only if it is listed, by prediction_id, in the
    # append-only quarantine register (tennis_edge/ledger/quarantine.py), which refuses any row generated after
    # the in-play guard was deployed. Unregistered or post-guard violations are ACTIVE and fail the gate exactly
    # as every violation did before; so does a damaged register. Nothing is deleted from the ledger.
    if quarantine is not None:
        from tennis_edge.ledger.quarantine import GUARD_DEPLOYED_AT
        by_id = {r["prediction_id"]: r for r in ledger_rows}
        from tennis_edge.ledger.quarantine import is_legacy
        legacy = [v for v in viol if v in quarantine and is_legacy({**quarantine[v], "git_sha": by_id[v].get("git_sha"),
                                                                    "generated_at_utc": by_id[v]["generated_at_utc"]})]
        active = [v for v in viol if v not in set(legacy)]
        since = [r for r in ledger_rows if datetime.fromisoformat(r["generated_at_utc"]) >= GUARD_DEPLOYED_AT]
        verifiable = sum(1 for r in since if starts.get(r["match_id"], (None,))[0] is not None)
        detail.update({"legacy_quarantined": len(legacy), "active_violations": len(active),
                       "active_violation_ids": active[:20], "quarantine_register_rows": len(quarantine),
                       "quarantine_register_problems": quarantine_problems or [],
                       "guard_deployed_at": GUARD_DEPLOYED_AT.isoformat(),
                       "rows_since_guard": len(since), "rows_since_guard_with_first_ball_truth": verifiable,
                       "note": ("rows since the guard WITHOUT A/B first-ball truth cannot be verified either way; they are "
                                "START_UNKNOWN and excluded from strict research by construction (see TENNIS-10)")})
        ok = not active and not leaked and not quarantine_problems
        return GateResult("TENNIS-6", "no_post_start_leakage", "PASS" if ok else "FAIL", detail)
    return GateResult("TENNIS-6", "no_post_start_leakage", "PASS" if not viol and not leaked else "FAIL", detail)


def gate_7_identity(links_summary: dict | None) -> GateResult:
    """TENNIS-7: no AMBIGUOUS mapping is used in production; ambiguity rate reported."""
    if not links_summary:
        return GateResult("TENNIS-7", "player_identity_integrity", "UNKNOWN", {"reason": "no link summary"})
    amb = links_summary.get("AMBIGUOUS", 0); used_amb = links_summary.get("ambiguous_used_in_production", 0)
    return GateResult("TENNIS-7", "player_identity_integrity", "PASS" if used_amb == 0 else "FAIL", {"ambiguous": amb, "ambiguous_used": used_amb, **{k: v for k, v in links_summary.items() if k in ("MATCHED", "UNMATCHED")}})


def gate_8_9_truth(sports_ok: int | None, sports_total: int | None, exchange_conflicts: int | None,
                   rules_id_changes: list | None, first_ball: dict | None = None,
                   settlement: dict | None = None) -> tuple[GateResult, GateResult]:
    """TENNIS-8: sports truth health, which since the first-ball wave explicitly INCLUDES first-ball
    coverage: sports truth for >= 98% of settled predictions, an intact first-ball hash chain, and every
    match we are watching at a level with a wired source actually bound to that source. TENNIS-9: no
    unexplained exchange/sports conflicts and no unreviewed settlement-rule text changes.

    `sports_ok` counts settled predictions whose sports truth comes from a source INDEPENDENT of the
    exchange. A "sports truth" copied from Kalshi's own result cannot be reconciled against Kalshi's
    result, so it is reported (`settlement.sports_truth_kalshi_derived`) but never counted as ok."""
    fb = first_ball if first_ball is not None else first_ball_metrics()
    wl = fb.get("watchlist") or {}
    pct_mapped = wl.get("pct_covered_with_source_mapping")
    fb_ok = (not fb.get("chain_violations")) and (pct_mapped is None or pct_mapped >= 0.9)
    detail_fb = {"first_ball": {k: fb.get(k) for k in
                                ("truths", "strict_truths", "no_play", "contradictions", "contradiction_rate",
                                 "by_confidence", "bracket_seconds_median", "bracket_seconds_p90",
                                 "chain_violations", "observations", "matches_observed", "watchlist",
                                 "pct_classifiable", "pct_strict_pregame", "timing_classes")}}
    if settlement:
        detail_fb["settlement"] = settlement
    if sports_total is None:
        status = "UNKNOWN"
        g8 = GateResult("TENNIS-8", "sports_truth_health", status,
                        {"reason": "no settled predictions yet", **detail_fb})
    else:
        rate = sports_ok / sports_total if sports_total else 0
        ok = bool(sports_total) and rate >= 0.98 and fb_ok
        g8 = GateResult("TENNIS-8", "sports_truth_health", "PASS" if ok else "FAIL",
                        {"ok": sports_ok, "total": sports_total, "rate": round(rate, 4),
                         "first_ball_ok": fb_ok, **detail_fb})
    if exchange_conflicts is None:
        reason = ("no settled predictions yet" if sports_total is None else
                  "no sports truth independent of the exchange to reconcile the exchange result against")
        g9 = GateResult("TENNIS-9", "exchange_settlement_health", "UNKNOWN", {"reason": reason, "rules_id_changes": rules_id_changes or []})
    else:
        rec = (settlement or {}).get("exchange_reconciliation") or {}
        g9 = GateResult("TENNIS-9", "exchange_settlement_health", "PASS" if exchange_conflicts == 0 and not rules_id_changes else "FAIL",
                        {"conflicts": exchange_conflicts, "reconciled_against_independent_truth": (settlement or {}).get("exchange_reconciled"),
                         "reconciliation": rec, "rules_id_changes": rules_id_changes or [],
                         "scope": "MATCH_WINNER settlements whose match has an independent (non-Kalshi) result"})
    return g8, g9


def gate_10_clv_coverage(n_settled: int | None, n_with_close: int | None, n_actual_start_basis: int | None,
                         first_ball: dict | None = None, n_strict_settled: int | None = None,
                         n_quarantined_ab: int | None = None) -> GateResult:
    """TENNIS-10: CLV close coverage, measured against STRICT first-ball-anchored closes.

    The denominator is deliberately the predictions whose match HAS A/B first-ball truth. A close cut off
    at `scheduled_start - margin` no longer counts: it is not evidence that the quote preceded the first
    ball, and counting it would let the gate go green on exactly the rows this wave exists to distrust.
    Predictions with no first-ball truth are reported, not averaged away.

    `n_actual_start_basis` is that denominator (settled predictions whose match has A/B truth) and
    `n_strict_settled` the numerator from the same population (those with a strict CLV record). When the
    numerator is not supplied the older all-ledger strict count is used, as before."""
    fb = first_ball if first_ball is not None else first_ball_metrics()
    strict_rows = fb.get("strict_clv_rows")
    detail = {"settled": n_settled, "with_close": n_with_close, "actual_first_ball_basis": n_actual_start_basis,
              "strict_settled": n_strict_settled,
              "strict_clv_rows": strict_rows, "executable_close_rows": fb.get("executable_close_rows"),
              "matches_with_strict_truth": fb.get("strict_truths"),
              "observations_classified": fb.get("observations_classified"),
              "pct_strict_pregame": fb.get("pct_strict_pregame"),
              "horizons_populated": fb.get("horizons_populated"), "horizons_total": fb.get("horizons_total")}
    if not fb.get("strict_truths"):
        return GateResult("TENNIS-10", "clv_close_coverage", "UNKNOWN",
                          {"reason": "no match has A/B first-ball truth yet, so no strict close is possible", **detail})
    if n_settled is None:
        return GateResult("TENNIS-10", "clv_close_coverage", "UNKNOWN",
                          {"reason": "no settled predictions yet", **detail})
    if n_strict_settled is not None and n_actual_start_basis:
        rate = n_strict_settled / n_actual_start_basis
    else:
        rate = (strict_rows or 0) / n_settled if n_settled else 0
    detail["strict_rate"] = round(rate, 4)
    # 2026-10-05: a row QUARANTINED for being priced after the first ball (TENNIS-6 register) is not a pregame
    # prediction, so it cannot have a pregame close; counting it here penalised one defect twice. It leaves the
    # denominator only when it is in the append-only register; both rates are reported, the threshold is unchanged.
    if n_quarantined_ab is not None and n_strict_settled is not None and n_actual_start_basis:
        eligible = n_actual_start_basis - n_quarantined_ab
        rate = n_strict_settled / eligible if eligible else 0
        detail.update(quarantined_post_start_in_population=n_quarantined_ab, pregame_eligible=eligible,
                      strict_rate_pregame_eligible=round(rate, 4),
                      structural_note="levels with no first-ball source (Challenger, WTA 125, ITF) have no A/B truth and are "
                                      "outside this population by construction; see first_ball.watchlist")
    return GateResult("TENNIS-10", "clv_close_coverage", "PASS" if rate >= 0.95 else "FAIL", detail)


def gate_11_consistency(violations: list | None) -> GateResult:
    """TENNIS-11: probability consistency invariants across each priced match/tournament (see pricing.payoffs.check_consistency)."""
    if violations is None:
        return GateResult("TENNIS-11", "probability_consistency", "UNKNOWN", {"reason": "no projection run"})
    return GateResult("TENNIS-11", "probability_consistency", "PASS" if not violations else "FAIL", {"violations": violations[:20], "n": len(violations)})


def gate_12_ledger(ledger_root=None) -> GateResult:
    """TENNIS-12: append-only ledger hash chain intact."""
    from tennis_edge.ledger.predictions import PredictionLedger
    root = ledger_root or os.path.join(PROJ, "data", "research", "ledger")
    if not os.path.isdir(root) or not any(f.endswith(".jsonl") for f in os.listdir(root)):
        return GateResult("TENNIS-12", "append_only_ledger", "UNKNOWN", {"reason": "ledger empty"})
    v = PredictionLedger(root).verify_chain()
    return GateResult("TENNIS-12", "append_only_ledger", "PASS" if not v else "FAIL", {"violations": v[:10]})


def gate_13_reproducible(manifest_path=None) -> GateResult:
    """TENNIS-13: the processed dataset manifest exists with source run ids and a content hash that matches the file."""
    import hashlib
    p = manifest_path or os.path.join(PROJ, "data", "processed", "build_manifest.json")
    if not os.path.exists(p):
        return GateResult("TENNIS-13", "reproducible_artifacts", "UNKNOWN", {"reason": "no build manifest"})
    m = json.load(open(p))
    mp = os.path.join(os.path.dirname(p), "matches.parquet")
    if not os.path.exists(mp):
        return GateResult("TENNIS-13", "reproducible_artifacts", "FAIL", {"reason": "matches.parquet missing"})
    h = hashlib.sha256(open(mp, "rb").read()).hexdigest()
    ok = h == m.get("matches_sha256") and all(v.get("run") for v in m["sources"].values() if v.get("status") == "OK")
    return GateResult("TENNIS-13", "reproducible_artifacts", "PASS" if ok else "FAIL", {"hash_match": h == m.get("matches_sha256"), "built_at": m.get("built_at"), "rows": m.get("rows")})


def gate_14_source_freshness(max_age_days=8, now=None) -> GateResult:
    """TENNIS-14: the newest source snapshot with match data is younger than max_age_days and covers the current season."""
    runs = sorted(glob.glob(os.path.join(PROJ, "data", "sources", "*", "manifest.json")))
    best = None
    for r in runs:
        m = json.load(open(r))
        if any(k in m["sources"] for k in ("tennis_atp", "tennis_wta", "tml_database")):
            best = m
    if not best:
        return GateResult("TENNIS-14", "data_source_freshness", "UNKNOWN", {"reason": "no match-data source snapshot"})
    age = ((now or datetime.now(timezone.utc)) - datetime.fromisoformat(best["finished_at"])).total_seconds() / 86400
    seasons = [v.get("max_season_file") for v in best["sources"].values() if v.get("max_season_file")]
    cur = (now or datetime.now(timezone.utc)).year
    # a season FILE named 2026 can still end months ago (fork staleness): check the rating states' as_of_date
    as_of = {}
    for tour in ("ATP", "WTA"):
        sp = os.path.join(PROJ, "data", "processed", f"ratings_{tour}.json")
        if os.path.exists(sp):
            as_of[tour] = json.load(open(sp)).get("as_of_date")
    stale_days = {t: ((now or datetime.now(timezone.utc)).date() - datetime.fromisoformat(d).date()).days for t, d in as_of.items() if d}
    ok = age <= max_age_days and (not seasons or max(seasons) >= cur) and all(v <= max_age_days for v in stale_days.values()) and bool(stale_days)
    return GateResult("TENNIS-14", "data_source_freshness", "PASS" if ok else "FAIL",
                      {"run": best["run_id"], "snapshot_age_days": round(age, 2), "max_season_files": seasons, "ratings_as_of": as_of, "ratings_stale_days": stale_days})


def latest_run_files(directory: str) -> list[str]:
    """Per-run derived tables (<run_id>.jsonl, or .jsonl.gz since 2026-10-05), ordered by run id."""
    files = glob.glob(os.path.join(directory, "*.jsonl")) + glob.glob(os.path.join(directory, "*.jsonl.gz"))
    return sorted(files, key=lambda f: os.path.basename(f).split(".")[0])


def settlement_stats(research_root=None) -> dict | None:
    """What the settle job has actually written, read straight from its tables.

    Until 2026-09-27 nothing computed these, so `run_all()` passed `None` to TENNIS-8/9/10 and every one
    of them reported "no settled predictions yet" while the settlement table held 12,000+ rows. The gate
    was reading the wrong layer (nothing), not the settlement path failing."""
    root = research_root or os.path.join(PROJ, "data", "research")
    files = sorted(glob.glob(os.path.join(root, "settlements", "*.jsonl")))
    if not files:
        return None
    seen, rows = set(), []
    for f in files:
        with open(f) as fh:
            for line in fh:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if r.get("prediction_id") in seen:
                    continue
                seen.add(r.get("prediction_id"))
                rows.append(r)
    binary = [r for r in rows if r.get("gradeable")]
    sports = [r for r in binary if r.get("sports")]
    kalshi_derived = [r for r in sports if (r["sports"].get("source") or "") == "kalshi_result"]
    independent = [r for r in sports if (r["sports"].get("source") or "") not in ("", "kalshi_result")
                   and (r["sports"].get("confidence") or 0) >= 0.9]
    out = {"settled": len(rows), "settled_binary": len(binary), "settled_scalar": len(rows) - len(binary),
           "sports_truth_rows": len(sports), "sports_truth_kalshi_derived": len(kalshi_derived),
           "sports_truth_independent": len(independent), "settlement_files": len(files)}
    # 2026-10-05: the INDEPENDENT sports-truth lane (scripts/ops/sports_truth.py; tennis_edge/ledger/sports_truth.py)
    # resolves settled predictions against Sackmann / TML / ESPN results -- never Kalshi -- in its own derived table.
    st_files = sorted(glob.glob(os.path.join(root, "sports_truth", "*.jsonl.gz")))
    if st_files:
        import gzip as _gz
        binary_ids = {r.get("prediction_id") for r in binary}
        resolved, by_status, rec, structural = set(), {}, {}, {}
        with _gz.open(st_files[-1], "rt") as fh:
            for line in fh:
                try:
                    x = json.loads(line)
                except ValueError:
                    continue
                stt = (x.get("independent") or {}).get("status")
                by_status[stt] = by_status.get(stt, 0) + 1
                if stt == "RESOLVED" and x.get("prediction_id") in binary_ids:
                    resolved.add(x["prediction_id"])
                if stt in ("NOT_COVERED", "NO_CANONICAL_IDS"):
                    k = f"{x.get('tour')}|{x.get('level')}|{stt}"
                    structural[k] = structural.get(k, 0) + 1
                rs = (x.get("reconciliation") or {}).get("status")
                if rs:
                    rec[rs] = rec.get(rs, 0) + 1
        n_struct = by_status.get("NOT_COVERED", 0) + by_status.get("NO_CANONICAL_IDS", 0)
        old_ids = {r.get("prediction_id") for r in independent}
        out.update(sports_truth_independent=len(old_ids | resolved),
                   independent_truth_run=os.path.basename(st_files[-1]), independent_truth_by_status=by_status,
                   independent_truth_structural_non_coverage=structural,
                   independent_truth_rate_among_covered=round(by_status.get("RESOLVED", 0) / max(1, sum(by_status.values()) - n_struct), 4),
                   exchange_reconciliation=rec,
                   exchange_conflicts=rec.get("CONFLICT", 0),
                   exchange_reconciled=rec.get("AGREE", 0) + rec.get("EXPLAINED", 0) + rec.get("CONFLICT", 0))
    clvs = latest_run_files(os.path.join(root, "clv"))
    if clvs:
        latest = {}
        import gzip as _gzc
        with (_gzc.open(clvs[-1], "rt") if clvs[-1].endswith(".gz") else open(clvs[-1])) as fh:
            for line in fh:
                try:
                    c = json.loads(line)
                except ValueError:
                    continue
                latest[c.get("prediction_id")] = c
        settled_clv = [latest[r["prediction_id"]] for r in rows if r.get("prediction_id") in latest]
        out.update(clv_run=os.path.basename(clvs[-1]),
                   settled_with_ab_truth=sum(1 for c in settled_clv if c.get("truth_confidence") in ("A", "B")),
                   settled_with_close=sum(1 for c in settled_clv if c.get("close_ts")),
                   settled_strict_clv=sum(1 for c in settled_clv if c.get("strict")))
        out["_ab_truth_ids"] = [c.get("prediction_id") for c in settled_clv if c.get("truth_confidence") in ("A", "B")]
        out["_strict_research_rows"] = [{"strict": c.get("strict"), "timing_class": c.get("timing_class")}
                                        for c in latest.values()]
    return out


def _auto_extra() -> dict:
    """Evidence the gates can read for themselves: latest projection run (consistency, mapping), ledger
    rows, first-ball truth, and the settle job's own settlement and CLV tables."""
    extra = {}
    latest = os.path.join(PROJ, "data", "research", "projections", "latest.json")
    if os.path.exists(latest):
        pj = json.load(open(latest))
        extra["consistency_violations"] = pj.get("consistency_violations", [])
        amb = sum(1 for e in pj.get("excluded", []) if e.get("stage") == "identity" and "AMBIGUOUS" in e.get("reason", ""))
        extra["links_summary"] = {"AMBIGUOUS": amb, "ambiguous_used_in_production": 0, "MATCHED": len(pj.get("projected_tickers", []))}
    root = os.path.join(PROJ, "data", "research", "ledger")
    if os.path.isdir(root):
        from tennis_edge.ledger.predictions import PredictionLedger
        rows = list(PredictionLedger(root).rows())
        if rows:
            extra["ledger_rows"] = rows
            starts = {}
            for r in rows:
                s = r.get("scheduled_start")
                if s:
                    starts[r["match_id"]] = (None, datetime.fromisoformat(s.replace("Z", "+00:00")))
            extra["starts"] = starts
    # TENNIS-6 prefers ACTUAL first-ball truth over the scheduled fallback wherever truth exists
    fbroot = os.path.join(PROJ, "data", "firstball", "store")
    if os.path.isdir(fbroot):
        from tennis_edge.firstball.store import FirstBallStore
        for mid, t in FirstBallStore(fbroot).latest_truths().items():
            if mid in extra.get("starts", {}) and t.strict_eligible and not t.no_play:
                extra["starts"][mid] = (t.lower_bound_utc, extra["starts"][mid][1], t.upper_bound_utc)
    settled_at = {}
    for f in glob.glob(os.path.join(PROJ, "data", "research", "settlements", "*.jsonl")):
        with open(f) as fh:
            for line in fh:
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                ts = (r.get("exchange") or {}).get("settlement_ts")
                if ts and r.get("prediction_id"):
                    settled_at[r["prediction_id"]] = datetime.fromisoformat(ts.replace("Z", "+00:00"))
    if settled_at:
        extra["settled_at"] = settled_at
    qroot = os.path.join(PROJ, "data", "research", "quarantine")
    if os.path.isdir(qroot):
        from tennis_edge.ledger.quarantine import load as _load_quarantine
        extra["quarantine"], extra["quarantine_problems"] = _load_quarantine(qroot)
    st = settlement_stats()
    if st:
        ab_ids = st.pop("_ab_truth_ids", None)
        if ab_ids is not None and extra.get("quarantine") is not None:
            extra["n_quarantined_ab"] = sum(1 for i in ab_ids if i in extra["quarantine"])
        strict_rows = st.pop("_strict_research_rows", None)
        if strict_rows is not None:
            extra["strict_research_rows"] = strict_rows
        extra["settlement"] = st
        extra.setdefault("n_settled", st["settled"])
        extra.setdefault("sports_total", st["settled_binary"])
        extra.setdefault("sports_ok", st["sports_truth_independent"])
        if st.get("exchange_reconciled"):
            extra.setdefault("exchange_conflicts", st["exchange_conflicts"])
        if st.get("settled_with_ab_truth") is not None:
            extra.setdefault("n_actual_start_basis", st["settled_with_ab_truth"])
            extra.setdefault("n_with_close", st["settled_with_close"])
            extra.setdefault("n_strict_settled", st["settled_strict_clv"])
    return extra


# ---------------------------------------------------------------------------------------------------
# TENNIS-15: is every frozen experiment actually being fed, harvested and scored?
HEALTHY_NO_QUALIFYING_MARKETS = "HEALTHY_NO_QUALIFYING_MARKETS"
PRODUCER_NOT_RUNNING = "PRODUCER_NOT_RUNNING"
HARVEST_FAILED = "HARVEST_FAILED"
SCORING_ACTIVE = "SCORING_ACTIVE"
#: a producer that has not reported inside this window is dead, not quiet
PRODUCER_MAX_SILENCE_H = {"shadow_board_v1": 13.0, "model4_board_v1": 13.0, "external_scan": 2.0, "capture_books": 2.0}
CANDIDATE_PRODUCERS = {
    "EC-2026-001-MKTCOND-EXACT-SCORE": "model4_board_v1", "EC-2026-002-MKTCOND-GAME-SPREAD": "model4_board_v1",
    "EC-2026-003-GEN2-MODERATE-EVIDENCE": "shadow_board_v1", "W3-2026-001-ABSTAIN-ITF": "shadow_board_v1",
    "W3-2026-002-NONITF-POSITIVE-EDGE": "shadow_board_v1", "W4-2026-001-KALSHI-LONE-OUTLIER": "external_scan",
    "EC-2026-004-COHERENCE-EXECUTABLE": "capture_books"}


def _iso_dt(x):
    try:
        return datetime.fromisoformat(str(x).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None


def producer_last_seen(research_root: str, capture_root: str) -> dict:
    """producer -> last time it demonstrably ran (heartbeat, scan file or capture manifest)."""
    out = {}
    hb = os.path.join(research_root, "frozen_producers", "heartbeats.jsonl")
    if os.path.exists(hb):
        for line in open(hb):
            try:
                r = json.loads(line)
            except ValueError:
                continue
            t = _iso_dt(r.get("ran_at"))
            if t and (r.get("producer") not in out or t > out[r["producer"]]):
                out[r["producer"]] = t
    scans = sorted(glob.glob(os.path.join(research_root, "external", "scans", "scan_*.json")))
    if scans:
        try:
            out["external_scan"] = datetime.strptime(os.path.basename(scans[-1])[5:21], "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc)
        except ValueError:
            pass
    mans = sorted(glob.glob(os.path.join(capture_root, "*", "*.manifest.json")))
    if mans:
        try:
            out["capture_books"] = _iso_dt(json.load(open(mans[-1])).get("finished_at"))
        except (OSError, ValueError):
            pass
    return out


def gate_15_prospective_confirmation(research_root=None, capture_root=None, report_dir=None, now=None) -> GateResult:
    """TENNIS-15: per frozen candidate, is its producer alive, is the harvest succeeding, and where does
    scoring stand. Zero evidence because no qualifying market was listed is HEALTHY; a producer that has
    stopped reporting, or a harvest whose last failure is newer than its last success, is a FAILURE."""
    now = now or datetime.now(timezone.utc)
    research_root = research_root or os.path.join(PROJ, "data", "research")
    capture_root = capture_root or os.path.join(PROJ, "data", "kalshi", "capture")
    report_dir = report_dir or os.path.join(research_root, "candidate_confirmation")
    reports = {}
    for p in glob.glob(os.path.join(report_dir, "*.json")):
        try:
            r = json.load(open(p))
        except (OSError, ValueError):
            continue
        if isinstance(r, dict) and r.get("candidate_id"):
            reports[r["candidate_id"]] = r
    try:
        hs = json.load(open(os.path.join(report_dir, "HARVEST_STATUS.json")))
    except (OSError, ValueError):
        hs = {}
    if not reports and not hs:
        return GateResult("TENNIS-15", "prospective_confirmation_health", "UNKNOWN",
                          {"reason": "no candidate harvest has ever run"})
    last_ok, last_bad = _iso_dt(hs.get("last_success")), _iso_dt(hs.get("last_failure"))
    harvest_failed = last_ok is None or (last_bad is not None and last_bad > last_ok)
    seen = producer_last_seen(research_root, capture_root)
    starts_dir = os.path.join(research_root, "experiment_starts")
    per, bad = {}, []
    for cid, prod in CANDIDATE_PRODUCERS.items():
        rep = reports.get(cid) or {}
        summ = rep.get("summary") or {}
        start = None
        sp = os.path.join(starts_dir, f"{cid}.json")
        if os.path.exists(sp):
            start = json.load(open(sp)).get("effective_scorable_start")
        last = seen.get(prod)
        active = last is not None and (now - last).total_seconds() / 3600 <= PRODUCER_MAX_SILENCE_H[prod]
        needs_start = prod in ("shadow_board_v1", "model4_board_v1")
        status = rep.get("status")
        eligible = summ.get("eligible_n") or 0
        if harvest_failed:
            health = HARVEST_FAILED
        elif not active or (needs_start and start is None):
            health = PRODUCER_NOT_RUNNING
        elif eligible == 0:
            health = HEALTHY_NO_QUALIFYING_MARKETS
        elif status in ("INSUFFICIENT_N", "PENDING_SETTLEMENT", "PENDING_STRICT_CLV"):
            health = status
        else:
            health = SCORING_ACTIVE
        if health in (HARVEST_FAILED, PRODUCER_NOT_RUNNING):
            bad.append(cid)
        harvested = _iso_dt(rep.get("harvest_run_at")) or (
            datetime.strptime(rep["harvest_run"], "%Y%m%dT%H%M%SZ").replace(tzinfo=timezone.utc) if rep.get("harvest_run") else None)
        per[cid] = {"health": health, "producer": prod, "producer_required": True, "producer_active": active,
                    "producer_last_seen": last.isoformat() if last else None,
                    "effective_scorable_start": start, "eligible_n": eligible,
                    "settled_n": summ.get("settled_n"), "strict_clv_n": summ.get("strict_clv_n"),
                    "candidate_status": status, "last_evidence_at": rep.get("last_evidence_at"),
                    "evidence_age_h": round((now - _iso_dt(rep["last_evidence_at"])).total_seconds() / 3600, 1)
                    if _iso_dt(rep.get("last_evidence_at")) else None,
                    "harvest_age_h": round((now - harvested).total_seconds() / 3600, 1) if harvested else None}
    detail = {"last_harvest_success": hs.get("last_success"), "last_harvest_failure": hs.get("last_failure"),
              "last_harvest_failure_detail": (hs.get("last_failure_detail") or "")[-400:] or None,
              "harvest_failed": harvest_failed, "failing": bad, "candidates": per}
    return GateResult("TENNIS-15", "prospective_confirmation_health", "FAIL" if bad else "PASS", detail)


def gate_16_assisted_pipeline(research_root=None, firstball_root=None, now=None) -> GateResult:
    """TENNIS-16: ChatGPT-assisted decision pipeline health (slate, recording, settlement, integrity).
    An operations gate, separate from every autonomous candidate and from any authority: it never reads
    or writes a frozen model, candidate or experiment start, and a PASS says nothing about profitability."""
    from tennis_edge.assisted.health import gate_16
    research_root = research_root or os.path.join(PROJ, "data", "research")
    firstball_root = firstball_root or os.path.join(PROJ, "data", "firstball", "store")
    try:
        status, detail = gate_16(research_root, firstball_root=firstball_root, now=now)
    except Exception as e:                                                  # noqa: BLE001
        return GateResult("TENNIS-16", "assisted_decision_pipeline_health", "FAIL",
                          {"reason": f"gate raised {type(e).__name__}: {e}"})
    return GateResult("TENNIS-16", "assisted_decision_pipeline_health", status, detail)


def gate_17_discrepancy_integrity(research_root=None, now=None) -> GateResult:
    """TENNIS-17: model_market_discrepancy_integrity. Every model-market disagreement on the assisted slate and on
    recorded decisions is classified, and no EXTREME/HIGH_REVIEW gap escapes the sanity layer. Integrity, not
    profitability: a disagreement alone never fails it."""
    from tennis_edge.assisted.health import gate_17
    research_root = research_root or os.path.join(PROJ, "data", "research")
    try:
        status, detail = gate_17(research_root, now=now)
    except Exception as e:                                                  # noqa: BLE001
        return GateResult("TENNIS-17", "model_market_discrepancy_integrity", "FAIL",
                          {"reason": f"gate raised {type(e).__name__}: {e}"})
    return GateResult("TENNIS-17", "model_market_discrepancy_integrity", status, detail)


def gate_18_start_time_windows(research_root=None, firstball_root=None, now=None) -> GateResult:
    """TENNIS-18: start_time_window_health. Is the assisted workflow refreshed BEFORE the earliest credible first
    ball of each ATP/WTA window, from reconciled live start evidence rather than a nominal schedule?"""
    from tennis_edge.assisted.health import gate_18
    research_root = research_root or os.path.join(PROJ, "data", "research")
    firstball_root = firstball_root or os.path.join(PROJ, "data", "firstball", "store")
    try:
        status, detail = gate_18(research_root, firstball_root=firstball_root, now=now)
    except Exception as e:                                                  # noqa: BLE001
        return GateResult("TENNIS-18", "start_time_window_health", "FAIL", {"reason": f"gate raised {type(e).__name__}: {e}"})
    return GateResult("TENNIS-18", "start_time_window_health", status, detail)


def run_all(extra: dict | None = None) -> list[GateResult]:
    extra = {**_auto_extra(), **(extra or {})}
    out = [gate_1_discovery(), gate_2_taxonomy()]
    out += list(gate_3_4_active_coverage())
    out.append(gate_5_capture_freshness())
    out.append(gate_6_no_post_start_leakage(extra.get("ledger_rows", []), extra.get("starts", {}),
                                            extra.get("strict_research_rows"), extra.get("quarantine"),
                                            extra.get("quarantine_problems"), extra.get("settled_at"))
               if extra.get("ledger_rows") else GateResult("TENNIS-6", "no_post_start_leakage", "UNKNOWN", {"reason": "no ledger rows supplied"}))
    out.append(gate_7_identity(extra.get("links_summary")))
    fb = extra.get("first_ball") if extra.get("first_ball") is not None else first_ball_metrics()
    out += list(gate_8_9_truth(extra.get("sports_ok"), extra.get("sports_total"), extra.get("exchange_conflicts"),
                               extra.get("rules_id_changes"), first_ball=fb, settlement=extra.get("settlement")))
    out.append(gate_10_clv_coverage(extra.get("n_settled"), extra.get("n_with_close"),
                                    extra.get("n_actual_start_basis"), first_ball=fb,
                                    n_strict_settled=extra.get("n_strict_settled"),
                                    n_quarantined_ab=extra.get("n_quarantined_ab")))
    out.append(gate_11_consistency(extra.get("consistency_violations")))
    out.append(gate_12_ledger()); out.append(gate_13_reproducible()); out.append(gate_14_source_freshness())
    out.append(gate_15_prospective_confirmation())
    out.append(gate_16_assisted_pipeline())
    out.append(gate_17_discrepancy_integrity())
    out.append(gate_18_start_time_windows())
    return out
