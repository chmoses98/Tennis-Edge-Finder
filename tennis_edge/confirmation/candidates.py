"""Per-candidate harvesters: the frozen rule, applied to what was captured after the freeze.

Each harvester does the same five things, in this order, and nothing else:

  1. take the candidate's own `confirmation_start` from its frozen file;
  2. walk the immutable observation stream(s) the rule needs, dropping everything captured earlier;
  3. evaluate the frozen inclusion rule on the fields AS PRESERVED AT CAPTURE -- a field that was not
     preserved makes the row UNSCORABLE, it is never reconstructed;
  4. deduplicate exactly as the candidate says (W4: the first qualifying observation of each contract);
  5. attach later truth (settlement, first-ball timing, strict close) and compute ONLY the metrics the
     candidate's frozen conditions name.

The thresholds live in the frozen candidate text and are transcribed below as constants next to the
sentence they come from. None of them is a parameter: a harvester that could be called with a different
threshold would be a tuning surface.
"""
from __future__ import annotations

import gzip
import json
import os
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from statistics import median

from tennis_edge.confirmation import evidence as ev
from tennis_edge.confirmation import sources as src
from tennis_edge.confirmation import stats
from tennis_edge.confirmation.status import (KIND_ABSTENTION, KIND_EXISTENCE, KIND_PRICING, KIND_TRADE,
                                             ScoreSummary, assign_status)
from tennis_edge.firstball.classify import (AMBIGUOUS, POST_START, START_UNKNOWN, STRICT_PREGAME,
                                            classify)
from tennis_edge.ledger.close import Quote, canonical_close
from tennis_edge.ledger.clv import clv_record

HARVESTER_VERSION = 1

# ---------------------------------------------------------------------------------------------------
# Field provenance, per candidate. This table IS the audit: every field an inclusion rule or a pass
# condition needs, where it lives, and whether it existed at capture time. Classes:
PRESERVED = "PRESERVED_AT_CAPTURE"
DERIVABLE = "DERIVABLE_FROM_IMMUTABLE_CAPTURE"
LATER_TRUTH = "LATER_TRUTH_ATTACHMENT_ALLOWED"
NOT_AVAILABLE = "NOT_AVAILABLE"
AMBIGUOUS_FIELD = "AMBIGUOUS"
FIELD_CLASSES = (PRESERVED, DERIVABLE, LATER_TRUTH, NOT_AVAILABLE, AMBIGUOUS_FIELD)

_SETTLE = ("settlement result", "capture settlements sweep (Kalshi status=settled), discovery settled block", LATER_TRUTH)
_FB = ("first-ball truth (A/B)", "firstball/store truths, keyed by Kalshi event ticker", LATER_TRUTH)
_CLOSE = ("strict executable close", "capture quotes + order books + candles, cut at the first-ball lower bound", LATER_TRUTH)

