#!/usr/bin/env python3
"""Turn settled Kalshi match-winner markets into Opportunity-shaped research rows.

One row per EXECUTABLE ACTION, not per match: buying side A at its ask and buying side B at its ask are
two different decisions with two different prices, two different fees and two different outcomes, and a
selector that reasons about matches instead of actions will happily "select" a side nobody could buy.

Everything is walk-forward. Ratings come from `data/processed/asof/`, read strictly before the match
date, so no result from the day of the market or later can reach the price we would have quoted. Market
movement is built only from candles that CLOSED at or before the same cutoff as the quote itself.

What this dataset cannot do, stated once here rather than implied later: displayed depth is not in the
candle history, so `available_size` is an open-interest proxy and every economic figure downstream
assumes ONE contract at the last displayed ask. The live board uses real order-book depth.
"""
from __future__ import annotations

import argparse
import glob
import json
import math
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone, date

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.kalshi.markets import parse_market                       # noqa: E402
from tennis_edge.kalshi.families import SERIES                            # noqa: E402
from tennis_edge.identity.kalshi_map import KalshiPlayerMapper            # noqa: E402
from tennis_edge.models.asof import AsOfStates                            # noqa: E402
from tennis_edge.models.fair import compute_fair, PERTURBATIONS, FairConfig, FAIR_VERSION  # noqa: E402
from tennis_edge.models.quality import QualityInputs, data_quality        # noqa: E402
from tennis_edge.models.state import load_state                           # noqa: E402
from tennis_edge.pricing.competition import classify_competition, build_surface_lookup, lookup_surface  # noqa: E402
from tennis_edge.pricing.fees import taker_fee, breakeven_price, FeeSchedule  # noqa: E402
from tennis_edge.rules.formats import resolve_format, FormatResolutionError    # noqa: E402

PREGAME_HOURS = float(os.environ.get("PREGAME_HOURS", "7"))
MATCH_SERIES = [tk for tk, (fam, tour, lvl, disc) in SERIES.items()
                if fam == "MATCH_WINNER" and disc == "singles" and tour in ("ATP", "WTA")]


def ts(s):
    return int(datetime.fromisoformat(s.replace("Z", "+00:00")).timestamp()) if s else None


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def candle_series(path: str):
    """(end_ts, bid, ask, mid, volume, oi) for every hourly candle carrying a two-sided quote."""
    body = json.load(open(path))
    c60 = body.get("candles_60")
    cands = (c60[0] if isinstance(c60, list) else c60) or {}
    out = []
    for c in cands.get("candlesticks") or []:
        bid, ask = _f((c.get("yes_bid") or {}).get("close_dollars")), _f((c.get("yes_ask") or {}).get("close_dollars"))
        if bid is None or ask is None:
            continue
        out.append({"end_ts": int(c.get("end_period_ts") or 0), "bid": bid, "ask": ask,
                    "mid": 0.5 * (bid + ask), "volume": _f(c.get("volume_fp")) or 0.0,
                    "oi": _f(c.get("open_interest_fp")) or 0.0})
    out.sort(key=lambda r: r["end_ts"])
    return out


def prestart_quote(series, cutoff_ts, max_spread=0.15):
    best = None
    for c in series:
        if c["end_ts"] <= cutoff_ts:
            best = c
        else:
            break
    if not best or not (0 < best["bid"] <= best["ask"] < 1):
        return None
    if best["ask"] - best["bid"] > max_spread or best["oi"] <= 0:
        return None
    return best


