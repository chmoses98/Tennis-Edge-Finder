"""The selector: a small, transparent, versioned model of P(our disagreement is informative).

Deliberately an L2 logistic regression with standardised inputs. Not because nothing else could fit
better, but because with a few thousand observations on eighteen days of one exchange, a model whose
every coefficient can be read and argued with is worth more than a model that scores better on the data
that produced it.

Two rules are enforced in code rather than remembered:

* **Chronology.** A selector declares the window it was fitted on. Fitting it on a row dated on or after
  its declared end raises, and so does fitting one window's selector on another window's data. There is
  no flag to turn this off.
* **The confirmation set is untouchable.** `score` records the latest date it has ever been asked about,
  but fitting is refused once a selector has been frozen. A frozen selector can be read, applied and
  compared; it cannot be re-fitted to make a holdout look better.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone

import numpy as np
import pandas as pd


class SelectorFirewallError(RuntimeError):
    """Raised when fitting would touch data the selector is not allowed to see."""


def _sigmoid(z):
    return np.where(z >= 0, 1 / (1 + np.exp(-np.clip(z, -50, 50))),
                    np.exp(np.clip(z, -50, 50)) / (1 + np.exp(np.clip(z, -50, 50))))


def fit_l2_logistic(X, y, l2=10.0, iters=200):
    """Newton steps with an L2 penalty on the slopes; the intercept is unpenalised."""
    n, k = X.shape
    Xb = np.hstack([np.ones((n, 1)), X])
    beta = np.zeros(k + 1)
    pen = np.eye(k + 1) * l2
    pen[0, 0] = 0.0
    for _ in range(iters):
        p = _sigmoid(Xb @ beta)
        g = Xb.T @ (y - p) - pen @ beta
        W = np.clip(p * (1 - p), 1e-9, None)
        H = -(Xb.T * W) @ Xb - pen
        try:
            step = np.linalg.solve(H, g)
        except np.linalg.LinAlgError:
            break
        beta -= step
        if np.max(np.abs(step)) < 1e-9:
            break
    return beta


@dataclass
class Selector:
    version: str
    feature_names: tuple
    target: str
    trained_from: str            # ISO date, inclusive
    trained_through: str         # ISO date, INCLUSIVE; nothing on or after the next day was seen
    l2: float = 10.0
    mean: tuple = ()
    std: tuple = ()
    beta: tuple = ()
    n_train: int = 0
    frozen_at: str = ""
    notes: str = ""
    schema_version: int = 1
    _frozen: bool = field(default=False, repr=False)

    # ------------------------------------------------------------------ fit
    def fit(self, X: pd.DataFrame, y, dates) -> "Selector":
        if self._frozen:
            raise SelectorFirewallError(f"{self.version} is frozen; re-fitting it is not allowed")
        dts = pd.to_datetime(pd.Series(list(dates))).dt.date.astype(str)
        lo, hi = str(self.trained_from), str(self.trained_through)
        outside = dts[(dts < lo) | (dts > hi)]
        if len(outside):
            raise SelectorFirewallError(
                f"{self.version} declares {lo}..{hi} but was handed {len(outside)} rows outside it "
                f"({sorted(set(outside))[:3]}...)")
        if tuple(X.columns) != tuple(self.feature_names):
            raise SelectorFirewallError("feature columns do not match the declared feature set")
        A = X.to_numpy(float)
        mu, sd = A.mean(axis=0), A.std(axis=0)
        sd[sd == 0] = 1.0
        self.mean, self.std = tuple(mu), tuple(sd)
        self.beta = tuple(fit_l2_logistic((A - mu) / sd, np.asarray(y, float), l2=self.l2))
        self.n_train = int(len(A))
        return self

    def freeze(self) -> "Selector":
        self._frozen = True
        self.frozen_at = datetime.now(timezone.utc).isoformat()
        return self

    # ---------------------------------------------------------------- score
    def score(self, X: pd.DataFrame) -> np.ndarray:
        if not self.beta:
            raise SelectorFirewallError("selector has not been fitted")
        if tuple(X.columns) != tuple(self.feature_names):
            raise SelectorFirewallError("feature columns do not match the declared feature set")
        A = (X.to_numpy(float) - np.asarray(self.mean)) / np.asarray(self.std)
        return _sigmoid(np.hstack([np.ones((len(A), 1)), A]) @ np.asarray(self.beta))

    # ------------------------------------------------------------ inspection
    def coefficients(self) -> dict:
        return {n: float(b) for n, b in zip(self.feature_names, self.beta[1:])}

    def to_dict(self) -> dict:
        d = {k: v for k, v in asdict(self).items() if not k.startswith("_")}
        d["fingerprint"] = hashlib.sha256(
            json.dumps(d, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Selector":
        d = {k: v for k, v in d.items() if k != "fingerprint"}
        for k in ("feature_names", "mean", "std", "beta"):
            if k in d and d[k] is not None:
                d[k] = tuple(d[k])
        s = cls(**d)
        if s.frozen_at:
            s._frozen = True
        return s