FIELD_AUDIT: dict[str, list[tuple[str, str, str, str]]] = {
    "EC-2026-001-MKTCOND-EXACT-SCORE": [
        ("market family EXACT_SET_SCORE, listed contract", "capture quote records (rules text)", PRESERVED, ""),
        ("two-sided match-winner quote, de-vig in [0.05, 0.95]", "capture quote records of the sibling match-winner event", PRESERVED, ""),
        ("market_conditioned_v1 exact-score distribution at decision time", "none: no prospective job computes it", NOT_AVAILABLE,
         "the market-conditioned lane exists only in scripts/research/market_conditioned_study.py (retrospective)"),
        ("pure fundamental (Gen-2) exact-score distribution at decision time", "none", NOT_AVAILABLE,
         "the ledger's EXACT_SET_SCORE rows are priced by elo_surface_k_lo+sr_v0.1 (Gen-1 DP), not Gen-2"),
        ("Gen-2 state for both players at decision time", "none preserved per row", NOT_AVAILABLE, ""),
        _SETTLE + ("",), ("final exact set score", "Kalshi exact-score settlement", LATER_TRUTH, ""),
    ],
    "EC-2026-002-MKTCOND-GAME-SPREAD": [
        ("market family GAME_SPREAD / TOTAL_GAMES with a quoted line", "capture quote records", PRESERVED, ""),
        ("market_conditioned_v1 game-differential / total-games expectation", "none", NOT_AVAILABLE,
         "never computed prospectively"),
        ("fundamental-lane expectation", "none", NOT_AVAILABLE,
         "the ledger's spread/total rows are Gen-1 DP prices, not the frozen lanes"),
        ("completed-match game differential (no retirement)", "no games-level sports truth is wired into settlement", NOT_AVAILABLE,
         "Kalshi settles each line as yes/no; games won by each player are not captured"),
        _SETTLE + ("",),
    ],
    "EC-2026-003-GEN2-MODERATE-EVIDENCE": [
        ("MATCH_WINNER singles, ATP or WTA", "every stream", PRESERVED, ""),
        ("Gen-2 (gen2_dyn_hier_sr_v1) probability at prediction time", "shadow-board opportunities (fair_prob); dislocation rows (model_fair, surface=None)",
         AMBIGUOUS_FIELD, "preserved only in one shadow-board run (2026-09-12 17:13, 502 rows); dislocation rows carry a Gen-2 blend computed WITHOUT surface, a different input set"),
        ("thinner player's observed serve points in the Gen-2 state", "shadow-board serve_evidence_points", AMBIGUOUS_FIELD,
         "same single run; absent from the ledger (which holds Gen-1 SR points) and from dislocation rows"),
        ("Gen-1 Elo probability at the same decision", "prediction ledger models.ELO", AMBIGUOUS_FIELD,
         "preserved in the ledger, but never on the same row, instant or rating artifact as a Gen-2 probability"),
        ("Kalshi executable ask / mid at decision", "ledger market_quote; opportunities; dislocations", PRESERVED, ""),
        _FB + ("",), _CLOSE + ("",), _SETTLE + ("",),
    ],
    "EC-2026-004-COHERENCE-EXECUTABLE": [
        ("executable bid/ask on every leg", "capture order books (orderbook_fp) per pass", PRESERVED,
         "read from the book itself, so price and depth come from one immutable observation"),
        ("order-book depth on every leg", "capture order books", PRESERVED,
         "before 2026-09-27 the reader looked for legacy keys and saw no depth; fixed, see audit"),
        ("contract semantics (family, side, line, exact score)", "rules text in the capture quote records", DERIVABLE,
         "parse_market on the captured market record"),
        ("Kalshi taker fee per leg", "tennis_edge.pricing.fees at each leg's price", DERIVABLE, ""),
    ],
    "W3-2026-001-ABSTAIN-ITF": [
        ("MATCH_WINNER contract, level", "every stream; level from the series ticker", PRESERVED, ""),
        ("frozen decision probability gen2_dyn_hier_sr_v1+fair_v1 (with surface) at decision time", "shadow-board opportunities only",
         NOT_AVAILABLE, "the shadow board ran once, at 2026-09-12 17:13, eleven minutes BEFORE this freeze, and is scheduled in no workflow; "
                        "the ledger holds Gen-1; the dislocation scan computes fair_v1 with surface=None on the externally-listed subset only"),
        ("fee-adjusted edge at the executable ask", "would be derivable from the probability above", NOT_AVAILABLE, "no probability, no edge"),
        _SETTLE + ("",),
    ],
    "W3-2026-002-NONITF-POSITIVE-EDGE": [
        ("MATCH_WINNER contract, level != ITF", "every stream", PRESERVED, ""),
        ("frozen decision probability (fair_v1, with surface)", "shadow-board opportunities only", NOT_AVAILABLE, "as W3-2026-001"),
        ("selector_v1 qualification checklist", "shadow-board opportunities only", NOT_AVAILABLE,
         "twelve checks (staleness, spread, size, tail, data quality, ...) evaluated only by the shadow board"),
        ("Kalshi mid on the selected rows", "would come from the same rows", NOT_AVAILABLE, ""),
        _FB + ("",), _CLOSE + ("",), _SETTLE + ("",),
    ],
    "W4-2026-001-KALSHI-LONE-OUTLIER": [
        ("MATCH_WINNER, triangulation, external fair, external edge", "dislocation ledger (external_v1)", PRESERVED, ""),
        ("Kalshi bid/ask/spread/displayed size/quote age", "dislocation ledger", PRESERVED, ""),
        ("taker fee", "dislocation ledger kalshi_fee (quadratic taker at the ask)", PRESERVED, ""),
        ("external venue timestamp < 30 minutes", "external market store (venue source_timestamp per observation)", DERIVABLE,
         "joined on scan instant + source + de-vigged value; Smarkets publishes no venue timestamp, so a Smarkets "
         "contribution can never be VERIFIED fresh"),
        ("first qualifying observation per contract", "dislocation ledger order by generated_at", DERIVABLE, ""),
        _FB + ("",), _CLOSE + ("",), _SETTLE + ("",),
    ],
}


@dataclass
class HarvestResult:
    candidate_id: str
    kind: str
    evidence_rows: list = field(default_factory=list)       # EvidenceRow, rule-qualifying observations
    exclusions: list = field(default_factory=list)          # compact dicts for rows that failed the rule
    exclusion_counts: Counter = field(default_factory=Counter)
    universe: dict = field(default_factory=dict)
    metrics: dict = field(default_factory=dict)
    summary: ScoreSummary | None = None
    status: str = ""
    status_reason: str = ""
    notes: list = field(default_factory=list)

    def report(self) -> dict:
        return {"candidate_id": self.candidate_id, "kind": self.kind, "status": self.status,
                "status_reason": self.status_reason, "universe": self.universe, "metrics": self.metrics,
                "exclusion_counts": dict(self.exclusion_counts), "summary": self.summary.to_dict() if self.summary else None,
                "notes": self.notes, "field_audit": [dict(zip(("field", "source", "class", "note"), f))
                                                     for f in FIELD_AUDIT.get(self.candidate_id, [])],
                "harvester_version": HARVESTER_VERSION}


@dataclass
class Context:
    data_root: str
    candidates: dict
    truths: dict
    settlements: dict
    capture_root: str
    now: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    _quotes: dict | None = None
    _parsed: dict | None = None

    def quotes(self, tickers: set[str]) -> dict:
        from tennis_edge.ledger.quotes import quotes_from_capture
        if self._quotes is None:
            self._quotes = {}
        need = {t for t in tickers if t not in self._quotes}
        if need:
            got = quotes_from_capture(self.capture_root, need)
            for t in need:
                self._quotes[t] = got.get(t, [])
        return {t: self._quotes[t] for t in tickers}

    def parsed_markets(self) -> dict:
        """ticker -> (ParsedMarket, first captured record) from the capture's own market records."""
        if self._parsed is None:
            from tennis_edge.kalshi.markets import parse_market
            out = {}
            for _run, _ts, r in src.capture_quote_records(self.capture_root):
                t = r.get("ticker")
                if t and t not in out and r.get("rules_primary"):
                    out[t] = (parse_market(r), r)
            self._parsed = out
        return self._parsed


# ---------------------------------------------------------------------------------------------------
def _cand_fp(c: dict) -> str:
    return c.get("_fingerprint_recomputed") or c.get("fingerprint") or ""


