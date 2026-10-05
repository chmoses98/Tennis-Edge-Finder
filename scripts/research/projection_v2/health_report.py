#!/usr/bin/env python3
"""Before/after table for every TENNIS gate -> research/projection_v2/HEALTH_REMEDIATION.md.

--before / --after are health_latest.json files (run_all() output). Root cause and fix per gate are stated
once, here, so the report and the PR say the same thing.
"""
from __future__ import annotations

import argparse, json, os

OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2", "HEALTH_REMEDIATION.md")

NOTES = {
    "TENNIS-1": ("discovery healthy", "none needed"),
    "TENNIS-2": ("new series KXATPT5RANK (year-end top-5 ranking) not in the family registry",
                 "classified SEASON_RANKING, unpriced (no rankings-race model or rankings feed exists; not faked)"),
    "TENNIS-3": ("the same 16 KXATPT5RANK markets", "same classification"),
    "TENNIS-4": ("unmapped players (most appear in no reachable results source: ITF results stop April/June 2026; "
                 "others are another form of a Sackmann name, refused a minted id) and doubles teammates that "
                 "cannot be resolved; the board is now the full open snapshot (~1,200 projectable markets, not ~90)",
                 "transliteration aliases at 0.85; alias candidates queued for human review; minted ids for new TML/ESPN "
                 "players; detail separates NO_HISTORY (data gap) from fixable identity gaps. Stays FAIL while players "
                 "are absent from every source -- no unsafe matching"),
    "TENNIS-5": ("trade-tape backlog + capture cadence slipping because every pass fetched and checked out the 8 GB "
                 "evidence branch; AFTER: the conductor publishes every ~10 min (median 9.9, max 10.1), but this gate "
                 "reads the newest capture in RUN TENNIS's own pulled copy ~20 min after the pull, so it reads 20-34 min",
                 "blobless fetches and sparse publishes in the capture and first-ball conductors; quadratic ledger append "
                 "fixed (#21). Remaining FAIL is pipeline latency in the measurement -- threshold NOT changed, owner decision"),
    "TENNIS-6": ("330 legacy first-ball violations (pre 2026-09-27 guard) counted forever; AND an unseen active leak: "
                 "2,631 rows priced after the exchange had settled the market",
                 "append-only quarantine register by prediction id; post-settlement class detected; lifecycle guard "
                 "(full open snapshot, settled tickers excluded) so new code cannot produce either class"),
    "TENNIS-7": ("healthy", "none needed"),
    "TENNIS-8": ("all 'sports truth' was Kalshi's own result", "independent lane (Sackmann/TML/ESPN); coverage reported "
                 "overall and among covered levels; stays FAIL: ITF has no independent source"),
    "TENNIS-9": ("no independent truth to reconcile against", "reconciliation of Kalshi settlements against independent truth; "
                 "TML Challenger window narrowed to -6..+2 days after a previous-week meeting was taken as truth (#20)"),
    "TENNIS-10": ("330 post-start rows counted as missing pregame closes", "quarantined post-start rows excluded from "
                  "the pregame-eligible denominator (both rates reported, threshold unchanged)"),
    "TENNIS-11": ("healthy", "none needed"), "TENNIS-12": ("healthy", "none needed"),
    "TENNIS-13": ("healthy", "build manifest now also carries build_version"),
    "TENNIS-14": ("healthy", "none needed"), "TENNIS-15": ("healthy", "none needed"), "TENNIS-16": ("healthy", "none needed"),
    "TENNIS-17": ("healthy (every slate row STALE, held at warnings)", "fresh open snapshot before every slate"),
    "TENNIS-18": ("healthy, but stale slates were detected and not acted on", "planner dispatches a rebuild when a slate goes stale"),
}

KEYS = {"TENNIS-2": ("unknown_series", "parse_rate"), "TENNIS-3": ("unsupported",),
        "TENNIS-4": ("projectable_open_pregame", "projected", "not_projected", "identity_gap_kinds"),
        "TENNIS-5": ("age_min", "trade_backlog_ok"),
        "TENNIS-6": ("n_violations", "violation_classes", "legacy_quarantined", "active_violations", "post_start_rows_in_strict_research"),
        "TENNIS-8": ("ok", "total", "rate"), "TENNIS-9": ("conflicts", "reconciled_against_independent_truth"),
        "TENNIS-10": ("strict_rate", "strict_rate_pregame_eligible", "pregame_eligible")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--before", required=True)
    ap.add_argument("--after", required=True)
    ap.add_argument("--after-label", default="after")
    ap.add_argument("--out", default=OUT)
    a = ap.parse_args()
    b = {g["gate"]: g for g in json.load(open(a.before))}
    af = {g["gate"]: g for g in json.load(open(a.after))}
    L = ["# Health gates: before / after", "",
         f"Before: RUN TENNIS #99 health (main @ 4bd491d). After: {a.after_label}.", "",
         "Thresholds were not changed. Every FAIL that remains is a real condition, stated in its row.", "",
         "| gate | before | after | root cause | fix |", "|---|---|---|---|---|"]
    for k in sorted(set(b) | set(af), key=lambda x: int(x.split("-")[1])):
        rc, fix = NOTES.get(k, ("", ""))
        L.append(f"| {k} {af.get(k, b.get(k))['name']} | {b.get(k, {}).get('status', '--')} | {af.get(k, {}).get('status', '--')} | {rc} | {fix} |")
    L += ["", "## Key detail", ""]
    for k, keys in KEYS.items():
        bd, ad = (b.get(k) or {}).get("detail") or {}, (af.get(k) or {}).get("detail") or {}
        L.append(f"* **{k}** before: " + ", ".join(f"{x}={json.dumps(bd.get(x), default=str)}" for x in keys if x in bd))
        L.append(f"  after: " + ", ".join(f"{x}={json.dumps(ad.get(x), default=str)}" for x in keys if x in ad))
    open(a.out, "w").write("\n".join(L) + "\n")
    print("wrote", a.out)


if __name__ == "__main__":
    main()
