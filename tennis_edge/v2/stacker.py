"""Evidence-aware logistic ensemble (Workstream D) with outcome-only calibration built in (Workstream E).

Every feature is ANTISYMMETRIC in the two players (swapping A and B negates it) and the model has NO
intercept, so P(A beats B) = 1 - P(B beats A) holds exactly -- tested in tests/test_v2_engine.py. The
weights depend only on pre-match quantities (evidence counts, experience, level), never on prices.

Blocks (each one a small, interpretable group of coefficients):
  base     z = logit(Elo probability, match-format adjusted)
  level    z x level group (Slam / Masters / Challenger+125 / ITF / team+other; Tour 250/500 is the base)
           -- a segment-aware recalibration of the rating's sharpness
  exp      z x 1[thinner player has < 10 / 10-40 rated matches] -- shrink when the rating is young
  g2       (logit Gen-2 - z) x 1[thinner player's serve evidence bucket] -- how far to move toward the
           opponent-adjusted serve/return model, learned per evidence level
  sr       the same for the Gen-1 structural model
  g2s      (logit Gen-2 short half-life - logit Gen-2) x 1[evidence >= 1000] -- recent serve/return form
  form<h>  opponent-adjusted residual form difference at horizon h days
  context  rest, layoffs, 14-day load, 7-day minutes, recent retirement, surface switch, matches in event
  age      youth / veteran indicators (ratings lag players who are still improving or declining)

The model is a regularised logistic regression fitted WALK-FORWARD: season Y is predicted by weights fitted
on seasons Y-window .. Y-1 only.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, asdict

import numpy as np
import pandas as pd

LEVEL_GROUPS = {"GRAND_SLAM": "GS", "MASTERS_1000": "M", "TOUR_FINALS": "M", "OLYMPICS": "M", "TOUR_500_250": "T",
                "CHALLENGER": "C", "WTA_125": "C", "ITF": "I", "TEAM": "O", "OTHER": "O"}
EV_EDGES = (300.0, 1000.0, 5000.0, 20000.0)
BLOCK_ORDER = ("level", "exp", "g2", "sr", "g2s", "form", "context", "age")


def _logit(p):
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


def level_group(levels) -> np.ndarray:
    return np.array([LEVEL_GROUPS.get(str(x), "O") for x in levels])


def _bucket(x, edges):
    return np.searchsorted(np.asarray(edges), np.asarray(x, float), side="right")


@dataclass(frozen=True)
class StackerSpec:
    elo: str = "E_lp"
    blocks: tuple = ()
    form_horizon: int = 120
    C: float = 1.0
    window: int = 6

    def to_dict(self):
        d = asdict(self)
        d["blocks"] = list(self.blocks)
        return d

    def fingerprint(self) -> str:
        return hashlib.sha256(json.dumps(self.to_dict(), sort_keys=True).encode()).hexdigest()[:16]


def build_features(df: pd.DataFrame, spec: StackerSpec) -> tuple[np.ndarray, list]:
    z = _logit(df[f"pf_{spec.elo}"].to_numpy())
    cols, names = [z], ["z"]
    blocks = set(spec.blocks)
    if "level" in blocks:
        g = level_group(df["level"].to_numpy())
        for k in ("GS", "M", "C", "I", "O"):
            cols.append(z * (g == k)); names.append(f"z_x_{k}")
    if "exp" in blocks:
        nmin = np.minimum(df["n_a"].to_numpy(float), df["n_b"].to_numpy(float))
        cols.append(z * (nmin < 10)); names.append("z_x_nmin_lt10")
        cols.append(z * ((nmin >= 10) & (nmin < 40))); names.append("z_x_nmin_10_40")
    if "g2" in blocks:
        d = _logit(df["pf_g2"].to_numpy()) - z
        b = _bucket(df["g2_ev_min"].to_numpy(), EV_EDGES)
        for k in range(len(EV_EDGES) + 1):
            cols.append(d * (b == k)); names.append(f"g2_minus_z_ev{k}")
    if "sr" in blocks:
        d = _logit(df["pf_sr"].to_numpy()) - z
        pts = np.minimum(df["sr_pts_a"].to_numpy(float), df["sr_pts_b"].to_numpy(float))
        b = _bucket(pts, (1000.0, 5000.0))
        for k in range(3):
            cols.append(d * (b == k)); names.append(f"sr_minus_z_pts{k}")
    if "g2s" in blocks:
        d = _logit(df["pf_g2s"].to_numpy()) - _logit(df["pf_g2"].to_numpy())
        cols.append(d * (df["g2_ev_min"].to_numpy() >= 1000)); names.append("g2s_minus_g2")
    if "form" in blocks:
        h = spec.form_horizon
        cols.append(df[f"form{h}_a"].to_numpy(float) - df[f"form{h}_b"].to_numpy(float)); names.append(f"form{h}")
    if "context" in blocks:
        da, db = df["days_a"].to_numpy(float), df["days_b"].to_numpy(float)
        cols.append(df["rest_a"].to_numpy(float) - df["rest_b"].to_numpy(float)); names.append("rest")
        for t in (60, 180):
            la = np.where(np.isnan(da), 1.0, da >= t)
            lb = np.where(np.isnan(db), 1.0, db >= t)
            cols.append(la - lb); names.append(f"layoff{t}")
        cols.append(df["n14_a"].to_numpy(float) - df["n14_b"].to_numpy(float)); names.append("n14")
        cols.append((df["mins7_a"].to_numpy(float) - df["mins7_b"].to_numpy(float)) / 100.0); names.append("mins7")
        for c in ("ret30", "surf_switch", "in_event"):
            cols.append(df[f"{c}_a"].to_numpy(float) - df[f"{c}_b"].to_numpy(float)); names.append(c)
    if "age" in blocks:
        aa = df["age_a"].to_numpy(float)
        ab = df["age_b"].to_numpy(float)
        young = lambda a: np.where(np.isnan(a), 0.0, np.clip((23.0 - a) / 5.0, 0, 1))
        vet = lambda a: np.where(np.isnan(a), 0.0, np.clip((a - 30.0) / 5.0, 0, 1))
        cols.append(young(aa) - young(ab)); names.append("young")
        cols.append(vet(aa) - vet(ab)); names.append("veteran")
    X = np.column_stack(cols)
    return np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0), names


@dataclass
class FittedStacker:
    spec: StackerSpec
    names: list
    scale: list
    coef: list
    train_seasons: list = field(default_factory=list)
    n_train: int = 0

    def predict(self, df: pd.DataFrame) -> np.ndarray:
        X, names = build_features(df, self.spec)
        assert names == self.names, (names, self.names)
        z = (X / np.asarray(self.scale)) @ np.asarray(self.coef)
        return 1.0 / (1.0 + np.exp(-z))

    def to_dict(self):
        return {"spec": self.spec.to_dict(), "spec_fingerprint": self.spec.fingerprint(), "names": self.names,
                "scale": self.scale, "coef": self.coef, "train_seasons": self.train_seasons, "n_train": self.n_train}

    @classmethod
    def from_dict(cls, d):
        s = d["spec"]
        spec = StackerSpec(elo=s["elo"], blocks=tuple(s["blocks"]), form_horizon=s["form_horizon"], C=s["C"],
                           window=s["window"])
        return cls(spec=spec, names=d["names"], scale=d["scale"], coef=d["coef"],
                   train_seasons=d.get("train_seasons", []), n_train=d.get("n_train", 0))


def fit(df: pd.DataFrame, spec: StackerSpec) -> FittedStacker:
    from sklearn.linear_model import LogisticRegression
    X, names = build_features(df, spec)
    scale = np.sqrt(np.mean(X ** 2, axis=0))
    scale[scale == 0] = 1.0
    lr = LogisticRegression(C=spec.C, fit_intercept=False, max_iter=500)
    lr.fit(X / scale, df["y"].to_numpy())
    return FittedStacker(spec=spec, names=names, scale=scale.tolist(), coef=lr.coef_[0].tolist(),
                         train_seasons=sorted(int(s) for s in df["season"].unique()), n_train=int(len(df)))


def walk_forward(df: pd.DataFrame, spec: StackerSpec, seasons, min_train_season: int = 2008) -> np.ndarray:
    """Out-of-time predictions: season Y uses weights fitted on seasons Y-window .. Y-1 only."""
    out = np.full(len(df), np.nan)
    season = df["season"].to_numpy()
    for y in seasons:
        tr = (season >= max(y - spec.window, min_train_season)) & (season < y)
        te = season == y
        if not te.any() or not tr.any():
            continue
        f = fit(df.loc[tr], spec)
        out[te] = f.predict(df.loc[te])
    return out