def _level_of_ticker(ticker: str) -> tuple[str, str]:
    """(tour, level) from the series ticker, via the frozen taxonomy."""
    from tennis_edge.kalshi.families import SERIES
    fam = SERIES.get((ticker or "").split("-")[0])
    return (fam[1], fam[2]) if fam else ("UNKNOWN", "UNKNOWN")


def _timing(captured_at: str, match_id: str, truths: dict):
    t = truths.get(match_id)
    tc = classify(src.iso(captured_at), t)
    return t, tc


def _timing_reason(tc, truth) -> str | None:
    if tc.timing_class == STRICT_PREGAME:
        return None
    if tc.timing_class == POST_START:
        return ev.R_TIMING_POST
    if tc.timing_class == AMBIGUOUS:
        return ev.R_TIMING_AMBIG
    if truth is not None and truth.confidence == "C":
        return ev.R_TRUTH_C
    return ev.R_TIMING_UNKNOWN


def _strict_close(ctx: Context, ticker: str, truth, captured_at: str, bid, ask, size, tc):
    qs = ctx.quotes({ticker})[ticker]
    cc = canonical_close(qs, truth)
    entry = Quote(src.iso(captured_at), bid, ask, yes_ask_size=size)
    rec = clv_record(prediction_id="", ticker=ticker, match_id=truth.match_id if truth else "",
                     family="MATCH_WINNER", entry=entry, close=cc, truth=truth, timing=tc)
    return cc, rec


def _describe(rows: list) -> dict:
    """Sample description the report needs: dates, matches, days, tournaments, tour/level split."""
    if not rows:
        return {"n": 0}
    ts = sorted(r.captured_at for r in rows if r.captured_at)
    tl = Counter("/".join(_level_of_ticker(r.ticker)) for r in rows)
    return {"n": len(rows), "first": ts[0] if ts else None, "last": ts[-1] if ts else None,
            "physical_matches": len({r.physical_match_id for r in rows}),
            "calendar_days": len({t[:10] for t in ts}),
            "tournaments": len({(r.extra or {}).get("competition") for r in rows if (r.extra or {}).get("competition")}),
            "tour_level": dict(tl)}


# ---------------------------------------------------------------------------------------------------
# W4-2026-001-KALSHI-LONE-OUTLIER
#
# "MATCH_WINNER contracts where: a reference value exists from at least one admissible external group
#  whose venue timestamp is under 30 minutes old; triangulation is KALSHI_LONE_OUTLIER; external fair
#  minus the executable Kalshi ask minus the taker fee is >= 0.02; the Kalshi quote is two-sided, under an
#  hour old, inside a 6c spread and backed by at least one contract of displayed size. Measured on the
#  FIRST such observation of each contract; later observations of the same contract are follow-up, not
#  new evidence."
W4_MIN_EXTERNAL_EDGE = 0.02
W4_MAX_VENUE_AGE_S = 30 * 60
W4_MAX_KALSHI_AGE_S = 60 * 60
W4_MAX_SPREAD_CENTS = 6
W4_MIN_SIZE = 1.0
_EPS = 1e-9
#: consensus.py rule the external_v1 scan applied when it built the reference: an exchange midpoint from
#: a book wider than this is excluded. Needed to know WHICH groups contributed to a stored reference.
_EXCHANGE_SPREAD_CAP = 0.06


def w4_rule_gates(d: dict) -> dict:
    """The frozen W4 rule on one dislocation row's PRESERVED fields (freshness is checked separately)."""
    bid, ask, fee, ext = d.get("kalshi_bid"), d.get("kalshi_ask"), d.get("kalshi_fee"), d.get("external_fair")
    two_sided = bid is not None and ask is not None and 0 < bid <= ask < 1
    edge = (ext - ask - fee) if (ext is not None and two_sided and fee is not None) else None
    age = d.get("kalshi_quote_age_s")
    return {
        "family_match_winner": d.get("market_family") == "MATCH_WINNER",
        "reference_exists": ext is not None,
        "kalshi_lone_outlier": d.get("triangulation") == "KALSHI_LONE_OUTLIER",
        "external_edge_ge_2c": edge is not None and edge >= W4_MIN_EXTERNAL_EDGE - _EPS,
        "kalshi_two_sided": bool(two_sided),
        "kalshi_quote_under_1h": age is not None and age < W4_MAX_KALSHI_AGE_S,
        "spread_within_6c": bool(two_sided) and round((ask - bid) * 100) <= W4_MAX_SPREAD_CENTS,
        "displayed_size_ge_1": d.get("kalshi_size") is not None and d["kalshi_size"] >= W4_MIN_SIZE,
    }


def w4_freshness(d: dict, ext_obs: dict) -> tuple[str, dict]:
    """VERIFIED_FRESH | UNVERIFIABLE | MIXED | UNRESOLVED, plus venue ages, for the stored reference.

    Rebuilds which venue observations stood behind the stored `external_fair` from the immutable external
    store (same scan instant, same venue, same de-vigged value) and asks whether each CONTRIBUTING venue
    published a timestamp under 30 minutes old. A venue that publishes no timestamp cannot satisfy "whose
    venue timestamp is under 30 minutes old"; it is not treated as fresh, and it is not treated as stale."""
    at = d.get("generated_at")
    contributing, ages = [], {}
    for source, p in (d.get("external_prices") or {}).items():
        if p is None:
            continue
        cands = [o for o in ext_obs.get((at, source), []) if o.get("devigged_probability") == p]
        if not cands:
            return "UNRESOLVED", {"missing_observation": source}
        o = cands[0]
        if o.get("source_kind") in ("EXCHANGE", "PREDICTION_MARKET") and o.get("source_margin") is not None \
                and o["source_margin"] > _EXCHANGE_SPREAD_CAP:
            continue                                       # excluded from the reference at scan time
        st = o.get("source_timestamp")
        age = None
        if st:
            age = (src.iso(o["observed_at"]) - src.iso(st)).total_seconds()
            if age > 1800.0:
                continue                                   # the scan excluded it as stale too
        contributing.append((source, age, p))
        ages[source] = age
    if not contributing:
        return "UNRESOLVED", ages
    vals = sorted(p for _s, _a, p in contributing)
    ref = median(vals)
    if d.get("external_fair") is None or abs(ref - d["external_fair"]) > 1e-12:
        return "UNRESOLVED", {**ages, "rebuilt_reference": ref}
    verified = [a is not None and a < W4_MAX_VENUE_AGE_S for _s, a, _p in contributing]
    if all(verified):
        return "VERIFIED_FRESH", ages
    if not any(verified):
        return "UNVERIFIABLE", ages
    return "MIXED", ages


