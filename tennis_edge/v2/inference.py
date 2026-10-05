"""Projection V2 live inference: the research feature builder, applied to persisted end states.

`ProjectionV2.project(a, b, on=..., level=..., surface=..., fmt=...)` rebuilds the ONE-ROW frame the replay
would have recorded for this match (same column names, same state semantics) and runs the frozen
`stacker.build_features` + coefficients on it. `tests/test_v2_inference.py` asserts the result equals the
replay's own prediction for the same state, so research and production cannot drift.

Two things live inference must do that the backtest never had to:

* STALE DATA. Historical results are complete; live ones are not (no free source carries ITF results after
  April (WTA) / June (ATP) 2026, ATP Challenger lags ~2 weeks). A player with no result in our data for 150
  days looks LAID OFF to the context features even if they played yesterday. When the data horizon of the
  match's level is more than STALE_HORIZON_DAYS behind the match date, the schedule-derived features (rest,
  layoffs, 14-day load, 7-day minutes, recent retirement, surface switch, 30-day form) are NEUTRALISED for
  both players (their difference set to zero, i.e. "both have been playing normally") and the projection is
  tagged CONTEXT_NEUTRALISED_STALE_DATA with a quality downgrade. The ratings themselves are as stale as the
  data; the uncertainty envelope widens with the gap instead of pretending otherwise.
* MATCH-SPECIFIC FACTS the replay read from the row itself: matches already played in this event (unknown
  live for most levels -> 0 for both) and age (last known age plus elapsed time).

No prices are read here; the market enters only downstream, beside the frozen output.
"""
from __future__ import annotations

import math
from collections import deque
from dataclasses import replace
from datetime import date as _date

import numpy as np
import pandas as pd

from tennis_edge.models.gen2 import Gen2Config, Gen2State, _Ability
from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3
from tennis_edge.sim import vectorized as vz
from tennis_edge.v2.elo import EloV2, EloV2Config
from tennis_edge.v2.form import HORIZONS, ContextState, FormState, rest_feature
from tennis_edge.v2.replay import BO5, REFERENCE_ELO
from tennis_edge.v2.stacker import FittedStacker, LEVEL_GROUPS

STALE_HORIZON_DAYS = 10
#: assumed rating drift per player while results are missing, logit units per sqrt(year). An ASSUMPTION, not
#: a fitted quantity: it only widens the envelope (and is labelled so) when data are stale.
DRIFT_LOGIT_PER_SQRT_YEAR = 0.30
CONTEXT_FEATURES = ("rest", "layoff60", "layoff180", "n14", "mins7", "ret30", "surf_switch", "in_event")


def _d(x):
    return _date.fromisoformat(str(x)[:10]) if x else None


def _unab(v):
    a = _Ability()
    if v:
        a.num, a.den = float(v[0]), float(v[1])
        a.last = _d(v[2])
    return a


