"""Projection V2 production artifacts.

Two artifacts, deliberately separate:

1. COEFFICIENTS (config/projection_v2/coefficients.json, committed): the frozen stacker weights per tour,
   fitted walk-forward exactly as the research protocol prescribes for the current season (season Y uses
   seasons Y-6 .. Y-1). For 2026 these are the weights the 2026 holdout was scored with. They change only
   by a deliberate, versioned refit (`scripts/research/projection_v2/fit_coefficients.py`), never inside a
   production run.

2. STATE (data/processed/v2/state_<tour>.json.gz, rebuilt every RUN TENNIS): every player's end-of-data
   state for the lanes the frozen specification reads -- the chosen Elo variant, the reference Elo (form
   residuals and experience), the envelope's alternative Elo, Gen-2 at both half-lives, form and context --
   plus the data horizon per level so live inference knows which schedule features it can trust.

Nothing here reads a price.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import os
from datetime import date as _date
from datetime import datetime, timezone

import pandas as pd

from tennis_edge.models.gen2 import Gen2Config
from tennis_edge.v2.elo import EloV2Config
from tennis_edge.v2.form import HORIZONS
from tennis_edge.v2.replay import ELO_VARIANTS, GEN2_VARIANTS, REFERENCE_ELO, replay
from tennis_edge.v2.stacker import LEVEL_GROUPS

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
COEF_PATH = os.path.join(PROJ, "config", "projection_v2", "coefficients.json")
MODEL_VERSION = "projection_v2.0"
#: the envelope's alternative rating (second-best Elo of the selection window)
ALT_ELO = "E_mov"


def load_coefficients(path: str = COEF_PATH) -> dict:
    return json.load(open(path))


def lanes_needed(coef: dict) -> list[str]:
    names = {REFERENCE_ELO, ALT_ELO}
    for t in coef["tours"].values():
        for v in t["variants"].values():
            names.add(v["spec"]["elo"])
    return sorted(names)


def _iso(d):
    return str(d) if d is not None else None


#: a source still "covers" a level group when it has at least this many results of the group in the final
#: SOURCE_COVER_WINDOW_DAYS of its OWN data (a share of all history would exclude a new source such as ESPN)
SOURCE_COVER_MIN_RESULTS = 20
SOURCE_COVER_WINDOW_DAYS = 365
#: per-player activity is measured over this many days before each level's horizon
PRE_HORIZON_DAYS = 365
STALE_GROUP_DAYS = 10


def source_horizons(m: pd.DataFrame) -> tuple[dict, dict]:
    """(horizon, level_activity) per level group.

    horizon[g] = the newest last-result date among the SOURCES that still cover group g (>= SOURCE_COVER_MIN_RESULTS
    of g's results in the final SOURCE_COVER_WINDOW_DAYS of that source's own data). This is how current our data
    for g can be. It is NOT the
    last date g happened to have a match: Grand Slams are seasonal (the "GS" horizon would read four months
    stale on the first day of every Slam and grade every Slam row POOR), and ESPN files WTA 1000 events under
    500/250 (WTA "M" read 43 days stale on 2026-10-05 while Beijing was in the data). A level whose only
    covering source has stopped -- ATP ITF (Sackmann futures, 2026-06-01), WTA ITF and WTA 125 (2026-04-27) --
    keeps exactly that source's date. level_activity[g] is the old per-level last date, kept for audit."""
    d = pd.to_datetime(m["tourney_date"])
    grp = m["level_canonical"].map(lambda x: LEVEL_GROUPS.get(str(x), "O"))
    activity = {g: str(v.max().date()) for g, v in d.groupby(grp)}
    src = m["source_label"].astype(str) if "source_label" in m.columns else pd.Series("all", index=m.index)
    last_by_src = d.groupby(src).max()
    own_recent = d > src.map(last_by_src) - pd.Timedelta(days=SOURCE_COVER_WINDOW_DAYS)
    counts = pd.crosstab(src[own_recent], grp[own_recent])
    horizon = {}
    for g in activity:
        covering = [s for s in counts.index if g in counts.columns and counts.at[s, g] >= SOURCE_COVER_MIN_RESULTS]
        horizon[g] = str(max(last_by_src[s] for s in covering).date()) if covering else activity[g]
    return horizon, activity


def pre_horizon_activity(m: pd.DataFrame, horizon: dict, last_date) -> dict:
    """player id -> {group: matches in the PRE_HORIZON_DAYS before that group's horizon}, for every group whose
    horizon is more than STALE_GROUP_DAYS behind the data's last date. Live inference turns this into the
    number of results each player is probably missing (a player who played 40 ITF matches in the year before
    ITF results stopped has ~14 more missing for every further 126 days)."""
    out: dict = {}
    d = pd.to_datetime(m["tourney_date"])
    grp = m["level_canonical"].map(lambda x: LEVEL_GROUPS.get(str(x), "O"))
    last = pd.Timestamp(last_date)
    for g, h in horizon.items():
        h = pd.Timestamp(h)
        if (last - h).days <= STALE_GROUP_DAYS:
            continue
        sel = (grp == g) & (d > h - pd.Timedelta(days=PRE_HORIZON_DAYS)) & (d <= h)
        ids = pd.concat([m.loc[sel, "canonical_winner_id"], m.loc[sel, "canonical_loser_id"]]).dropna().astype(str)
        for pid, n in ids.value_counts().items():
            out.setdefault(pid, {})[g] = int(n)
    return out