def harvest_w4(ctx: Context, cand: dict) -> HarvestResult:
    cid = cand["candidate_id"]
    res = HarvestResult(cid, KIND_TRADE)
    cs = cand["confirmation_start"]
    root = os.path.join(ctx.data_root, "research", "external", "dislocations")
    all_rows = list(src.iter_jsonl(os.path.join(root, "*.jsonl")))
    pre = [r for _f, _h, r in all_rows if (r.get("generated_at") or "") < cs]
    post = [(f, h, r) for f, h, r in all_rows if (r.get("generated_at") or "") >= cs]
    res.exclusion_counts[ev.R_PRE_FREEZE] = len(pre)
    res.universe = {"stream": "research/external/dislocations (external_v1)", "rows_total": len(all_rows),
                    "rows_before_confirmation_start": len(pre), "rows_after": len(post)}

    gate_pass, gate_fail = [], Counter()
    for f, h, r in post:
        g = w4_rule_gates(r)
        failed = [k for k, v in g.items() if not v]
        if failed:
            for k in failed:
                gate_fail[k] += 1
            res.exclusions.append({"observation_id": r.get("row_hash") or h, "captured_at": r.get("generated_at"),
                                   "ticker": r.get("kalshi_ticker"), "reasons": [ev.R_RULE_FAILED] + failed})
            res.exclusion_counts[ev.R_RULE_FAILED] += 1
        else:
            gate_pass.append((f, h, r))
    res.universe["failed_gate_counts"] = dict(gate_fail)

    ext_obs = src.external_match_winner_obs(os.path.join(ctx.data_root, "research", "external", "market"),
                                            {r["generated_at"] for _f, _h, r in gate_pass})
    qualifying, fresh_counts = [], Counter()
    for f, h, r in gate_pass:
        fr, ages = w4_freshness(r, ext_obs)
        fresh_counts[fr] += 1
        if fr == "VERIFIED_FRESH":
            qualifying.append((f, h, r, fr, ages))
            continue
        reason = {"UNVERIFIABLE": ev.R_FRESHNESS_UNVERIFIED, "MIXED": ev.R_FRESHNESS_MIXED}.get(fr, ev.R_FRESHNESS_MIXED)
        res.exclusions.append({"observation_id": r.get("row_hash") or h, "captured_at": r.get("generated_at"),
                               "ticker": r.get("kalshi_ticker"), "reasons": [reason, f"freshness={fr}"],
                               "venue_ages_s": ages, "external_sources": r.get("external_sources")})
        res.exclusion_counts[reason] += 1
    res.universe["freshness_of_gate_passing_rows"] = dict(fresh_counts)
    # the scanner's own SHADOW_BET flag, reported so the literal reading can be compared with it
    res.universe["scanner_shadow_bet_rows"] = sum(1 for _f, _h, r in post if r.get("decision") == "SHADOW_BET")
    res.universe["rule_gates_pass_rows"] = len(gate_pass)
    res.universe["rule_and_freshness_pass_rows"] = len(qualifying)

    qualifying.sort(key=lambda x: (x[2]["generated_at"], x[2]["kalshi_ticker"]))
    seen = set()
    parsed = ctx.parsed_markets()
    rows = []
    for f, h, r, fr, ages in qualifying:
        tk = r["kalshi_ticker"]
        first = tk not in seen
        seen.add(tk)
        truth, tc = _timing(r["generated_at"], r["kalshi_event"], ctx.truths)
        reasons = []
        if not first:
            reasons.append(ev.R_REOBSERVATION)
        else:
            tr = _timing_reason(tc, truth)
            if tr:
                reasons.append(tr)
        cc, clv = _strict_close(ctx, tk, truth, r["generated_at"], r["kalshi_bid"], r["kalshi_ask"],
                                r.get("kalshi_size"), tc)
        sres, payout, sat = src.settlement_payout(ctx.settlements.get(tk))
        pnl = None if payout is None else payout - r["kalshi_ask"] - r["kalshi_fee"]
        pm = parsed.get(tk)
        srec = ctx.settlements.get(tk) or {}
        rows.append(ev.EvidenceRow(
            candidate_id=cid, observation_id=r.get("row_hash") or h, physical_match_id=r.get("physical_match_id"),
            ticker=tk, market_family=r.get("market_family"), side=r.get("side"),
            captured_at=r["generated_at"], candidate_freeze_at=cand["frozen_at"], confirmation_start=cs,
            candidate_fingerprint=_cand_fp(cand), model_version=r.get("selector_version"),
            fair_probability=r.get("external_fair"), model_probability=r.get("model_fair"),
            kalshi_bid=r["kalshi_bid"], kalshi_ask=r["kalshi_ask"], kalshi_mid=r.get("kalshi_mid"),
            kalshi_spread=r.get("kalshi_spread"), fee=r["kalshi_fee"], displayed_size=r.get("kalshi_size"),
            kalshi_quote_age_s=r.get("kalshi_quote_age_s"), external_reference=r.get("external_fair"),
            external_sources=tuple(r.get("external_sources") or ()), external_venue_ages_s=ages,
            external_freshness=fr, triangulation=r.get("triangulation"), decision_edge=r.get("external_edge"),
            extra={"kalshi_event": r.get("kalshi_event"), "scanner_decision": r.get("decision"),
                   "first_qualifying": first, "competition": pm[0].competition if pm else None,
                   "tour_level": "/".join(_level_of_ticker(tk))},
            first_ball_confidence=truth.confidence if truth else None,
            first_ball_lower_utc=truth.lower_bound_utc.isoformat() if (truth and truth.lower_bound_utc) else None,
            timing_class=tc.timing_class,
            strict_close_ts=clv.close_ts.isoformat() if clv.close_ts else None,
            strict_close_bid=clv.close_yes_bid, strict_close_ask=clv.close_yes_ask, close_basis=cc.close_basis,
            strict_clv_executable=clv.clv_executable if clv.strict else None,
            strict_clv_midpoint=clv.clv_midpoint if clv.strict else None,
            settlement_result=sres, settlement_value=payout, settled_at=sat, after_fee_pnl=pnl,
            inclusion_result=ev.EXCLUDED if reasons else ev.INCLUDED, exclusion_reasons=tuple(reasons),
            source_hashes={"dislocation_row_hash": r.get("row_hash"), "dislocation_file": os.path.basename(f),
                           "settlement_line": srec.get("_line_hash"),
                           "first_ball_truth": truth.evidence_payload_hash if truth else None,
                           "close_quote": (clv.close_ts.isoformat() + f"|{clv.close_yes_bid}|{clv.close_yes_ask}") if clv.close_ts else None},
            harvester_version=HARVESTER_VERSION))
        for x in reasons:
            res.exclusion_counts[x] += 1
    res.evidence_rows = rows

    firsts = [r for r in rows if r.extra.get("first_qualifying")]
    elig = [r for r in rows if r.inclusion_result == ev.INCLUDED]
    res.universe["first_qualifying_observations"] = len(firsts)
    res.universe["reobservations_removed"] = sum(1 for r in rows if not r.extra.get("first_qualifying"))
    res.universe["first_qualifying_by_timing"] = dict(Counter(r.timing_class for r in firsts))
    res.universe["first_qualifying_sample"] = _describe(firsts)
    res.universe["eligible_sample"] = _describe(elig)

    settled = [r for r in elig if r.settlement_value is not None]
    binary = [r for r in settled if r.settlement_result in ("yes", "no")]
    strict = [r for r in elig if r.strict_clv_executable is not None]
    y = [1.0 if r.settlement_result == "yes" else 0.0 for r in binary]
    b_ext = stats.brier_terms([r.external_reference for r in binary], y)
    b_mid = stats.brier_terms([r.kalshi_mid for r in binary], y)
    acc = stats.paired_ci(b_ext, b_mid)
    clv = stats.mean_ci([r.strict_clv_executable for r in strict])
    pnl = stats.mean_ci([r.after_fee_pnl for r in settled])
    res.metrics = {
        "eligible_n": len(elig), "settled_n": len(settled), "binary_settled_n": len(binary),
        "strict_clv_n": len(strict), "unresolved_n": len(elig) - len(settled),
        "brier_external_reference": (sum(b_ext) / len(b_ext)) if b_ext else None,
        "brier_kalshi_mid": (sum(b_mid) / len(b_mid)) if b_mid else None,
        "brier_diff_external_minus_mid": acc,
        "strict_executable_clv": clv,
        "strict_midpoint_clv": stats.mean_ci([r.strict_clv_midpoint for r in strict]),
        "after_fee_pnl_per_contract": pnl,
        "conditions": {
            "accuracy": "external Brier beats Kalshi mid with a 95% CI excluding zero (paired diff < 0)",
            "clv": "mean strict executable CLV > 0, CI excluding zero, A/B truth only",
            "economics": "realised after-fee P&L per contract > 0, CI excluding zero",
        },
    }
    res.summary = ScoreSummary(
        kind=KIND_TRADE, minimum_n=int(cand["minimum_n"]), eligible_n=len(elig), settled_n=len(settled),
        strict_clv_n=len(strict), unsettled_n=len(elig) - len(settled),
        clv_pending_n=sum(1 for r in elig if r.strict_clv_executable is None and r.settlement_value is None),
        accuracy_pass=(acc["mean"] is not None and acc["excludes_zero"] is True and acc["mean"] < 0) if binary else None,
        clv_pass=(clv["mean"] is not None and clv["excludes_zero"] is True and clv["mean"] > 0) if strict else None,
        economics_pass=(pnl["mean"] is not None and pnl["excludes_zero"] is True and pnl["mean"] > 0) if settled else None,
        clv_required=True)
    res.status, res.status_reason = assign_status(res.summary)
    return res


