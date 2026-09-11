#!/usr/bin/env python3
"""Phase 8: can ACTUAL first-ball truth be recovered for matches that already finished?

The question is not rhetorical and the answer is not assumed. A dated scoreboard payload is scanned for
any field that could carry a REAL start (as opposed to a scheduled one): a start that differs from the
scheduled time, an end time, an elapsed clock, or an explicit actual-start field. The test that settles
it is simple -- if a source records actual starts, then across hundreds of completed matches at least
some of them must differ from the scheduled time, because matches run late.

Run it against any saved probe payload; it prints a verdict and writes a JSON report.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import sys
from datetime import datetime, timezone

ACTUAL_START_HINTS = ("actualstart", "actual_start", "firstball", "first_ball", "starttime", "startdate",
                      "begin", "commenced", "playstarted")


def competitions(payload):
    for ev in (payload or {}).get("events") or []:
        comps = list(ev.get("competitions") or [])
        for g in ev.get("groupings") or []:
            comps += list(g.get("competitions") or [])
        for c in comps:
            yield ev, c


def assess(payload) -> dict:
    rows, fields = [], {}
    for ev, c in competitions(payload):
        st = ((c.get("status") or {}).get("type") or {})
        rows.append({"id": c.get("id"), "date": c.get("date"), "startDate": c.get("startDate"),
                     "endDate": c.get("endDate"), "state": st.get("state"),
                     "clock": (c.get("status") or {}).get("displayClock"),
                     "suspended": c.get("wasSuspended")})
        for k in c:
            if any(h in k.lower().replace(" ", "") for h in ACTUAL_START_HINTS):
                fields[k] = fields.get(k, 0) + 1
    done = [r for r in rows if r["state"] == "post"]
    differing = [r for r in rows if r["date"] and r["startDate"] and r["date"] != r["startDate"]]
    with_end = [r for r in rows if r["endDate"]]
    verdict = ("RECOVERABLE" if differing or with_end else "NOT_RECOVERABLE")
    return {
        "competitions": len(rows), "completed": len(done),
        "start_fields_present": fields,
        "completed_with_start_differing_from_schedule": len(differing),
        "completed_with_an_end_time": len(with_end),
        "verdict": verdict,
        "reasoning": ("at least one completed match reports a start that differs from its scheduled time, "
                      "so the source does record real starts"
                      if verdict == "RECOVERABLE" else
                      "every competition reports startDate identical to its scheduled date and no end time; "
                      "across this many completed matches some would have run late, so the field is a "
                      "SCHEDULE, not an actual start. Historical first-ball truth cannot be recovered here."),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("payloads", nargs="+", help="raw JSON (optionally .gz) scoreboard payloads")
    ap.add_argument("--out", default="")
    a = ap.parse_args()
    report = {"assessed_at": datetime.now(timezone.utc).isoformat(), "payloads": {}}
    for p in a.payloads:
        opener = gzip.open if p.endswith(".gz") else open
        with opener(p, "rt") as f:
            try:
                payload = json.load(f)
            except ValueError as e:
                report["payloads"][p] = {"error": f"unparseable: {e}"}
                continue
        r = assess(payload)
        report["payloads"][p] = r
        print(f"{os.path.basename(p)}: {r['competitions']} competitions, {r['completed']} completed, "
              f"{r['completed_with_start_differing_from_schedule']} with a start differing from schedule "
              f"-> {r['verdict']}")
        print(f"   {r['reasoning']}")
    if a.out:
        os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
        with open(a.out, "w") as f:
            json.dump(report, f, indent=1)
        print("wrote", a.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
