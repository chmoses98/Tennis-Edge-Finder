#!/usr/bin/env python3
"""The owner-facing board: what the system would look at today, and what it refuses.

Reads the live capture (quotes carry displayed depth, which the historical candle archive does not),
prices every match-winner contract from walk-forward ratings, and applies selector_v1. Most of the board
comes back PASS. That is the product working, not the product failing.

Nothing here places, recommends or sizes a real wager. Every row is written to an append-only,
hash-chained store first and rendered second, so the board that gets read is the board that was
recorded.
"""
from __future__ import annotations

import argparse
import glob
import gzip
import json
import os
import sys
import uuid
from datetime import datetime, timezone, date

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

import pandas as pd  # noqa: E402

from tennis_edge.identity.kalshi_map import KalshiPlayerMapper           # noqa: E402
from tennis_edge.kalshi.families import SERIES                           # noqa: E402
from tennis_edge.kalshi.markets import parse_market                      # noqa: E402
from tennis_edge.models.asof import AsOfStates                           # noqa: E402
from tennis_edge.models.fair import compute_fair, PERTURBATIONS          # noqa: E402
from tennis_edge.models.quality import QualityInputs, data_quality       # noqa: E402
from tennis_edge.models.state import load_state                          # noqa: E402
from tennis_edge.opportunity import Opportunity, OpportunityStore, qualify  # noqa: E402
from tennis_edge.opportunity.qualify import QualificationInputs          # noqa: E402
from tennis_edge.pricing.competition import classify_competition, build_surface_lookup, lookup_surface  # noqa: E402
from tennis_edge.pricing.fees import taker_fee, breakeven_price, FeeSchedule   # noqa: E402
from tennis_edge.rules.formats import resolve_format, FormatResolutionError    # noqa: E402
from tennis_edge.selector.decide import decide, DecisionInputs, DecisionPolicy, SELECTOR_VERSION  # noqa: E402

MATCH_SERIES = {tk for tk, (fam, tour, lvl, disc) in SERIES.items()
                if fam == "MATCH_WINNER" and disc == "singles" and tour in ("ATP", "WTA")}


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def latest_quotes(capture_root: str) -> dict:
    """Carry-forward reconstruction: capture writes only CHANGED markets, so the current board is the
    accumulation of every snapshot so far today, not the last file."""
    days = sorted(d for d in glob.glob(os.path.join(capture_root, "*")) if os.path.isdir(d))
    if not days:
        return {}
    out = {}
    for f in sorted(glob.glob(os.path.join(days[-1], "*.quotes.jsonl.gz"))):
        with gzip.open(f, "rt") as fh:
            for line in fh:
                if not line.strip():
                    continue
                m = json.loads(line)
                out[m["ticker"]] = m
    return out