# ---------------------------------------------------------------------------------------------------
# EC-2026-004-COHERENCE-EXECUTABLE (DISCOVERY_ONLY)
#
# "Any structure detected by tennis_edge.pricing.coherence on executable bid/ask with order-book depth on
#  every leg and an executable margin > 0 after Kalshi taker fees." After-fee condition: "executable
#  margin > 0 after taker fees on every leg, with the minimum leg size >= 10 contracts".
EC4_MIN_LEG_SIZE = 10.0


def harvest_ec4(ctx: Context, cand: dict) -> HarvestResult:
    from tennis_edge.pricing.coherence import Contract, scan_match
    from tennis_edge.ledger.quotes import book_top
    cid = cand["candidate_id"]
    res = HarvestResult(cid, KIND_EXISTENCE)
    cs = cand["confirmation_start"]
    parsed = ctx.parsed_markets()
    by_run: dict = defaultdict(list)
    n_books = n_pre = n_unparsed = n_onesided = 0
    for f, h, r in src.iter_jsonl(os.path.join(ctx.capture_root, "*", "*.books.jsonl.gz")):
        n_books += 1
        if (r.get("captured_at") or "") < cs:
            n_pre += 1
            continue
        pm = parsed.get(r.get("ticker"))
        if pm is None or pm[0].status != "PARSED" or pm[0].scope != "MATCH":
            n_unparsed += 1
            continue
        top = book_top(r)
        if top is None:
            n_onesided += 1
            continue
        by_run[r.get("run_id")].append((pm[0], top, r.get("captured_at"), h))
    structures: dict = {}
    price_only = Counter()
    n_match_passes = 0
    for run in sorted(by_run):
        groups = defaultdict(list)
        for pm, top, ts, h in by_run[run]:
            sfx = pm.event_ticker.split("-", 1)[1] if "-" in pm.event_ticker else pm.event_ticker
            groups[sfx].append((pm, top, ts, h))
        for sfx, items in groups.items():
            n_match_passes += 1
            ts = max(x[2] for x in items)
            for mode in ("price_only", "size_verified"):
                cs_ = []
                for pm, (yb, ybs, nb, nbs), _ts, _h in items:
                    cs_.append(Contract(ticker=pm.ticker, family=pm.family, yes_bid=yb, yes_ask=round(1.0 - nb, 6),
                                        yes_bid_size=1.0 if mode == "price_only" else ybs,
                                        yes_ask_size=1.0 if mode == "price_only" else nbs,
                                        line=pm.line, subject_is_a=pm.subject_is_a, set_index=pm.set_index,
                                        exact_score=("-".join(str(x) for x in pm.exact_score) if pm.exact_score else None),
                                        ts=ts, fee_type="quadratic"))
                if len(cs_) < 2:
                    continue
                for o in scan_match(cs_, sfx, ts=ts):
                    if mode == "price_only":
                        price_only[o.kind] += 1
                        continue
                    key = (o.kind, sfx, tuple(sorted(l["ticker"] for l in o.legs)))
                    qual = o.size >= EC4_MIN_LEG_SIZE and o.executable_margin > 0
                    s = structures.get(key)
                    if s is None:
                        structures[key] = {"first": o, "first_run": run, "first_ts": ts, "last_ts": ts, "passes": 1,
                                           "qualifying_passes": int(qual), "max_margin": o.executable_margin,
                                           "max_size": o.size, "qualifying_first_ts": ts if qual else None}
                    else:
                        s["last_ts"] = ts
                        s["passes"] += 1
                        s["qualifying_passes"] += int(qual)
                        s["max_margin"] = max(s["max_margin"], o.executable_margin)
                        s["max_size"] = max(s["max_size"], o.size)
                        if qual and s["qualifying_first_ts"] is None:
                            s["qualifying_first_ts"] = ts
    rows = []
    for key, s in structures.items():
        o = s["first"]
        qual = s["qualifying_passes"] > 0
        dur = (src.iso(s["last_ts"]) - src.iso(s["first_ts"])).total_seconds()
        reasons = () if qual else (ev.R_RULE_FAILED, f"min leg size {s['max_size']:.0f} < {EC4_MIN_LEG_SIZE:.0f} on every pass")
        rows.append(ev.EvidenceRow(
            candidate_id=cid, observation_id=ev.canonical_hash(list(key) + [s["first_run"]]),
            physical_match_id=key[1], ticker="|".join(key[2]), market_family=o.family, side=None,
            captured_at=s["first_ts"], candidate_freeze_at=cand["frozen_at"], confirmation_start=cs,
            candidate_fingerprint=_cand_fp(cand), model_version="coherence_v1",
            fee=o.fees_per_set, displayed_size=o.size, decision_edge=o.executable_margin,
            extra={"kind": o.kind, "legs": o.legs, "capital_per_set": o.capital_per_set,
                   "worst_case_payoff": o.worst_case_payoff, "theoretical_margin": o.theoretical_margin,
                   "executable_margin_first": o.executable_margin, "max_executable_margin": s["max_margin"],
                   "max_size": s["max_size"], "passes_seen": s["passes"], "qualifying_passes": s["qualifying_passes"],
                   "duration_s": dur, "total_executable_profit_first": o.total_executable_profit},
            inclusion_result=ev.INCLUDED if qual else ev.EXCLUDED, exclusion_reasons=reasons,
            source_hashes={"first_capture_run": s["first_run"]}, harvester_version=HARVESTER_VERSION))
    res.evidence_rows = rows
    qual_rows = [r for r in rows if r.inclusion_result == ev.INCLUDED]
    res.universe = {"stream": "kalshi/capture/*/books (order books, orderbook_fp)", "books_read": n_books,
                    "books_before_confirmation_start": n_pre, "books_unparsed_or_not_match_scope": n_unparsed,
                    "books_one_sided": n_onesided, "capture_runs_scanned": len(by_run),
                    "match_passes_scanned": n_match_passes,
                    "note": "books are captured only for match-scope markets within 6h of their nominal start "
                            "(budget 400 per pass), so the scan sees the near-start board, not every listing"}
    res.exclusion_counts[ev.R_PRE_FREEZE] = n_pre
    res.metrics = {
        "price_only_violations_by_kind": dict(price_only),
        "size_verified_positive_margin_structures": len(rows),
        "qualifying_structures (margin>0 after fees, min leg >= 10)": len(qual_rows),
        "qualifying": [{"kind": r.extra["kind"], "family": r.market_family, "match": r.physical_match_id,
                        "first_seen": r.captured_at, "duration_s": r.extra["duration_s"],
                        "capital_per_set": r.extra["capital_per_set"], "worst_case_payoff": r.extra["worst_case_payoff"],
                        "max_executable_margin": r.extra["max_executable_margin"], "max_size": r.extra["max_size"]}
                       for r in qual_rows],
        "sub_threshold": [{"kind": r.extra["kind"], "family": r.market_family, "match": r.physical_match_id,
                           "first_seen": r.captured_at, "max_executable_margin": r.extra["max_executable_margin"],
                           "max_size": r.extra["max_size"], "duration_s": r.extra["duration_s"]}
                          for r in rows if r.inclusion_result != ev.INCLUDED],
    }
    res.summary = ScoreSummary(kind=KIND_EXISTENCE, minimum_n=int(cand["minimum_n"]), eligible_n=len(qual_rows))
    res.status, res.status_reason = assign_status(res.summary)
    res.notes.append("DISCOVERY_ONLY: a qualifying structure is an existence observation, never a betting candidate.")
    return res


