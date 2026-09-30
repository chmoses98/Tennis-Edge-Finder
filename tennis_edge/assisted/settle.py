"""Attach later truth to assisted decisions and wagers WITHOUT touching them (Part 3).

Every settlement is a DERIVED row appended to `assisted_settlements.jsonl`; the decision and wager records
are only read. Two row kinds:

  DECISION  one per decision: the exchange result, the unit outcome of one contract of the decision's side
            at the decision's own executable price (BET/WATCH with a side), the same for the side the
            MODEL preferred (the pass-quality question), and strict CLV.
  WAGER     one per wager the person reported as filled: actual P&L on the actual stake.

Strict CLV (same rules as tennis_edge.ledger.clv): the close is the last executable quote strictly before
the EARLIEST possible first ball of A/B first-ball truth, and the entry must itself be STRICT_PREGAME.
Executable CLV = the side's close BID minus the side's entry ASK (what a taker could have sold back for);
midpoint CLV = the side's close mid minus its entry mid, secondary. Fees are never folded into CLV.

A row is appended when the exchange has settled the market. If strict CLV was unavailable then and becomes
available later (first-ball truth recovered), ONE revision row is appended; earlier rows stay as written.
"""
from __future__ import annotations

import os
from datetime import datetime, timedelta, timezone

from tennis_edge.firstball.classify import STRICT_PREGAME, classify
from tennis_edge.ledger.close import canonical_close
from tennis_edge.pricing.fees import taker_fee

from .market import first_ball_bound, iso, load_truths, quote_timelines, settlements, truth_for
from .schema import SETTLEMENT_FIELDS, side_prices
from .store import SETTLEMENTS_FILE, AppendOnlyJsonl, RecordStore, canonical_hash

SETTLER_VERSION = "assisted_settle_v1"
CLV_DAYS_AFTER = 3


def payout_yes(rec: dict) -> tuple[str | None, float | None]:
    try:
        v = float(rec.get("settlement_value_dollars"))
    except (TypeError, ValueError):
        return None, None
    res = (rec.get("result") or "").lower()
    if res == "yes":
        return "YES", v
    if res == "no":
        return "NO", v
    if res == "scalar":
        return "VOID_SCALAR", v
    return None, None


def _side_payout(side: str, pay_yes: float) -> float:
    return pay_yes if side == "YES" else 1.0 - pay_yes


def _clv(side, entry_bid, entry_ask, cc, strict_entry: bool) -> dict:
    """Strict executable and midpoint CLV of one side, or why there is none."""
    reasons = []
    cq = cc.quote
    entry_ok = entry_bid is not None and entry_ask is not None and 0 < entry_bid <= entry_ask < 1
    if not entry_ok:
        reasons.append("entry quote not executable")
    if cq is None or not cq.executable:
        reasons.append(f"no executable close ({cc.close_basis})")
    if not cc.strict:
        reasons.append(f"close basis {cc.close_basis} is not A/B first-ball anchored")
    if not strict_entry:
        reasons.append("entry not STRICT_PREGAME")
    if reasons:
        return {"strict": False, "strict_close": None, "strict_executable_clv": None, "midpoint_clv": None,
                "reason": "; ".join(reasons)}
    e_bid, e_ask = side_prices(side, entry_bid, entry_ask)
    c_bid, c_ask = side_prices(side, cq.yes_bid, cq.yes_ask)
    return {"strict": True,
            "strict_close": {"ts": cq.ts.isoformat(), "yes_bid": cq.yes_bid, "yes_ask": cq.yes_ask, "source": cq.source,
                             "basis": cc.close_basis, "cutoff": cc.cutoff.isoformat() if cc.cutoff else None,
                             "truth_confidence": cc.truth_confidence},
            "strict_executable_clv": round(c_bid - e_ask, 6),
            "midpoint_clv": round(0.5 * (c_bid + c_ask) - 0.5 * (e_bid + e_ask), 6), "reason": ""}


def _unit(side, price, pay_yes) -> dict:
    """One contract of `side` bought at `price`, taker fee included."""
    if side not in ("YES", "NO") or price is None or pay_yes is None:
        return {"gross_pnl": None, "fees": None, "net_pnl": None, "roi": None, "side_won": None}
    pay = _side_payout(side, pay_yes)
    fee = taker_fee(price, 1.0)
    gross = pay - price
    net = gross - fee
    return {"gross_pnl": round(gross, 6), "fees": fee, "net_pnl": round(net, 6), "roi": round(net / (price + fee), 6),
            "side_won": (pay == 1.0) if pay in (0.0, 1.0) else None}


