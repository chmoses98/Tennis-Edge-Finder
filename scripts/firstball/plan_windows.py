#!/usr/bin/env python3
"""Plan the next main-tour handicap window from LIVE start evidence, and get the assisted workflow there early.

Runs inside the first-ball conductor after every polling segment (~10 min), so it always sees the freshest
live-score readings. Each run:

  1. builds the live board from the capture (latest full snapshot + later passes) and reconciles every match's
     start (tennis_edge.firstball.start_times): first-ball truth > live state > live schedule > court
     progression > Kalshi nominal (LOW, never a day placeholder);
  2. groups upcoming ATP/WTA singles matches into windows by EARLIEST credible first ball;
  3. checks whether the published assisted slate is still authoritative (slate_freshness);
  4. decides which refreshes are due (due_actions) and, with --dispatch, triggers them:
       slate_primary   `TENNIS assisted slate` ~45 min before the window's earliest credible first ball
       slate_final     `TENNIS assisted slate` ~10 min before, for the final status/price check
       run_tennis      a full `RUN TENNIS` ~60-95 min before, only when the producer rows are > 3 h old
     each (window, kind) at most once, at most 6 full runs a day;
  5. writes <out>/plan_latest.json, <out>/NEXT_WINDOW.md, and appends <out>/plan_log.jsonl and
     <out>/dispatch_log.jsonl (published with the first-ball store).

It never touches a model, a probability, a candidate or a decision, and it never places anything.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.assisted.schema import level_bucket, match_code_of, series_of     # noqa: E402
from tennis_edge.firstball import start_times as ST                                # noqa: E402
from tennis_edge.firstball.start_evidence import board_statuses                     # noqa: E402
from tennis_edge.firstball.watchlist import capture_board                           # noqa: E402
from tennis_edge.kalshi.families import SERIES                                      # noqa: E402

WORKFLOWS = {"run_tennis": "tennis-run.yml", "slate_primary": "tennis-assisted-slate.yml",
             "slate_final": "tennis-assisted-slate.yml", "slate_stale_refresh": "tennis-assisted-slate.yml"}
#: at most one stale-slate rebuild per this many minutes (each rebuild takes a fresh open-market snapshot)
STALE_REFRESH_MIN = 20


def board_entries(capture_root: str, now: datetime) -> list[dict]:
    """One entry per physical match on the live board that has a match-winner market."""
    from tennis_edge.kalshi.markets import parse_market
    seen: dict[str, dict] = {}
    for t, m in capture_board(capture_root, now).items():
        s = series_of(t)
        fam = SERIES.get(s)
        if not fam or fam[0] != "MATCH_WINNER":
            continue
        code = match_code_of(m.get("event_ticker") or t)
        key = f"{fam[1]}:{code}:{fam[3]}"
        e = seen.setdefault(key, {"match_id": m.get("event_ticker") or t, "key": key, "code": code, "series": s,
                                  "nominal": m.get("occurrence_datetime") or m.get("expected_expiration_time"),
                                  "level_bucket": level_bucket(s, None, fam[3]), "discipline": fam[3], "names": {}})
        pm = parse_market(m)
        if pm.subject and pm.subject_is_a is not None:
            e["names"][pm.subject_is_a] = pm.subject
    out = []
    for e in seen.values():
        e["label"] = f"{e['names'].get(True, '?')} vs {e['names'].get(False, '?')}"
        out.append(e)
    return out


def _last_jsonl(path: str) -> dict | None:
    last = None
    if os.path.exists(path):
        with open(path) as f:
            for line in f:
                if line.strip():
                    try:
                        last = json.loads(line)
                    except ValueError:
                        continue
    return last


def _read_jsonl(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    out = []
    with open(path) as f:
        for line in f:
            if line.strip():
                try:
                    out.append(json.loads(line))
                except ValueError:
                    continue
    return out


def dispatch(kind: str, reason: str) -> dict:
    """POST a workflow_dispatch. Returns the outcome; never raises (a failed dispatch is logged, and the next
    segment re-plans, so a lost dispatch is retried rather than silently forgotten)."""
    token, repo = os.environ.get("GH_TOKEN"), os.environ.get("GITHUB_REPOSITORY")
    ref = os.environ.get("DISPATCH_REF", "main")
    if not token or not repo:
        return {"dispatched": False, "http": None, "note": "no GH_TOKEN/GITHUB_REPOSITORY (dry run)"}
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{WORKFLOWS[kind]}/dispatches"
    req = urllib.request.Request(url, data=json.dumps({"ref": ref}).encode(), method="POST",
                                 headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=20) as r:
            return {"dispatched": r.status in (200, 201, 204), "http": r.status}
    except Exception as e:                                                   # noqa: BLE001
        return {"dispatched": False, "http": getattr(e, "code", None), "note": str(e)[:200]}


def render(plan: dict, fresh: dict, actions: list, now: datetime) -> str:
    def hm(x):
        return x[:16].replace("T", " ") + "Z" if isinstance(x, str) and x else "--"
    w = plan.get("next_window")
    L = [f"# NEXT ACTIONABLE MAIN-TOUR WINDOW (planned {now:%Y-%m-%d %H:%M}Z)", ""]
    if w:
        L += [f"* Earliest credible first ball: **{hm(w['earliest_credible_first_ball'])}**",
              f"* Recommended RUN TENNIS time: **{hm(w['recommended_run_tennis_time'])}**"
              + ("  (OVERDUE: run now)" if w["primary_overdue"] else ""),
              f"* Final price/status check time: **{hm(w['final_status_price_check_time'])}**",
              f"* Matches in window: {w['n_matches']}", ""]
        L += ["| match | expected start | status | source | confidence |", "|---|---|---|---|---|"]
        for m in w["matches"]:
            L.append(f"| {m['label']} | {hm(m['current_expected_start'])} | {m['start_status']} | {m['start_time_source']} | "
                     f"{m['start_time_confidence']} |")
    else:
        L += ["* No main-tour singles match currently has a credible upcoming start."]
    unv = plan.get("main_tour_status_unverified") or []
    if unv:
        L += ["", f"**{len(unv)} main-tour match(es) without a verified start status** (BET blocked until checked): "
                  + ", ".join(u["label"] for u in unv[:12])]
    L += ["", f"Published slate: `{fresh.get('slate_id')}` built {hm(fresh.get('slate_built_at'))} -- "
              + ("**STALE / NEEDS REFRESH**: " + "; ".join(fresh.get("reasons") or []) if fresh.get("stale") else "current"),
          "", "Dispatched this pass: " + (", ".join(f"{a['kind']} ({'ok' if a.get('dispatched') else a.get('note') or a.get('http')})"
                                                     for a in actions) or "none"), ""]
    for i, x in enumerate(plan.get("windows") or [], 1):
        if i == 1:
            continue
        L.append(f"* later window {i}: first ball {hm(x['earliest_credible_first_ball'])}, run by {hm(x['recommended_run_tennis_time'])}, "
                 f"{x['n_matches']} match(es)")
    return "\n".join(L) + "\n"


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--store", default=os.path.join(PROJ, "data", "firstball", "store"))
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"))
    ap.add_argument("--slates", default=os.path.join(PROJ, "data", "research", "assisted_slates"))
    ap.add_argument("--out", default=None, help="default <store>/schedule")
    ap.add_argument("--now", default=None, help="ISO time for a deterministic replay")
    ap.add_argument("--dispatch", action="store_true", help="trigger due refreshes via workflow_dispatch")
    a = ap.parse_args(argv)
    now = ST._parse(a.now) if a.now else datetime.now(timezone.utc)
    out = a.out or os.path.join(a.store, "schedule")
    os.makedirs(out, exist_ok=True)

    entries = board_entries(a.capture, now)
    statuses = board_statuses([{"match_id": e["key"], "code": e["code"], "series": e["series"], "nominal": e["nominal"],
                                "level_bucket": e["level_bucket"]} for e in entries], store_root=a.store, now=now)
    plan_in = [{"match_id": e["match_id"], "label": e["label"], "level_bucket": e["level_bucket"],
                "discipline": e["discipline"], "start": statuses[e["key"]]} for e in entries]
    plan = ST.plan_windows(plan_in, now)
    try:
        slate = json.load(open(os.path.join(a.slates, "latest.json")))
    except (OSError, ValueError):
        slate = None
    fresh = ST.slate_freshness(slate, plan, now)
    run = _last_jsonl(os.path.join(a.slates, "slate_runs.jsonl")) or {}
    srcs = run.get("sources") or {}
    log_path = os.path.join(out, "dispatch_log.jsonl")
    log = _read_jsonl(log_path)
    actions = ST.due_actions(plan, now, last_slate_built_at=run.get("built_at"),
                             last_model_run_at=srcs.get("shadow_last") or srcs.get("ledger_last"), dispatch_log=log)
    # 2026-10-05: a slate that has gone stale because a match STARTED, became ambiguous or moved 15+ minutes
    # earlier is not left standing until the next planned refresh -- the slate is rebuilt now, at most once per
    # STALE_REFRESH_MIN minutes, so a person never reads an old slate as current for longer than that.
    if any(r.startswith("STATUS_OR_SCHEDULE_CHANGED_SINCE_BUILD") for r in fresh.get("reasons") or []):
        recent = [x for x in log if x.get("kind") == "slate_stale_refresh" and x.get("at")
                  and (now - ST._parse(x["at"])).total_seconds() < STALE_REFRESH_MIN * 60]
        if not recent and not any(x["kind"].startswith("slate") for x in actions):
            actions.append({"kind": "slate_stale_refresh", "at": now.isoformat(),
                            "reason": f"published slate {fresh.get('slate_id')} is stale: {len(fresh.get('changed_matches') or [])} "
                                      "match(es) changed status/start since it was built"})
    for act in actions:
        act.update(dispatch(act["kind"], act["reason"]) if a.dispatch else {"dispatched": False, "note": "plan only"})
        with open(log_path, "a") as f:
            f.write(json.dumps(act, default=str) + "\n")
    counts: dict = {}
    for st in statuses.values():
        counts[st["start_status"]] = counts.get(st["start_status"], 0) + 1
    body = {"generated_at": now.isoformat(), "planner": "start_times_v1", "AUTONOMOUS_REAL_MONEY_AUTHORITY": "OFF",
            "board_matches": len(entries), "counts_by_status": counts, **plan, "slate_freshness": fresh,
            "actions_this_pass": actions,
            "statuses": {e["match_id"]: {**statuses[e["key"]], "label": e["label"], "level_bucket": e["level_bucket"]}
                         for e in entries if e["level_bucket"] in ST.COVERED_BUCKETS and e["discipline"] == "singles"}}
    tmp = os.path.join(out, "plan_latest.json.tmp")
    with open(tmp, "w") as f:
        json.dump(body, f, indent=1, default=str)
    os.replace(tmp, os.path.join(out, "plan_latest.json"))
    with open(os.path.join(out, "NEXT_WINDOW.md"), "w") as f:
        f.write(render(plan, fresh, actions, now))
    nw = plan.get("next_window") or {}
    with open(os.path.join(out, "plan_log.jsonl"), "a") as f:
        f.write(json.dumps({"generated_at": now.isoformat(), "next_window": nw.get("earliest_credible_first_ball"),
                            "run_by": nw.get("recommended_run_tennis_time"), "n_matches": nw.get("n_matches"),
                            "counts_by_status": counts, "slate_stale": fresh.get("stale"),
                            "actions": [x["kind"] for x in actions]}) + "\n")
    print(json.dumps({"next_window": nw.get("earliest_credible_first_ball"), "run_by": nw.get("recommended_run_tennis_time"),
                      "n": nw.get("n_matches"), "counts": counts, "slate_stale": fresh.get("stale"),
                      "actions": [(x["kind"], x.get("dispatched")) for x in actions]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
