"""Walk-forward rating states: what did we know on the morning of day D, and nothing more.

The production rating artifact is a single END state. Using it to score a market from July would let
July's own results inform July's prediction, which is the oldest way to invent an edge. This module
replays the canonical table once and records, for every player, the state of their ratings after each
match from a base date onward. Reading "as of D" then means: the last checkpoint STRICTLY BEFORE D, or
the base snapshot if the player has not played since.

Strictly before the DATE, not the timestamp: a player who plays twice on the same day contributes
neither match to a prediction made that day. That is conservative in the only direction that matters.

The serve/return baselines are snapshotted once at the base date. They are tour-wide aggregates over
millions of points and move by less than a thousandth over a summer; carrying them forward would be the
only thing in this file that could smuggle a later fact into an earlier prediction.
"""
from __future__ import annotations

import gzip
import json
import os
from datetime import date as _date

from tennis_edge.models.elo import Elo, EloConfig, match_sort_key
from tennis_edge.models.gen2 import Gen2Config, Gen2State, _Ability, serve_points
from tennis_edge.models.serve_return import ServeReturnModel, SRConfig
from tennis_edge.models.state import PROD_ELO

SURFACES = ("Hard", "Clay", "Grass", "Carpet")


def _ab(a: _Ability) -> list:
    return [a.num, a.den, str(a.last) if a.last else None]


def _unab(v) -> _Ability:
    a = _Ability()
    if v:
        a.num, a.den = float(v[0]), float(v[1])
        a.last = _date.fromisoformat(v[2]) if v[2] else None
    return a


def _g2rec(g2: Gen2State, pid: str) -> dict:
    return {"serve": _ab(g2.serve[pid]) if pid in g2.serve else None,
            "ret": _ab(g2.ret[pid]) if pid in g2.ret else None,
            "ss": {s: _ab(g2.surf_serve[(pid, s)]) for s in SURFACES if (pid, s) in g2.surf_serve},
            "sr": {s: _ab(g2.surf_ret[(pid, s)]) for s in SURFACES if (pid, s) in g2.surf_ret}}


def _rec(elo: Elo, sr: ServeReturnModel, pid: str, name: str | None) -> dict:
    s_ab, r_ab = sr.abilities(pid)
    return {"elo": elo.r.get(pid), "n": elo.n.get(pid, 0),
            "last_date": str(elo.last_date.get(pid)) if elo.last_date.get(pid) else None,
            "surfaces": {s: [elo.rs[(pid, s)], elo.ns[(pid, s)]] for s in SURFACES if (pid, s) in elo.rs},
            "sr_s": s_ab, "sr_r": r_ab, "sr_points": sr.points_seen(pid), "name": name}


def build_asof(matches, tour: str, base_date: _date, elo_cfg: EloConfig = PROD_ELO,
               sr_cfg: SRConfig = SRConfig(), g2_cfg: Gen2Config = Gen2Config()) -> dict:
    """Replay `matches` for one tour; snapshot every player at `base_date` and again after each later match."""
    m = matches[(matches.tour == tour) & (matches.outcome_type != "WALKOVER") & matches.tourney_date.notna()].copy()
    if "canonical_id_status" in m.columns:
        m = m[m.canonical_id_status == "MAPPED"].copy()
        m["winner_id"] = m["canonical_winner_id"].astype(str)
        m["loser_id"] = m["canonical_loser_id"].astype(str)
    else:
        m = m[m.id_system == "sackmann"].copy()
    import pandas as pd
    m["tourney_date"] = pd.to_datetime(m["tourney_date"]).dt.date
    m = match_sort_key(m)

    elo, sr = Elo(elo_cfg), ServeReturnModel(sr_cfg)
    g2 = Gen2State(cfg=g2_cfg)
    names: dict = {}
    base: dict | None = None
    base_g2: dict | None = None
    g2_globals: dict | None = None
    baselines: dict | None = None
    checkpoints: dict = {}
    checkpoints_g2: dict = {}

    for rec in m.itertuples(index=False):
        d = rec.tourney_date
        if base is None and d >= base_date:
            base = {p: _rec(elo, sr, p, names.get(p)) for p in elo.r}
            base_g2 = {p: _g2rec(g2, p) for p in set(g2.serve) | set(g2.ret)}
            g2_globals = _g2_globals(g2)
            baselines = {f"{k[0]}|{k[1]}": sr.base_num[k] / sr.base_den[k] for k in sr.base_den if sr.base_den[k] > 0}
        w, l = rec.winner_id, rec.loser_id
        names[w], names[l] = rec.winner_name, rec.loser_name
        surface, level = rec.surface, rec.level_canonical
        elo._init(w, level); elo._init(l, level)
        sr._decay(w, d); sr._decay(l, d)
        weight = elo_cfg.retirement_weight if rec.outcome_type in ("RETIRED", "DEFAULT") else 1.0
        elo.update(w, l, surface, level, weight, d)
        sr.update(rec)
        row = rec._asdict()
        wp, ww = serve_points(row, "w")
        lp, lw = serve_points(row, "l")
        if wp and lp:
            g2.observe(server=w, returner=l, points=wp, won=ww, tour=rec.tour, level=level, surface=surface, date=d)
            g2.observe(server=l, returner=w, points=lp, won=lw, tour=rec.tour, level=level, surface=surface, date=d)
        if base is not None:
            for p in (w, l):
                checkpoints.setdefault(p, []).append([str(d), _rec(elo, sr, p, names.get(p))])
                if wp and lp:
                    checkpoints_g2.setdefault(p, []).append([str(d), _g2rec(g2, p)])
    if base is None:                      # every match predates the base date
        base = {p: _rec(elo, sr, p, names.get(p)) for p in elo.r}
        base_g2 = {p: _g2rec(g2, p) for p in set(g2.serve) | set(g2.ret)}
        g2_globals = _g2_globals(g2)
        baselines = {f"{k[0]}|{k[1]}": sr.base_num[k] / sr.base_den[k] for k in sr.base_den if sr.base_den[k] > 0}
    return {"tour": tour, "base_date": str(base_date), "n_matches": int(len(m)),
            "elo_config": elo_cfg.__dict__, "gen2_config": g2_cfg.to_dict(), "baselines": baselines,
            "base": base, "checkpoints": checkpoints,
            "gen2_globals": g2_globals, "gen2_base": base_g2, "gen2_checkpoints": checkpoints_g2}