def _row(**kw) -> dict:
    r = {k: kw.get(k) for k in SETTLEMENT_FIELDS}
    r.update({k: v for k, v in kw.items() if k not in r})
    return r


def settle(store_root: str, data_root: str, *, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    store = RecordStore(store_root)
    decisions = [d for d in store.records("decisions") if d.get("_fingerprint_ok")]
    wagers = [w for w in store.records("wagers") if w.get("_fingerprint_ok")]
    ledger = AppendOnlyJsonl(os.path.join(store_root, SETTLEMENTS_FILE))
    prior: dict[tuple, dict] = {}
    for r in ledger.rows():
        k = (r.get("row_kind"), r.get("decision_id"), r.get("wager_id"))
        if k not in prior or (r.get("revision") or 0) > (prior[k].get("revision") or 0):
            prior[k] = r
    if not decisions:
        return {"appended": 0, "settled_decisions": 0, "unsettled_decisions": 0, "settled_at": now.isoformat()}

    capture_root = os.path.join(data_root, "kalshi", "capture")
    tickers = {d["ticker"] for d in decisions}
    sets = settlements(capture_root, tickers)
    truths = load_truths(os.path.join(data_root, "firstball", "store"))
    need_days = set()
    for d in decisions:
        if d["ticker"] in sets:
            c = iso(d["created_at"])
            for i in range(-1, CLV_DAYS_AFTER + 1):
                need_days.add((c + timedelta(days=i)).strftime("%Y-%m-%d"))
    qmap = quote_timelines(capture_root, {d["ticker"] for d in decisions if d["ticker"] in sets}, sorted(need_days))
    by_dec = {d["decision_id"]: d for d in decisions}

    appended = 0
    unsettled = 0
    for d in decisions:
        s = sets.get(d["ticker"])
        if s is None:
            unsettled += 1
            continue
        result, pay = payout_yes(s)
        truth = truth_for(truths, d.get("event_id") or d["ticker"])
        created = iso(d["created_at"])
        timing = classify(created, truth)
        cc = canonical_close(qmap.get(d["ticker"], []), truth)
        bound = first_ball_bound(truth)
        post_start = bool(bound is not None and bound <= created)
        side = d.get("side")
        dclv = _clv(side, d.get("kalshi_bid"), d.get("kalshi_ask"), cc, timing.timing_class == STRICT_PREGAME) \
            if side in ("YES", "NO") else {"strict": False, "strict_close": None, "strict_executable_clv": None,
                                           "midpoint_clv": None, "reason": "no side (PASS without a side)"}
        m_side = d.get("model_preferred_side")
        mclv = _clv(m_side, d.get("kalshi_bid"), d.get("kalshi_ask"), cc, timing.timing_class == STRICT_PREGAME) \
            if m_side in ("YES", "NO") else None
        m_price = side_prices(m_side, d.get("kalshi_bid"), d.get("kalshi_ask"))[1] if m_side in ("YES", "NO") else None
        unit = _unit(side, d.get("side_entry_price"), pay)
        key = ("DECISION", d["decision_id"], None)
        old = prior.get(key)
        if old is not None and (old.get("strict_executable_clv") is not None or dclv["strict_executable_clv"] is None) \
                and (old.get("settlement_result") == result):
            continue
        row = _row(settlement_id=f"AS-{now.strftime('%Y%m%d')}-{canonical_hash([key, (old or {}).get('revision', 0) + 1])[:12]}",
                   row_kind="DECISION", decision_id=d["decision_id"], wager_id=None,
                   revision=(old or {}).get("revision", 0) + 1, supersedes=(old or {}).get("settlement_id"),
                   settled_at=now.isoformat(), settlement_result=result, settlement_value_yes=pay,
                   exchange_settled_at=s.get("settlement_ts"), side=side, side_won=unit["side_won"],
                   entry_price=d.get("side_entry_price"), contracts=1.0 if unit["net_pnl"] is not None else None,
                   gross_pnl=unit["gross_pnl"], fees=unit["fees"], net_pnl=unit["net_pnl"], roi=unit["roi"],
                   pnl_unit="ONE_CONTRACT_AT_DECISION_PRICE", stake_units_if_bet=d.get("stake_units_if_bet"),
                   strict_close=dclv["strict_close"], strict_executable_clv=dclv["strict_executable_clv"],
                   midpoint_clv=dclv["midpoint_clv"], clv_timing_class=timing.timing_class,
                   clv_exclusion_reason=dclv["reason"],
                   first_ball_confidence=truth.confidence if truth else "UNKNOWN",
                   first_ball_lower_utc=truth.lower_bound_utc.isoformat() if (truth and truth.lower_bound_utc) else None,
                   post_start_violation=post_start,
                   model_side=m_side, model_side_entry_price=m_price,
                   model_side_unit=_unit(m_side, m_price, pay) if m_side in ("YES", "NO") else None,
                   model_side_strict_executable_clv=(mclv or {}).get("strict_executable_clv"),
                   outcome_yes=(1 if result == "YES" else 0 if result == "NO" else None),
                   settlement_source="kalshi_capture_settlements", settled_by=SETTLER_VERSION)
        ledger.append(row)
        appended += 1

    for w in wagers:
        d = by_dec.get(w["decision_id"])
        s = sets.get(w["ticker"])
        if d is None or s is None or w["status"] == "CANCELLED":
            continue
        key = ("WAGER", w["decision_id"], w["wager_id"])
        old = prior.get(key)
        result, pay = payout_yes(s)
        truth = truth_for(truths, d.get("event_id") or w["ticker"])
        placed = iso(w["placed_at"])
        timing = classify(placed, truth)
        cc = canonical_close(qmap.get(w["ticker"], []), truth)
        if w["status"] == "VOIDED_BY_EXCHANGE":
            gross, fees = 0.0, 0.0
        else:
            gross = w["contracts"] * (_side_payout(w["side"], pay) - w["entry_price"])
            fees = w["fees"]
        net = gross - fees
        clv = None
        reason = ""
        cq = cc.quote
        if cc.strict and cq is not None and cq.executable and timing.timing_class == STRICT_PREGAME:
            clv = round(side_prices(w["side"], cq.yes_bid, cq.yes_ask)[0] - w["entry_price"], 6)
        else:
            reason = f"close {cc.close_basis}; entry timing {timing.timing_class}"
        if old is not None and (old.get("strict_executable_clv") is not None or clv is None):
            continue
        row = _row(settlement_id=f"AS-{now.strftime('%Y%m%d')}-{canonical_hash([key, (old or {}).get('revision', 0) + 1])[:12]}",
                   row_kind="WAGER", decision_id=w["decision_id"], wager_id=w["wager_id"],
                   revision=(old or {}).get("revision", 0) + 1, supersedes=(old or {}).get("settlement_id"),
                   settled_at=now.isoformat(), settlement_result=result, settlement_value_yes=pay,
                   exchange_settled_at=s.get("settlement_ts"), side=w["side"],
                   side_won=(_side_payout(w["side"], pay) == 1.0) if result in ("YES", "NO") else None,
                   entry_price=w["entry_price"], contracts=w["contracts"], stake_dollars=w["stake_dollars"],
                   gross_pnl=round(gross, 6), fees=round(fees, 6), net_pnl=round(net, 6),
                   roi=round(net / (w["stake_dollars"] + w["fees"]), 6) if (w["stake_dollars"] + w["fees"]) > 0 else None,
                   pnl_unit="ACTUAL_WAGER_DOLLARS", strict_close=({"ts": cq.ts.isoformat(), "yes_bid": cq.yes_bid,
                                                                    "yes_ask": cq.yes_ask, "basis": cc.close_basis}
                                                                   if clv is not None else None),
                   strict_executable_clv=clv, midpoint_clv=None, clv_timing_class=timing.timing_class,
                   clv_exclusion_reason=reason, first_ball_confidence=truth.confidence if truth else "UNKNOWN",
                   first_ball_lower_utc=truth.lower_bound_utc.isoformat() if (truth and truth.lower_bound_utc) else None,
                   post_start_violation=bool(w.get("placed_after_first_ball")),
                   settlement_source="kalshi_capture_settlements", settled_by=SETTLER_VERSION)
        ledger.append(row)
        appended += 1
    return {"appended": appended, "settled_decisions": len(decisions) - unsettled, "unsettled_decisions": unsettled,
            "settled_at": now.isoformat()}


def latest_settlements(store_root: str) -> dict[tuple, dict]:
    """(row_kind, decision_id, wager_id) -> highest-revision settlement row."""
    out: dict[tuple, dict] = {}
    for r in AppendOnlyJsonl(os.path.join(store_root, SETTLEMENTS_FILE)).rows():
        k = (r.get("row_kind"), r.get("decision_id"), r.get("wager_id"))
        if k not in out or (r.get("revision") or 0) > (out[k].get("revision") or 0):
            out[k] = r
    return out