# ---------------------------------------------------------------------------------------------------
# Candidates whose decision-time inputs were never preserved after their freeze.
def _count_ledger(ctx: Context, since: str, families: set[str], singles_tours=("ATP", "WTA")) -> dict:
    root = os.path.join(ctx.data_root, "research", "ledger")
    n = 0
    mv = Counter()
    tickers, matches = set(), set()
    for _f, h, r in src.iter_jsonl(os.path.join(root, "*.jsonl")):
        if r.get("generated_at_utc", "") < since or r.get("family") not in families:
            continue
        if r.get("tour") not in singles_tours or r.get("model_version", "").startswith("doubles"):
            continue
        n += 1
        mv[r.get("model_version")] += 1
        tickers.add(r["ticker"])
        matches.add(r["match_id"].split("-", 1)[-1])
    return {"rows": n, "model_versions": dict(mv), "tickers": len(tickers), "matches": len(matches)}


def _count_opportunities(ctx: Context, since: str) -> dict:
    root = os.path.join(ctx.data_root, "research", "opportunities")
    allr = [r for _f, _h, r in src.iter_jsonl(os.path.join(root, "*.jsonl"))]
    post = [r for r in allr if r.get("generated_at", "") >= since]
    ts = sorted(r.get("generated_at", "") for r in allr)
    return {"rows_total": len(allr), "rows_after_confirmation_start": len(post),
            "first": ts[0] if ts else None, "last": ts[-1] if ts else None,
            "model_versions": dict(Counter(r.get("model_version") for r in allr))}