def build_state(matches: pd.DataFrame, tour: str, coef: dict, matches_sha256: str | None = None) -> dict:
    """Replay the whole table for one tour with only the lanes production needs; serialise end states."""
    by_name = {c.name: c for c in ELO_VARIANTS}
    elo_cfgs = tuple(by_name[n] for n in lanes_needed(coef))
    _, st = replay(matches, tour, record_from=10 ** 6, elo_variants=elo_cfgs, gen2_variants=GEN2_VARIANTS)
    elos, g2s, sr, form, ctx = st["elos"], st["gen2"], st["sr"], st["form"], st["ctx"]
    ref = elos[REFERENCE_ELO]
    m = matches[(matches.tour == tour) & matches.tourney_date.notna()]
    horizon, activity = source_horizons(m)
    pre = pre_horizon_activity(m, horizon, st["last_date"])
    # last known age per player (live age = last age + elapsed time); ages are pre-match facts
    ages = {}
    if "winner_age" in m.columns:
        mm = m[["tourney_date", "canonical_winner_id", "canonical_loser_id", "winner_age", "loser_age"]].copy()
        mm["tourney_date"] = pd.to_datetime(mm["tourney_date"])
        for idc, agec in (("canonical_winner_id", "winner_age"), ("canonical_loser_id", "loser_age")):
            x = mm[[idc, agec, "tourney_date"]].dropna().sort_values("tourney_date").drop_duplicates(idc, keep="last")
            for pid, age, d in zip(x[idc].astype(str), x[agec], x["tourney_date"]):
                prev = ages.get(pid)
                if prev is None or prev[1] < str(d.date()):
                    ages[pid] = (float(age), str(d.date()))
    players = {}
    for pid in ref.r:
        rec = {"n": ref.n.get(pid, 0), "elo": {name: e.state(pid) for name, e in elos.items()}}
        for k, g in g2s.items():
            rec[k] = {"serve": _ab(g.serve.get(pid)), "ret": _ab(g.ret.get(pid)),
                      "ss": {s: _ab(g.surf_serve[(pid, s)]) for s in ("Hard", "Clay", "Grass", "Carpet") if (pid, s) in g.surf_serve},
                      "sr": {s: _ab(g.surf_ret[(pid, s)]) for s in ("Hard", "Clay", "Grass", "Carpet") if (pid, s) in g.surf_ret}}
        rec["form"] = {str(h): [form.s.get((pid, h), 0.0), form.c.get((pid, h), 0.0)] for h in HORIZONS}
        rec["form_last"] = _iso(form.last.get(pid))
        dq = ctx.recent.get(pid)
        rec["ctx"] = {"recent": [[str(d), mins] for d, mins in (dq or [])],
                      "last_surface": [str(ctx.last_surface[pid][0]), ctx.last_surface[pid][1]] if pid in ctx.last_surface else None,
                      "last_ret_loss": _iso(ctx.last_ret_loss.get(pid))}
        rec["sr_points"] = sr.points_seen(pid)
        if pid in ages:
            rec["age"] = list(ages[pid])
        if pid in pre:
            rec["pre_horizon"] = pre[pid]
        players[pid] = rec
    g2_globals = {k: {"base_num": dict(g.base_num), "base_den": dict(g.base_den),
                      "level_num": {f"{a}|{b}": v for (a, b), v in g.level_num.items()},
                      "level_den": {f"{a}|{b}": v for (a, b), v in g.level_den.items()},
                      "cfg": g.cfg.to_dict()} for k, g in g2s.items()}
    sr_base = {f"{a}|{b}": sr.base_num[(a, b)] / sr.base_den[(a, b)] for (a, b) in sr.base_den if sr.base_den[(a, b)] > 0}
    return {"model_version": MODEL_VERSION, "tour": tour, "built_at": datetime.now(timezone.utc).isoformat(),
            "matches_sha256": matches_sha256, "last_date": st["last_date"], "n_matches": st["n_matches"],
            "data_horizon_by_level_group": horizon, "data_horizon_basis": "source_coverage_v2",
            "level_activity_last_date": activity, "pre_horizon_days": PRE_HORIZON_DAYS, "elo_configs": {c.name: c.to_dict() for c in elo_cfgs},
            "gen2": g2_globals, "sr_baseline": sr_base, "sr_base_raw": {f"{a}|{b}": [sr.base_num[(a, b)], sr.base_den[(a, b)]] for (a, b) in sr.base_den},
            "coefficients_fingerprint": coef.get("fingerprint"), "players": players}


def _ab(a):
    return [a.num, a.den, str(a.last) if a.last else None] if a is not None else None


def save_state(state: dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt") as f:
        json.dump(state, f, separators=(",", ":"), default=str)


def load_state(path: str) -> dict:
    with gzip.open(path, "rt") as f:
        return json.load(f)


def fingerprint(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, default=str).encode()).hexdigest()[:16]