class ProjectionV2:
    def __init__(self, state: dict, coefficients: dict):
        self.state = state
        self.tour = state["tour"]
        self.coef = coefficients
        tour_coef = coefficients["tours"][self.tour]["variants"]
        self.stackers = {k: FittedStacker.from_dict(v) for k, v in tour_coef.items()}
        self.base = self.stackers["base"]
        self.elo_cfgs = {}
        for name, d in state["elo_configs"].items():
            d = dict(d)
            self.elo_cfgs[name] = EloV2Config(**{k: v for k, v in d.items()})
        self.players = state["players"]
        self.horizon = {k: _d(v) for k, v in state["data_horizon_by_level_group"].items()}

    # ------------------------------------------------------------------ lane readers (same semantics as replay)
    def _elo_p(self, name, a, b, surface, level):
        e = EloV2(self.elo_cfgs[name])
        for p in (a, b):
            rec = (self.players.get(p) or {}).get("elo", {}).get(name)
            if rec and rec.get("r") is not None:
                e.r[p], e.n[p] = rec["r"], rec["n"]
                for s, (rs, ns) in (rec.get("surf") or {}).items():
                    e.rs[(p, s)], e.ns[(p, s)] = rs, ns
        return e.predict(a, b, surface, level)

    def _gen2(self, key, a, b, level, surface):
        g = self.state["gen2"][key]
        st = Gen2State(cfg=Gen2Config(**g["cfg"]))
        st.base_num, st.base_den = dict(g["base_num"]), dict(g["base_den"])
        st.level_num = {tuple(k.split("|", 1)): v for k, v in g["level_num"].items()}
        st.level_den = {tuple(k.split("|", 1)): v for k, v in g["level_den"].items()}
        for p in (a, b):
            r = (self.players.get(p) or {}).get(key)
            if not r:
                continue
            if r.get("serve"):
                st.serve[p] = _unab(r["serve"])
            if r.get("ret"):
                st.ret[p] = _unab(r["ret"])
            for s, v in (r.get("ss") or {}).items():
                st.surf_serve[(p, s)] = _unab(v)
            for s, v in (r.get("sr") or {}).items():
                st.surf_ret[(p, s)] = _unab(v)
        pa, pb = st.predict_point_probs(a, b, self.tour, level, surface)
        return pa, pb, st.evidence(a), st.evidence(b)

    def _spw(self, surface):
        """ServeReturnModel.baseline(tour, surface), from the persisted sums."""
        raw = self.state["sr_base_raw"]
        key = f"{self.tour}|{surface}"
        num, den = raw.get(key, (0.0, 0.0))
        if den < 2000:
            tn = sum(v[0] for k, v in raw.items() if k.startswith(self.tour + "|"))
            td = sum(v[1] for k, v in raw.items() if k.startswith(self.tour + "|"))
            if td >= 2000:
                return tn / td
            return 0.64 if self.tour == "ATP" else 0.57
        return num / den

    def _form(self, p, on):
        fs = FormState()
        r = self.players.get(p) or {}
        for h in HORIZONS:
            s, c = (r.get("form") or {}).get(str(h), (0.0, 0.0))
            fs.s[(p, h)], fs.c[(p, h)] = s, c
        if r.get("form_last"):
            fs.last[p] = _d(r["form_last"])
        return fs.read(p, on)

    def _ctx(self, p, on, surface):
        cs = ContextState()
        r = (self.players.get(p) or {}).get("ctx") or {}
        if r.get("recent"):
            cs.recent[p] = deque((_d(d), m) for d, m in r["recent"])
        if r.get("last_surface"):
            cs.last_surface[p] = (_d(r["last_surface"][0]), r["last_surface"][1])
        if r.get("last_ret_loss"):
            cs.last_ret_loss[p] = _d(r["last_ret_loss"])
        return cs.read(p, on, surface, None)

    def _age(self, p, on):
        r = (self.players.get(p) or {}).get("age")
        if not r:
            return np.nan
        return float(r[0]) + (on - _d(r[1])).days / 365.25

    # ------------------------------------------------------------------ the one-row frame
    def frame(self, a, b, *, on: _date, level: str, surface: str | None, best_of: int = 3) -> pd.DataFrame:
        names = {self.base.spec.elo, REFERENCE_ELO}
        names |= {s.spec.elo for s in self.stackers.values()}
        row = {"season": on.year, "level": level, "surface": surface, "best_of": best_of, "y": np.nan}
        for name in names:
            row[f"p_{name}"] = self._elo_p(name, a, b, surface, level)
        for key in ("g2", "g2s"):
            pa, pb, ea, eb = self._gen2(key, a, b, level, surface)
            row.update({f"{key}_pa": pa, f"{key}_pb": pb, f"{key}_ev_a": ea, f"{key}_ev_b": eb})
        row["spw"] = self._spw(surface)
        row["n_a"] = (self.players.get(a) or {}).get("n", 0)
        row["n_b"] = (self.players.get(b) or {}).get("n", 0)
        for side, p in (("a", a), ("b", b)):
            fr = self._form(p, on)
            for h in HORIZONS:
                row[f"form{h}_{side}"] = fr[f"form{h}"]
                row[f"cnt{h}_{side}"] = fr[f"cnt{h}"]
            cx = self._ctx(p, on, surface)
            row[f"rest_{side}"] = rest_feature(cx["days"])
            row[f"days_{side}"] = cx["days"] if cx["days"] is not None else np.nan
            for c in ("n14", "mins7", "surf_switch", "ret30", "in_event"):
                row[f"{c}_{side}"] = cx[c]
            row[f"age_{side}"] = self._age(p, on)
        df = pd.DataFrame([row])
        bo5 = best_of == 5
        for name in names:
            p = df[f"p_{name}"].to_numpy().copy()
            if bo5:
                p = vz.reformat_match_prob(p, 2 * df["spw"].to_numpy(), BO5)
            df[f"pf_{name}"] = p
        fmt = BO5 if bo5 else TOUR_SINGLES_BO3
        for key in ("g2", "g2s"):
            df[f"pf_{key}"] = vz.match_win_prob(df[f"{key}_pa"].to_numpy(), df[f"{key}_pb"].to_numpy(), fmt)
        df["g2_ev_min"] = np.minimum(df["g2_ev_a"], df["g2_ev_b"])
        return df

    # ------------------------------------------------------------------ public
    def stale_days(self, level: str, on: _date) -> int:
        h = self.horizon.get(LEVEL_GROUPS.get(level, "O"))
        return max(0, (on - h).days) if h else 9999

    def project(self, a: str, b: str, *, on: _date, level: str, surface: str | None, fmt: MatchFormat = TOUR_SINGLES_BO3,
                identity_confidence: float = 1.0) -> dict:
        best_of = 5 if fmt.best_of == 5 else 3
        raw = self.frame(a, b, on=on, level=level, surface=surface, best_of=best_of)
        stale = self.stale_days(level, on)
        neutralised = stale > STALE_HORIZON_DAYS
        df = self._neutralise(raw) if neutralised else raw
        # TRUE days since each player's last result in our data (read before any neutralisation)
        days_raw = [None if np.isnan(raw[f"days_{s}"].iloc[0]) else int(raw[f"days_{s}"].iloc[0]) for s in ("a", "b")]
        player_stale = max(d if d is not None else 9999 for d in days_raw)
        probs = {k: float(s.predict(df)[0]) for k, s in self.stackers.items()}
        p = probs["base"]
        # translate to a non-standard format of the same length (match tiebreak, no-ad) through point probs
        std = BO5 if best_of == 5 else TOUR_SINGLES_BO3
        reformatted = fmt.final_set != std.final_set or fmt.no_ad != std.no_ad or fmt.tiebreak_at != std.tiebreak_at
        spw2 = 2 * float(df["spw"].iloc[0])

        def to_fmt(x):
            if not reformatted:
                return x
            pa, pb = vz.point_probs_from_match_prob(np.array([x]), spw2, std)
            return float(vz.match_win_prob(pa, pb, fmt)[0])
        p_fmt = to_fmt(p)
        vals = [to_fmt(v) for v in probs.values()]
        drift = 0.0
        if neutralised:
            drift = 1.645 * math.sqrt(2) * DRIFT_LOGIT_PER_SQRT_YEAR * math.sqrt(stale / 365.0)
            z = math.log(p_fmt / (1 - p_fmt))
            vals += [1 / (1 + math.exp(-(z - drift))), 1 / (1 + math.exp(-(z + drift)))]
        lo, hi = min(vals), max(vals)
        ev_min = float(df["g2_ev_min"].iloc[0])
        n_min = int(min(df["n_a"].iloc[0], df["n_b"].iloc[0]))
        tags = []
        if n_min < 15:
            tags.append("THIN_RATING_HISTORY")
        if ev_min < 300:
            tags.append("NO_SERVE_EVIDENCE")
        if neutralised:
            tags.append(f"CONTEXT_NEUTRALISED_STALE_DATA({stale}d)")
        if player_stale > 180:
            tags.append(f"STALE_PLAYER_RATING({player_stale}d)")
        if identity_confidence < 0.95:
            tags.append("IDENTITY_ALIAS")
        if reformatted:
            tags.append("FORMAT_TRANSLATED")
        width = hi - lo
        if width > 0.15:
            tags.append("WIDE_ENVELOPE")
        if identity_confidence < 0.85 or n_min < 5 or width > 0.25 or stale > 90 or player_stale > 180:
            grade = "POOR"
        elif identity_confidence >= 0.95 and n_min >= 40 and ev_min >= 1000 and not neutralised and width <= 0.08:
            grade = "HIGH"
        elif identity_confidence >= 0.95 and n_min >= 15 and stale <= 60 and width <= 0.15:
            grade = "MEDIUM"
        else:
            grade = "LOW"
        feats, names = __import__("tennis_edge.v2.stacker", fromlist=["build_features"]).build_features(df, self.base.spec)
        return {"p": p_fmt, "p_low": lo, "p_high": hi, "envelope_width": width, "grade": grade, "tags": tags,
                "variants": {k: to_fmt(v) for k, v in probs.items()}, "stale_days": stale,
                "context_neutralised": neutralised, "rating_drift_logit_1p645": drift,
                "components": {"p_elo": float(df[f"pf_{self.base.spec.elo}"].iloc[0]), "p_gen2": float(df["pf_g2"].iloc[0]),
                               "gen2_serve_point_a": float(df["g2_pa"].iloc[0]), "gen2_return_point_a": float(df["g2_pb"].iloc[0])},
                "evidence": {"rated_matches_a": int(df["n_a"].iloc[0]), "rated_matches_b": int(df["n_b"].iloc[0]),
                             "serve_points_a": float(df["g2_ev_a"].iloc[0]), "serve_points_b": float(df["g2_ev_b"].iloc[0]),
                             "days_since_last_result_in_data_a": days_raw[0], "days_since_last_result_in_data_b": days_raw[1],
                             "level_data_horizon_days_behind": stale},
                "features": dict(zip(names, map(float, feats[0]))), "spw": float(df["spw"].iloc[0]),
                "model_version": self.state["model_version"], "state_built_at": self.state["built_at"],
                "state_last_date": self.state["last_date"], "matches_sha256": self.state.get("matches_sha256"),
                "coefficients_fingerprint": self.coef.get("fingerprint"),
                "spec_fingerprint": self.coef.get("frozen_spec_fingerprint")}

    @staticmethod
    def _neutralise(df: pd.DataFrame) -> pd.DataFrame:
        """Both players 'have been playing normally': B's schedule features copied onto A's, so every
        schedule-derived difference is exactly zero, and 30-day form zeroed for both."""
        out = df.copy()
        for c in ("rest", "days", "n14", "mins7", "surf_switch", "ret30", "in_event"):
            out[f"{c}_a"] = 0.0
            out[f"{c}_b"] = 0.0
        out["rest_a"] = out["rest_b"] = rest_feature(7)
        out["days_a"] = out["days_b"] = 7.0
        for h in HORIZONS:
            out[f"form{h}_a"] = 0.0
            out[f"form{h}_b"] = 0.0
        return out