def _count_dislocations(ctx: Context, since: str) -> dict:
    root = os.path.join(ctx.data_root, "research", "external", "dislocations")
    n = 0
    tk = set()
    for _f, _h, r in src.iter_jsonl(os.path.join(root, "*.jsonl")):
        if r.get("generated_at", "") >= since:
            n += 1
            tk.add(r.get("kalshi_ticker"))
    return {"rows": n, "contracts": len(tk)}


def _listed(ctx: Context, since: str, families: set[str]) -> dict:
    """Contracts Kalshi ACTUALLY listed after `since`, from the capture's own market records."""
    parsed = ctx.parsed_markets()
    tk, matches, fam = set(), set(), Counter()
    first_seen = {}
    for _run, ts, r in src.capture_quote_records(ctx.capture_root, since):
        t = r.get("ticker")
        pm = parsed.get(t)
        if pm is None or pm[0].family not in families:
            continue
        if t not in tk:
            fam[pm[0].family] += 1
        tk.add(t)
        matches.add(pm[0].event_ticker.split("-", 1)[-1])
        first_seen.setdefault(t, ts)
    settled = {t for t in tk if t in ctx.settlements}
    return {"contracts_listed": len(tk), "physical_matches": len(matches), "by_family": dict(fam),
            "contracts_settled": len(settled)}


def _unscorable(cid: str, kind: str, cand: dict, universe: dict, unscorable_n: int, missing: list[str],
                notes: list[str]) -> HarvestResult:
    res = HarvestResult(cid, kind)
    res.universe = universe
    res.exclusion_counts[ev.R_MISSING_FIELD] = unscorable_n
    res.metrics = {"eligible_n": 0, "settled_n": 0, "strict_clv_n": 0, "missing_fields": missing,
                   "note": "no metric is computed: the probability the frozen rule decides on was not preserved "
                           "at capture time, and reconstructing it now would be synthesising historical state"}
    res.summary = ScoreSummary(kind=kind, minimum_n=int(cand["minimum_n"]), eligible_n=0,
                               unscorable_n=unscorable_n, clv_required=kind == KIND_TRADE)
    res.status, res.status_reason = assign_status(res.summary)
    res.notes = notes
    return res


def harvest_ec1(ctx: Context, cand: dict) -> HarvestResult:
    cs = cand["confirmation_start"]
    listed = _listed(ctx, cs, {"EXACT_SET_SCORE"})
    led = _count_ledger(ctx, cs, {"EXACT_SET_SCORE"})
    uni = {"kalshi_listed_after_freeze": listed, "ledger_rows_after_freeze (Gen-1 DP lane)": led,
           "stream_needed": "a prospective market_conditioned_v1 + fundamental exact-score distribution per listed match"}
    return _unscorable(cand["candidate_id"], KIND_PRICING, cand, uni, listed["contracts_listed"],
                       [f[0] for f in FIELD_AUDIT[cand["candidate_id"]] if f[2] == NOT_AVAILABLE],
                       [f"Kalshi listed {listed['contracts_listed']} exact-score contracts on "
                        f"{listed['physical_matches']} physical matches after the freeze. Exact-score log loss is "
                        f"scored per match, so even with both lanes preserved the candidate could not have reached "
                        f"its minimum of {cand['minimum_n']}" if listed["physical_matches"] < int(cand["minimum_n"]) else
                        "listing volume alone would not have blocked scoring",
                        "The unscorable count is the listed contracts; the ledger rows for the same family are "
                        "Gen-1 DP prices and are reported separately, not added in."])


