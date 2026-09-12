#!/usr/bin/env python3
"""Scan the captured Kalshi tennis board for cross-market coherence violations.

Two questions, deliberately answered separately, because conflating them is how a research project talks
itself into an edge that does not exist:

  HOW MANY INCONSISTENCIES?   Price-only scan. Every contract is given a nominal one-contract size, so a
                              violation is reported whenever the executable BID/ASK prices break a
                              relationship, whether or not anyone could have traded it.
  HOW MANY WERE EXECUTABLE?   Size-verified scan. Sizes come from the captured order books, so a
                              violation only counts if there was depth on every leg. Fees are charged on
                              every leg in both scans.

Persistence is measured by re-running the scan on every capture pass and tracking how long the same
structure keeps violating.
"""
from __future__ import annotations

import argparse
import glob
import gzip
import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.kalshi.markets import parse_market                    # noqa: E402
from tennis_edge.pricing.coherence import Contract, scan_match         # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _f(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if 0.0 < v < 1.0 else None


def latest_discovery(root=None):
    runs = sorted(glob.glob(os.path.join(root or os.path.join(PROJ, "data", "kalshi", "discovery"), "*", "summary.json")))
    return os.path.dirname(runs[-1]) if runs else None


def parsed_universe(disc: str) -> dict:
    out = {}
    for p in glob.glob(os.path.join(disc, "markets", "*.json")):
        blocks = json.load(open(p))
        for state in ("open", "closed", "settled", "unopened"):
            for m in (blocks.get(state) or {}).get("markets") or []:
                pm = parse_market(m)
                if pm.status == "PARSED" and pm.scope == "MATCH":
                    out[pm.ticker] = pm
    return out


def book_sizes(capture_root: str) -> dict:
    """(run_id, ticker) -> (yes_bid_size, yes_ask_size) from the captured order books."""
    sizes = {}
    for f in sorted(glob.glob(os.path.join(capture_root, "*", "*.books.jsonl.gz"))):
        with gzip.open(f, "rt") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                ob = ((r.get("orderbook") or {}).get("orderbook") or r.get("orderbook") or {})
                if not isinstance(ob, dict):
                    continue

                def top(levels):
                    best = None
                    for lv in levels or []:
                        try:
                            p, s = float(lv[0]), float(lv[1])
                        except (TypeError, ValueError, IndexError):
                            continue
                        if best is None or p > best[0]:
                            best = (p, s)
                    return best
                ty, tn = top(ob.get("yes")), top(ob.get("no"))
                if ty and tn:
                    sizes[(r.get("run_id"), r.get("ticker"))] = (ty[1], tn[1])
    return sizes