def _g2_globals(g2: Gen2State) -> dict:
    return {"base_num": dict(g2.base_num), "base_den": dict(g2.base_den),
            "level_num": {f"{k[0]}|{k[1]}": v for k, v in g2.level_num.items()},
            "level_den": {f"{k[0]}|{k[1]}": v for k, v in g2.level_den.items()}}


class AsOfStates:
    """Read a walk-forward artifact. `state(pid, on)` is what we knew the morning of `on`."""

    def __init__(self, obj: dict):
        self.tour = obj["tour"]
        self.base_date = _date.fromisoformat(obj["base_date"])
        self.baselines = obj.get("baselines") or {}
        self._base = obj["base"]
        self._cp = {p: [(_date.fromisoformat(d), r) for d, r in lst] for p, lst in obj.get("checkpoints", {}).items()}
        self.gen2_config = Gen2Config(**(obj.get("gen2_config") or {}))
        self._g2_globals = obj.get("gen2_globals") or {}
        self._g2_base = obj.get("gen2_base") or {}
        self._g2_cp = {p: [(_date.fromisoformat(d), r) for d, r in lst]
                       for p, lst in (obj.get("gen2_checkpoints") or {}).items()}

    @classmethod
    def load(cls, path: str) -> "AsOfStates":
        op = gzip.open if path.endswith(".gz") else open
        with op(path, "rt") as f:
            return cls(json.load(f))

    def state(self, pid: str, on: _date) -> dict | None:
        best = None
        for d, r in self._cp.get(pid, ()):
            if d < on:
                best = r
            else:
                break
        if best is not None:
            return best
        return self._base.get(pid)

    def _g2rec_asof(self, pid: str, on: _date) -> dict | None:
        best = None
        for d, r in self._g2_cp.get(pid, ()):
            if d < on:
                best = r
            else:
                break
        return best if best is not None else self._g2_base.get(pid)

    def gen2_state(self, pids, on: _date) -> Gen2State:
        """A Gen2State carrying only what we knew about these players the morning of `on`.

        The tour baseline and level offsets are the ones snapshotted at the base date. They are sums over
        tens of millions of serve points; refreshing them inside the window would be the only path by
        which a later result could reach an earlier prediction, and they move by fractions of a
        thousandth over a season."""
        st = Gen2State(cfg=self.gen2_config)
        g = self._g2_globals
        st.base_num = dict(g.get("base_num") or {})
        st.base_den = dict(g.get("base_den") or {})
        st.level_num = {tuple(k.split("|", 1)): v for k, v in (g.get("level_num") or {}).items()}
        st.level_den = {tuple(k.split("|", 1)): v for k, v in (g.get("level_den") or {}).items()}
        for pid in pids:
            r = self._g2rec_asof(pid, on)
            if not r:
                continue
            if r.get("serve"):
                st.serve[pid] = _unab(r["serve"])
            if r.get("ret"):
                st.ret[pid] = _unab(r["ret"])
            for s, v in (r.get("ss") or {}).items():
                st.surf_serve[(pid, s)] = _unab(v)
            for s, v in (r.get("sr") or {}).items():
                st.surf_ret[(pid, s)] = _unab(v)
        return st

    def known_players(self) -> int:
        return len(self._base)


def save_asof(obj: dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with gzip.open(path, "wt") as f:
        json.dump(obj, f, separators=(",", ":"), default=str)