def harvest_ec2(ctx: Context, cand: dict) -> HarvestResult:
    cs = cand["confirmation_start"]
    listed = _listed(ctx, cs, {"GAME_SPREAD", "TOTAL_GAMES"})
    led = _count_ledger(ctx, cs, {"GAME_SPREAD", "TOTAL_GAMES"})
    uni = {"kalshi_listed_after_freeze": listed, "ledger_rows_after_freeze (Gen-1 DP lane)": led}
    return _unscorable(cand["candidate_id"], KIND_PRICING, cand, uni, listed["contracts_listed"],
                       [f[0] for f in FIELD_AUDIT[cand["candidate_id"]] if f[2] == NOT_AVAILABLE],
                       [f"Kalshi listed {listed['contracts_listed']} spread/total contracts on "
                        f"{listed['physical_matches']} physical matches after the freeze; no games-level sports "
                        "truth exists to compute a game-differential MAE even for those, and the metric is scored "
                        f"per match, so {listed['physical_matches']} matches could not reach {cand['minimum_n']}"
                        if listed["physical_matches"] < int(cand["minimum_n"]) else
                        f"Kalshi listed {listed['contracts_listed']} spread/total contracts on "
                        f"{listed['physical_matches']} physical matches after the freeze; no games-level sports "
                        "truth exists to compute a game-differential MAE even for those",
                        "The unscorable count is the listed contracts; ledger rows are reported separately."])


def harvest_ec3(ctx: Context, cand: dict) -> HarvestResult:
    cs = cand["confirmation_start"]
    led = _count_ledger(ctx, cs, {"MATCH_WINNER"})
    opp = _count_opportunities(ctx, cs)
    dis = _count_dislocations(ctx, cs)
    uni = {"ledger (Gen-1 only)": led, "shadow-board opportunities (Gen-2, no Gen-1 on the row)": opp,
           "dislocations (Gen-2 blend without surface, no serve points, no Gen-1)": dis}
    n = led["rows"] + opp["rows_after_confirmation_start"] + dis["rows"]
    return _unscorable(cand["candidate_id"], KIND_TRADE, cand, uni, n,
                       [f[0] for f in FIELD_AUDIT[cand["candidate_id"]] if f[2] in (NOT_AVAILABLE, AMBIGUOUS_FIELD)],
                       ["No single preserved row carries a Gen-2 probability, a Gen-1 Elo probability and the "
                        "thinner player's Gen-2 serve points for the same decision. Joining rows from different "
                        "streams, instants and rating artifacts would construct a comparison nobody made.",
                        f"The only rows with Gen-2 serve evidence are one shadow-board run ({opp['rows_after_confirmation_start']} "
                        f"rows, both sides of each contract, one afternoon); even paired generously they could not "
                        f"reach the frozen minimum of {cand['minimum_n']}."])


def harvest_w3(ctx: Context, cand: dict) -> HarvestResult:
    cs = cand["confirmation_start"]
    led = _count_ledger(ctx, cs, {"MATCH_WINNER"})
    opp = _count_opportunities(ctx, cs)
    dis = _count_dislocations(ctx, cs)
    uni = {"shadow-board opportunities (the frozen lane)": opp, "ledger (Gen-1 lane, not the frozen model)": led,
           "dislocations (fair_v1 WITHOUT surface, externally listed subset only)": dis}
    n = led["rows"] + dis["rows"] + opp["rows_after_confirmation_start"]
    kind = KIND_ABSTENTION if cand["candidate_id"].startswith("W3-2026-001") else KIND_TRADE
    return _unscorable(cand["candidate_id"], kind, cand, uni, n,
                       [f[0] for f in FIELD_AUDIT[cand["candidate_id"]] if f[2] == NOT_AVAILABLE],
                       [f"The frozen decision probability is produced only by scripts/ops/shadow_board.py, which "
                        f"last ran at {opp['last']} -- before this candidate's freeze at {cand['frozen_at']} -- and "
                        "is not scheduled by any workflow. After the freeze it was never computed.",
                        "The dislocation scan's model_fair is fair_v1's Gen-2 blend computed with surface=None on "
                        "only the matches an external venue also lists; it is a different number from a different "
                        "population, so using it would be substituting a proxy for the frozen rule."])


HARVESTERS = {
    "EC-2026-001-MKTCOND-EXACT-SCORE": harvest_ec1,
    "EC-2026-002-MKTCOND-GAME-SPREAD": harvest_ec2,
    "EC-2026-003-GEN2-MODERATE-EVIDENCE": harvest_ec3,
    "EC-2026-004-COHERENCE-EXECUTABLE": harvest_ec4,
    "W3-2026-001-ABSTAIN-ITF": harvest_w3,
    "W3-2026-002-NONITF-POSITIVE-EDGE": harvest_w3,
    "W4-2026-001-KALSHI-LONE-OUTLIER": harvest_w4,
}


def write_exclusions(path: str, rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt") as f:
        for r in rows:
            f.write(json.dumps(r, separators=(",", ":"), default=str) + "\n")