def passes(capture_root: str, carry_forward: bool = True):
    """run_id -> the LIVE board at that pass, in chronological order.

    The capture writes only markets whose quote CHANGED since the previous pass (with a periodic full
    snapshot), so a pass file is a delta, not a board. Scanning deltas makes every match look like it has
    two contracts and finds nothing. Carrying the last known quote forward reconstructs what was actually
    quotable at that moment, which is the thing a coherence scan has to look at.
    """
    running: dict = {}
    out = {}
    for f in sorted(glob.glob(os.path.join(capture_root, "*", "*.quotes.jsonl.gz"))):
        run = None
        with gzip.open(f, "rt") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                if not r.get("ticker"):
                    continue
                run = r.get("run_id") or run
                running[r["ticker"]] = r
        if run:
            out[run] = dict(running) if carry_forward else {k: v for k, v in running.items()
                                                            if v.get("run_id") == run}
    return dict(sorted(out.items()))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--discovery", default="")
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"))
    ap.add_argument("--out", default=os.path.join(PROJ, "research", "coherence"))
    a = ap.parse_args()

    disc = a.discovery or latest_discovery()
    if not disc:
        print("::warning::no discovery snapshot"); return 0
    universe = parsed_universe(disc)
    sizes = book_sizes(a.capture)
    all_passes = passes(a.capture)
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    os.makedirs(a.out, exist_ok=True)

    stats = {"run_id": run_id, "discovery": os.path.basename(disc), "passes": len(all_passes),
             "parsed_match_markets": len(universe), "book_quotes": len(sizes),
             "price_only": defaultdict(int), "executable": defaultdict(int),
             "quotes_seen": 0, "matches_scanned": 0, "contracts_scanned": 0}
    found, seen_keys = [], {}

    for run, quotes in all_passes.items():
        by_match = defaultdict(list)
        for tk, q in quotes.items():
            pm = universe.get(tk)
            if pm is None:
                continue
            yb, ya = _f(q.get("yes_bid_dollars")), _f(q.get("yes_ask_dollars"))
            if yb is None or ya is None:
                continue
            stats["quotes_seen"] += 1
            bs, as_ = sizes.get((run, tk), (None, None))
            suffix = pm.event_ticker.split("-", 1)[1] if "-" in pm.event_ticker else pm.event_ticker
            by_match[suffix].append((pm, q, yb, ya, bs, as_))
        for suffix, rows in by_match.items():
            stats["matches_scanned"] += 1
            stats["contracts_scanned"] += len(rows)
            ts = max(r[1].get("captured_at", "") for r in rows)
            for mode, nominal in (("price_only", 1.0), ("executable", None)):
                cs = []
                for pm, q, yb, ya, bs, as_ in rows:
                    bsz = nominal if nominal is not None else bs
                    asz = nominal if nominal is not None else as_
                    if bsz is None or asz is None:
                        continue
                    cs.append(Contract(ticker=pm.ticker, family=pm.family, yes_bid=yb, yes_ask=ya,
                                       yes_bid_size=bsz, yes_ask_size=asz, line=pm.line,
                                       subject_is_a=pm.subject_is_a,
                                       exact_score=("-".join(str(x) for x in pm.exact_score)
                                                    if pm.exact_score else None),
                                       ts=ts, fee_type=q.get("fee_type") or "quadratic"))
                if len(cs) < 2:
                    continue
                for o in scan_match(cs, suffix, ts=ts):
                    stats[mode][o.kind] += 1
                    key = (mode, o.kind, suffix, tuple(sorted(l["ticker"] for l in o.legs)))
                    d = o.to_dict()
                    d.update(mode=mode, capture_run=run, match_suffix=suffix)
                    if key in seen_keys:
                        prev = seen_keys[key]
                        prev["last_seen"] = ts
                        prev["passes_seen"] += 1
                        prev["duration_s"] = (datetime.fromisoformat(ts) -
                                              datetime.fromisoformat(prev["first_seen"])).total_seconds()
                    else:
                        d["first_seen"] = ts; d["last_seen"] = ts; d["passes_seen"] = 1; d["duration_s"] = 0.0
                        seen_keys[key] = d
                        found.append(d)

    # A null result is only informative with the board's shape attached: how wide the two-sided market
    # actually is, and how much of a derivative board there is to be incoherent about in the first place.
    import statistics as _st
    last_run = list(all_passes)[-1] if all_passes else None
    fam_counts, pair_sums, group_sizes = defaultdict(int), [], defaultdict(int)
    if last_run:
        bym = defaultdict(list)
        for tk, q in all_passes[last_run].items():
            pm = universe.get(tk)
            yb, ya = _f(q.get("yes_bid_dollars")), _f(q.get("yes_ask_dollars"))
            if pm is None or yb is None or ya is None:
                continue
            fam_counts[pm.family] += 1
            sfx = pm.event_ticker.split("-", 1)[1] if "-" in pm.event_ticker else pm.event_ticker
            bym[sfx].append((pm, yb, ya))
        for sfx, rows in bym.items():
            group_sizes[len(rows)] += 1
            mw = [r for r in rows if r[0].family == "MATCH_WINNER" and r[0].subject_is_a is not None]
            if len({r[0].subject_is_a for r in mw}) == 2:
                side_a = next(r for r in mw if r[0].subject_is_a)
                side_b = next(r for r in mw if not r[0].subject_is_a)
                pair_sums.append((side_a[2] + side_b[2], side_a[1] + side_b[1]))
    stats["board_shape"] = {
        "open_quotes_by_family": dict(sorted(fam_counts.items(), key=lambda kv: -kv[1])),
        "contracts_per_match": {str(k): v for k, v in sorted(group_sizes.items())},
        "two_sided_match_winner_pairs": len(pair_sums),
        "ask_sum_median": round(_st.median([s[0] for s in pair_sums]), 4) if pair_sums else None,
        "ask_sum_min": round(min([s[0] for s in pair_sums]), 4) if pair_sums else None,
        "bid_sum_median": round(_st.median([s[1] for s in pair_sums]), 4) if pair_sums else None,
        "bid_sum_max": round(max([s[1] for s in pair_sums]), 4) if pair_sums else None,
        "round_trip_spread_median": round(_st.median([x - y for x, y in pair_sums]), 4) if pair_sums else None,
        "pairs_ask_sum_below_1": sum(1 for x, _ in pair_sums if x < 1.0),
        "pairs_bid_sum_above_1": sum(1 for _, y in pair_sums if y > 1.0),
    }
    stats["price_only"] = dict(stats["price_only"]); stats["executable"] = dict(stats["executable"])
    stats["distinct_opportunities"] = len(found)
    with open(os.path.join(a.out, f"opportunities_{run_id}.jsonl"), "w") as f:
        for d in found:
            f.write(json.dumps(d, default=str) + "\n")

    L = [f"# Cross-market coherence scan ({run_id})", "",
         f"Discovery `{stats['discovery']}`, {stats['passes']} capture passes, "
         f"{stats['parsed_match_markets']} parsed match-scope markets, {stats['quotes_seen']} executable "
         f"quotes read, {stats['matches_scanned']} match-passes scanned.", "",
         "| scan | what it counts | violations |", "|---|---|---|",
         f"| price-only | executable BID/ASK break a relationship, size ignored | {sum(stats['price_only'].values())} |",
         f"| size-verified | same, but every leg had order-book depth | {sum(stats['executable'].values())} |", ""]
    for mode in ("price_only", "executable"):
        if stats[mode]:
            L += [f"**{mode}** by kind: " + ", ".join(f"{k} {v}" for k, v in sorted(stats[mode].items())), ""]
    exe = [d for d in found if d["mode"] == "executable"]
    if exe:
        exe.sort(key=lambda d: -d["executable_margin"])
        L += ["## Size-verified opportunities", "",
              "| match | kind | family | margin after fees | size | profit | seen for |", "|---|---|---|---|---|---|---|"]
        for d in exe[:25]:
            L.append(f"| {d['match_suffix']} | {d['kind']} | {d['family']} | {d['executable_margin']:+.4f} | "
                     f"{d['size']:.0f} | {d['total_executable_profit']:+.2f} | {d['duration_s']:.0f}s |")
    else:
        L += ["## Size-verified opportunities", "",
              "**None.** No structure on the captured board violated a relationship after order-book depth "
              "and taker fees were applied.", ""]
    bs = stats["board_shape"]
    L += ["", "## Board shape (latest pass), which is what makes the null result readable", "",
          "| measure | value |", "|---|---|",
          f"| open executable quotes by family | {bs['open_quotes_by_family']} |",
          f"| contracts per match | {bs['contracts_per_match']} |",
          f"| two-sided match-winner pairs | {bs['two_sided_match_winner_pairs']} |",
          f"| ask-sum, median (arb needs < 1 minus fees) | {bs['ask_sum_median']} |",
          f"| ask-sum, minimum seen | {bs['ask_sum_min']} |",
          f"| bid-sum, median (arb needs > 1 plus fees) | {bs['bid_sum_median']} |",
          f"| bid-sum, maximum seen | {bs['bid_sum_max']} |",
          f"| round-trip spread, median | {bs['round_trip_spread_median']} |",
          f"| pairs with ask-sum below 1.00 | {bs['pairs_ask_sum_below_1']} |",
          f"| pairs with bid-sum above 1.00 | {bs['pairs_bid_sum_above_1']} |", ""]
    json.dump(stats, open(os.path.join(a.out, f"summary_{run_id}.json"), "w"), indent=1, default=str)
    open(os.path.join(a.out, "RESULTS.md"), "w").write("\n".join(L) + "\n")
    print("\n".join(L))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