def render(rows, meta) -> str:
    L = [f"# TENNIS -- SHADOW ONLY ({meta['generated_at'][:16]}Z)", "",
         f"**REAL-MONEY AUTHORITY: OFF.** selector {SELECTOR_VERSION}. "
         f"{meta['n_markets']} contracts priced, {meta['counts'].get('PASS', 0)} PASS, "
         f"{meta['counts'].get('WATCH', 0)} WATCH, {meta['counts'].get('SHADOW_BET', 0)} SHADOW BET.", ""]
    shown = [r for r in rows if r.decision in ("SHADOW_BET", "WATCH")]
    shown.sort(key=lambda r: (r.decision != "SHADOW_BET", -(r.fee_adjusted_edge or 0)))
    if not shown:
        L += ["Nothing on the board clears the gates today. That is a decision, not an outage.", ""]
    for r in shown[:25]:
        L += [f"## {r.decision} -- {r.event}", "",
              f"* Market: `{r.ticker}` {r.side} at **{r.executable_ask:.2f}** "
              f"(bid {r.executable_bid:.2f}, spread {r.spread*100:.0f}c, size {r.available_size:.0f})",
              f"* Fair: **{r.fair_prob*100:.1f}%** (envelope {r.fair_prob_low*100:.1f}-{r.fair_prob_high*100:.1f}%)",
              f"* Raw edge {r.raw_edge*100:+.1f}c / after fees {r.fee_adjusted_edge*100:+.1f}c / "
              f"robust {r.robust_edge*100:+.1f}c",
              f"* Bet up to **{r.bet_up_to:.2f}**; EV per contract at +1c/+2c/+3c: "
              + " / ".join(f"{r.ev_curve.get(k, 0)*100:+.1f}c" for k in ("+1c", "+2c", "+3c")),
              f"* Data quality {r.data_quality_grade} ({r.data_quality_score:.2f}), "
              f"serve evidence {r.serve_evidence_points:.0f} points on the thinner player",
              f"* FIRST BALL: {r.first_ball_classification} (confidence {r.first_ball_confidence})",
              "", f"**For:** {r.reason_for}", "", f"**Against:** {r.reason_against}", ""]
    L += ["---", "", "No wager is recommended. A SHADOW_BET row means the opportunity survived every "
          "check this system knows how to run; Wave 3 found no subset in which our probability was more "
          "accurate than the Kalshi price, so survival is a statement about our checks, not about the "
          "market.", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"))
    ap.add_argument("--asof", default=os.path.join(PROJ, "data", "processed", "asof"))
    ap.add_argument("--store", default=os.path.join(PROJ, "data", "research", "opportunities"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "selector", "SHADOW_BOARD.md"))
    ap.add_argument("--no-store", action="store_true", help="render without appending to the store")
    a = ap.parse_args()

    quotes = latest_quotes(a.capture)
    if not quotes:
        print("::warning::no capture on disk; nothing to render"); return 0
    states = {t: load_state(os.path.join(PROJ, "data", "processed", f"ratings_{t}.json")) for t in ("ATP", "WTA")}
    asof = {t: AsOfStates.load(os.path.join(a.asof, f"asof_{t}.json.gz")) for t in ("ATP", "WTA")}
    mapper = KalshiPlayerMapper(states, cache_path=os.path.join(PROJ, "data", "research", "wave3_map_cache.json"))
    mtab = pd.read_parquet(os.path.join(PROJ, "data", "processed", "matches.parquet"),
                           columns=["tourney_name", "surface", "season"])
    surf_lookup = build_surface_lookup(mtab)

    by_event = {}
    for tk, m in quotes.items():
        if m.get("status") != "active":
            continue
        series = tk.split("-")[0]
        if series not in MATCH_SERIES:
            continue
        by_event.setdefault(m.get("event_ticker"), []).append(m)

    now = datetime.now(timezone.utc)
    store = OpportunityStore(a.store)
    rows, counts, skipped = [], {}, {}
    for ev, ms in by_event.items():
        pms = [(parse_market(m), m) for m in ms]
        pms = [x for x in pms if x[0].status == "PARSED"]
        if len(pms) != 2:
            skipped["not_two_sides"] = skipped.get("not_two_sides", 0) + 1; continue
        sides = {pm.subject_is_a: (pm, m) for pm, m in pms}
        if True not in sides or False not in sides:
            skipped["missing_side"] = skipped.get("missing_side", 0) + 1; continue
        pm_a, m_a = sides[True]
        pm_b, m_b = sides[False]
        info = classify_competition(pm_a.competition, pm_a.tour)
        tour = info["tour"] if info["tour"] in ("ATP", "WTA") else (
            "WTA" if pm_a.series_ticker.startswith(("KXWTA", "KXITFW")) else "ATP")
        sched_s = m_a.get("occurrence_datetime") or m_a.get("expected_expiration_time")
        on = (datetime.fromisoformat(sched_s.replace("Z", "+00:00")).date() if sched_s else now.date())
        ma = mapper.resolve(tour, pm_a.subject, pm_a.competitor_id, on)
        mb = mapper.resolve(tour, pm_b.subject, pm_b.competitor_id, on)
        if ma["status"] != "MAPPED" or mb["status"] != "MAPPED":
            skipped["unmapped_identity"] = skipped.get("unmapped_identity", 0) + 1; continue
        try:
            fmt = resolve_format(tour, info["level"], on.year,
                                 info["competition"] if info["level"] == "GRAND_SLAM" else None, "singles")
        except FormatResolutionError:
            skipped["format_unresolved"] = skipped.get("format_unresolved", 0) + 1; continue
        surface, _ = lookup_surface(pm_a.competition, info["surface_hint"], surf_lookup)
        st = asof[tour]
        fairs = {}
        for cfg in PERTURBATIONS:
            fr = compute_fair(st, ma["player_id"], mb["player_id"], tour=tour, level=info["level"],
                              surface=surface, fmt=fmt, on=on, cfg=cfg)
            if fr is not None:
                fairs[cfg.name] = fr
        if "base" not in fairs:
            skipped["no_rating_state"] = skipped.get("no_rating_state", 0) + 1; continue
        base = fairs["base"]
        env = [f.p_gen2_blend for f in fairs.values()]
        ra_rec, rb_rec = st.state(ma["player_id"], on), st.state(mb["player_id"], on)

        def _stale(rec):
            try:
                return (on - date.fromisoformat(str(rec.get("last_date"))[:10])).days
            except (TypeError, ValueError):
                return None
        dq = data_quality(QualityInputs(
            n_matches_a=ra_rec.get("n", 0), n_matches_b=rb_rec.get("n", 0),
            serve_points_a=base.evidence_a, serve_points_b=base.evidence_b,
            days_since_last_a=_stale(ra_rec), days_since_last_b=_stale(rb_rec), level_familiarity=1.0,
            identity_confidence=min(ma["confidence"], mb["confidence"]), format_known=True))

        for pm, m, fair_p, env_side in ((pm_a, m_a, base.p_gen2_blend, env),
                                        (pm_b, m_b, 1 - base.p_gen2_blend, [1 - p for p in env])):
            ask, bid = _f(m.get("yes_ask_dollars")), _f(m.get("yes_bid_dollars"))
            size = _f(m.get("yes_ask_size_fp"))
            if ask is None or bid is None or not (0 < bid <= ask < 1):
                skipped["no_two_sided_quote"] = skipped.get("no_two_sided_quote", 0) + 1; continue
            fee = taker_fee(ask, 1.0, FeeSchedule())
            raw = fair_p - ask
            feeadj = raw - fee
            robust = min(env_side) - ask - fee
            quote_age = (now - datetime.fromisoformat(m["captured_at"])).total_seconds()
            q = qualify(QualificationInputs(
                family="MATCH_WINNER", identity_confidence=min(ma["confidence"], mb["confidence"]),
                fair_prob=fair_p, executable_ask=ask, executable_bid=bid, quote_age_seconds=quote_age,
                available_size=size, fee_per_contract=fee, first_ball_classification="START_UNKNOWN",
                data_quality_score=dq["data_quality_score"]))
            dec = decide(DecisionInputs(
                qualification_ok=q.ok, fee_adjusted_edge=feeadj, robust_edge=robust,
                env_width=max(env_side) - min(env_side), data_quality=dq["data_quality_score"],
                level=info["level"], lanes_agree=bool(
                    (base.p_elo - 0.5) * (base.p_gen2_blend - 0.5) > 0)))
            ev_curve = {}
            for c in (0, 1, 2, 3, 5):
                p = min(ask + c / 100.0, 0.99)
                ev_curve[f"+{c}c"] = fair_p - p - taker_fee(p, 1.0, FeeSchedule())
            opp = Opportunity(
                opportunity_id=str(uuid.uuid4()), generated_at=now.isoformat(),
                physical_match_id=f"{tour}:{min(ma['player_id'], mb['player_id'])}:{max(ma['player_id'], mb['player_id'])}:{on}",
                event=ev, ticker=pm.ticker, family="MATCH_WINNER", side="YES", strike=None,
                lane="MODEL_3", model_version="gen2_dyn_hier_sr_v1+fair_v1", fair_prob=fair_p,
                uncertainty=0.5 * (max(env_side) - min(env_side)),
                fair_prob_low=min(env_side), fair_prob_high=max(env_side),
                executable_ask=ask, executable_bid=bid, midpoint=0.5 * (ask + bid), spread=ask - bid,
                available_size=size, fee_per_contract=fee, raw_edge=raw, fee_adjusted_edge=feeadj,
                uncertainty_adjusted_edge=feeadj - 0.5 * (max(env_side) - min(env_side)),
                robust_edge=robust, bet_up_to=breakeven_price(fair_p, FeeSchedule()), ev_curve=ev_curve,
                data_quality_score=dq["data_quality_score"], data_quality_grade=dq["grade"],
                serve_evidence_points=min(base.evidence_a, base.evidence_b),
                identity_confidence=min(ma["confidence"], mb["confidence"]),
                source_freshness_days=max([x for x in (_stale(ra_rec), _stale(rb_rec)) if x is not None] or [None]),
                first_ball_classification="START_UNKNOWN", first_ball_confidence="UNKNOWN",
                seconds_to_first_ball=None, seconds_to_first_ball_basis="NONE",
                quote_age_seconds=quote_age,
                market_movement={"basis": "live capture; no pre-cutoff candle history in this path"},
                liquidity_context={"displayed_ask_size": size, "open_interest": _f(m.get("open_interest_fp")),
                                   "volume_24h": _f(m.get("volume_24h_fp"))},
                selector_score=None, selector_version=SELECTOR_VERSION, decision=dec["decision"],
                reason_for=dec["reason_for"], reason_against=dec["reason_against"],
                candidate_ids=(), qualification=q.checks)
            rows.append(opp)
            counts[opp.decision] = counts.get(opp.decision, 0) + 1
            if not a.no_store:
                store.append(opp)

    meta = {"generated_at": now.isoformat(), "n_markets": len(rows), "counts": counts,
            "skipped": skipped, "selector_version": SELECTOR_VERSION,
            "authority": "RESEARCH_ONLY_NO_REAL_MONEY"}
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    open(a.out, "w").write(render(rows, meta) + "\n")
    json.dump(meta, open(os.path.splitext(a.out)[0] + ".json", "w"), indent=1, default=str)
    print(json.dumps(meta, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