def movement(series, cutoff_ts, quote):
    """Timestamp-safe movement context: nothing here is allowed to know anything after the cutoff."""
    hist = [c for c in series if c["end_ts"] <= cutoff_ts]
    if not hist:
        return {}
    now = quote["mid"]

    def mid_at(hours_back):
        want = cutoff_ts - hours_back * 3600
        prev = None
        for c in hist:
            if c["end_ts"] <= want:
                prev = c
            else:
                break
        return prev["mid"] if prev else None

    m1, m6, m24 = mid_at(1), mid_at(6), mid_at(24)
    last24 = [c for c in hist if c["end_ts"] >= cutoff_ts - 24 * 3600]
    diffs = [b["mid"] - a["mid"] for a, b in zip(last24, last24[1:])]
    changed = [c for c in hist if abs(c["mid"] - now) > 1e-9]
    return {
        "move_1h": None if m1 is None else now - m1,
        "move_6h": None if m6 is None else now - m6,
        "move_24h": None if m24 is None else now - m24,
        "abs_move_6h": None if m6 is None else abs(now - m6),
        "volatility_24h": float(np.std(diffs)) if len(diffs) >= 3 else None,
        "volume_24h": float(sum(c["volume"] for c in last24)),
        "n_quotes_24h": len(last24),
        "hours_since_last_change": None if not changed else (cutoff_ts - changed[-1]["end_ts"]) / 3600.0,
        "oi_at_quote": quote["oi"],
        "oi_growth_24h": (quote["oi"] - last24[0]["oi"]) if last24 else None,
        "history_hours": (cutoff_ts - hist[0]["end_ts"]) / 3600.0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--discovery", default=None, help="discovery snapshot holding candles")
    ap.add_argument("--asof", default=os.path.join(PROJ, "data", "processed", "asof"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "selector"))
    a = ap.parse_args()

    d = a.discovery
    if not d:
        runs = sorted(glob.glob(os.path.join(PROJ, "data", "kalshi", "discovery", "*", "candles")))
        d = os.path.dirname(runs[-1]) if runs else None
    if not d:
        print("::error::no discovery snapshot with candles"); return 1
    print(f"discovery: {d}", flush=True)

    states = {t: load_state(os.path.join(PROJ, "data", "processed", f"ratings_{t}.json")) for t in ("ATP", "WTA")}
    asof = {t: AsOfStates.load(os.path.join(a.asof, f"asof_{t}.json.gz")) for t in ("ATP", "WTA")}
    mapper = KalshiPlayerMapper(states, cache_path=os.path.join(PROJ, "data", "research", "wave3_map_cache.json"))
    mtab = pd.read_parquet(os.path.join(PROJ, "data", "processed", "matches.parquet"),
                           columns=["tourney_name", "surface", "season"])
    surf_lookup = build_surface_lookup(mtab)

    recs = {}
    for tk in MATCH_SERIES:
        for path in (os.path.join(d, "markets", f"{tk}.json"), os.path.join(d, "historical_markets", f"{tk}.json")):
            if not os.path.exists(path):
                continue
            obj = json.load(open(path))
            blocks = obj.values() if "markets" not in obj else [obj]
            for blk in blocks:
                for m in blk.get("markets") or []:
                    recs[m["ticker"]] = m
    by_event = defaultdict(list)
    for tk in MATCH_SERIES:
        for f in glob.glob(os.path.join(d, "candles", tk, "*.json")):
            t = os.path.basename(f)[:-5]
            if t in recs:
                by_event[recs[t]["event_ticker"]].append((t, f))

    rows, stats = [], defaultdict(int)
    for ev, lst in by_event.items():
        stats["events"] += 1
        pms = [(parse_market(recs[t]), recs[t], f) for t, f in lst]
        pms = [x for x in pms if x[0].status == "PARSED"]
        if len(pms) != 2:
            stats["not_two_parsed_sides"] += 1; continue
        sides = {pm.subject_is_a: (pm, m, f) for pm, m, f in pms}
        if True not in sides or False not in sides:
            stats["missing_side"] += 1; continue
        pm_a, m_a, f_a = sides[True]
        pm_b, m_b, f_b = sides[False]
        res_a = m_a.get("result")
        if res_a not in ("yes", "no"):
            stats["non_binary_settlement"] += 1; continue
        info = classify_competition(pm_a.competition, pm_a.tour)
        tour = info["tour"] if info["tour"] in ("ATP", "WTA") else (
            "WTA" if pm_a.series_ticker.startswith(("KXWTA", "KXITFW")) else "ATP")
        sched, close_t = ts(m_a.get("occurrence_datetime") or m_a.get("expected_expiration_time")), ts(m_a.get("close_time"))
        if not sched or not close_t:
            stats["no_schedule"] += 1; continue
        cutoff = min(sched - 300, close_t - PREGAME_HOURS * 3600)
        # ONE book prices both actions. On a Kalshi binary, buying NO is buying the other player at
        # 1 - yes_bid, so the opposite ticker is a cross-check rather than a requirement; insisting on
        # both books would discard a third of the settled universe for no gain in executability.
        books = []
        for pm, _m, f in ((pm_a, m_a, f_a), (pm_b, m_b, f_b)):
            ser = candle_series(f)
            q = prestart_quote(ser, cutoff)
            if q:
                books.append((pm.subject_is_a, ser, q))
        if not books:
            stats["no_prestart_quote"] += 1; continue
        # reference book: the freshest quote at the cutoff, tie-broken by the tighter spread
        is_a_ref, ref_series, ref_q = max(books, key=lambda b: (b[2]["end_ts"], -(b[2]["ask"] - b[2]["bid"])))
        try:
            fmt = resolve_format(tour, info["level"], 2026,
                                 info["competition"] if info["level"] == "GRAND_SLAM" else None, "singles")
        except FormatResolutionError:
            stats["format_unresolved"] += 1; continue
        kd = datetime.fromtimestamp(sched, tz=timezone.utc)
        on = kd.date()
        ma = mapper.resolve(tour, pm_a.subject, pm_a.competitor_id, on)
        mb = mapper.resolve(tour, pm_b.subject, pm_b.competitor_id, on)
        if ma["status"] != "MAPPED" or mb["status"] != "MAPPED":
            stats["unmapped_identity"] += 1; continue
        surface, _ = lookup_surface(pm_a.competition, info["surface_hint"], surf_lookup)
        st = asof[tour]
        fairs = {}
        for cfg in PERTURBATIONS:
            fr = compute_fair(st, ma["player_id"], mb["player_id"], tour=tour, level=info["level"],
                              surface=surface, fmt=fmt, on=on, cfg=cfg)
            if fr is not None:
                fairs[cfg.name] = fr
        if "base" not in fairs:
            stats["no_rating_state"] += 1; continue
        base = fairs["base"]
        env = [f.p_gen2_blend for f in fairs.values()]

        ra_rec, rb_rec = st.state(ma["player_id"], on), st.state(mb["player_id"], on)
        def _stale(rec):
            ld = rec.get("last_date")
            try:
                return (on - date.fromisoformat(str(ld)[:10])).days
            except (TypeError, ValueError):
                return None
        stale = [x for x in (_stale(ra_rec), _stale(rb_rec)) if x is not None]
        dq = data_quality(QualityInputs(
            n_matches_a=ra_rec.get("n", 0), n_matches_b=rb_rec.get("n", 0),
            serve_points_a=base.evidence_a, serve_points_b=base.evidence_b,
            days_since_last_a=_stale(ra_rec), days_since_last_b=_stale(rb_rec),
            level_familiarity=1.0, identity_confidence=min(ma["confidence"], mb["confidence"]),
            format_known=True))

        y_a = 1.0 if res_a == "yes" else 0.0
        mv_ref = movement(ref_series, cutoff, ref_q)
        # orient the reference book onto side A
        if is_a_ref:
            ask_a, bid_a = ref_q["ask"], ref_q["bid"]
        else:
            ask_a, bid_a = 1 - ref_q["bid"], 1 - ref_q["ask"]
        p_mkt_a = 0.5 * (ask_a + bid_a)
        ref_ticker = (pm_a if is_a_ref else pm_b).ticker
        # a two-sided cross-check when the other book also quoted: how far apart the two mids are
        other_mid = next((0.5 * (q["ask"] + q["bid"]) if isa else 1 - 0.5 * (q["ask"] + q["bid"])
                          for isa, _s, q in books if isa != is_a_ref), None)
        two_sided_gap = None if other_mid is None else abs(other_mid - p_mkt_a)

        for label, (pm, ask, bid, sign, fair_p, p_mkt, y) in {
            "A": ("A", (pm_a, ask_a, bid_a, 1.0, base.p_gen2_blend, p_mkt_a, y_a)),
            "B": ("B", (pm_b, 1 - bid_a, 1 - ask_a, -1.0, 1 - base.p_gen2_blend, 1 - p_mkt_a, 1 - y_a)),
        }.values():
            q = ref_q
            mv = {k: (v * sign if (v is not None and k in ("move_1h", "move_6h", "move_24h")) else v)
                  for k, v in mv_ref.items()}
            fee = taker_fee(ask, 1.0, FeeSchedule())
            env_side = [p if label == "A" else 1 - p for p in env]
            rows.append({
                "event": ev, "ticker": pm.ticker, "series": pm.series_ticker, "side_label": label,
                "tour": tour, "level": info["level"], "surface": surface, "competition": pm.competition,
                "physical_match_id": f"{tour}:{min(ma['player_id'], mb['player_id'])}:{max(ma['player_id'], mb['player_id'])}:{on}",
                "sched_utc": kd.isoformat(), "sched_date": str(on), "cutoff_ts": cutoff,
                "quote_age_s": float(cutoff - q["end_ts"]), "reference_ticker": ref_ticker,
                "y": y, "kalshi_bid": bid, "kalshi_ask": ask, "kalshi_mid": 0.5 * (ask + bid),
                "kalshi_oi": q["oi"], "two_sided_gap": two_sided_gap,
                "spread": ask - bid, "p_market_devig": p_mkt, "fee": fee,
                "p_elo": base.p_elo if label == "A" else 1 - base.p_elo,
                "p_sr": base.p_sr if label == "A" else 1 - base.p_sr,
                "p_gen2": base.p_gen2 if label == "A" else 1 - base.p_gen2,
                "p_fair": fair_p, "p_env_min": min(env_side), "p_env_max": max(env_side),
                "blend_weight": base.blend_weight, "serve_level": base.serve_level,
                "ev_side": base.evidence_a if label == "A" else base.evidence_b,
                "ev_other": base.evidence_b if label == "A" else base.evidence_a,
                "ev_min": min(base.evidence_a, base.evidence_b),
                "n_matches_min": min(ra_rec.get("n", 0), rb_rec.get("n", 0)),
                "days_stale_max": max(stale) if stale else None,
                "identity_confidence": min(ma["confidence"], mb["confidence"]),
                "data_quality": dq["data_quality_score"], "data_quality_grade": dq["grade"],
                "hours_to_sched": (sched - cutoff) / 3600.0,
                **{f"mv_{k}": v for k, v in mv.items()},
            })
        stats["linked"] += 1

    df = pd.DataFrame(rows)
    os.makedirs(a.out, exist_ok=True)
    df.to_parquet(os.path.join(a.out, "opportunities.parquet"), index=False)
    meta = {"built_at": datetime.now(timezone.utc).isoformat(), "discovery": os.path.basename(d),
            "fair_version": FAIR_VERSION, "pregame_hours": PREGAME_HOURS, "funnel": dict(stats),
            "rows": int(len(df)), "matches": int(len(df) / 2) if len(df) else 0,
            "perturbations": [c.name for c in PERTURBATIONS],
            "date_range": [df.sched_date.min(), df.sched_date.max()] if len(df) else None}
    json.dump(meta, open(os.path.join(a.out, "dataset_manifest.json"), "w"), indent=1, default=str)
    print(json.dumps(meta, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
