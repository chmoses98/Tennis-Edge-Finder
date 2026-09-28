"""Reproducible interval estimates for candidate scoring.

Every interval in the confirmation layer comes from here, with ONE fixed seed, so re-running the harvest
on the same evidence reproduces every published number to the last digit. The seed was fixed before any
prospective outcome was read and is never varied: re-drawing until an interval excludes zero is exactly
the kind of hindsight this layer exists to prevent.
"""
from __future__ import annotations

import math

import numpy as np

SEED = 20260927
N_BOOT = 10_000


def mean_ci(x, *, n_boot: int = N_BOOT, seed: int = SEED, alpha: float = 0.05) -> dict:
    """Mean and percentile-bootstrap interval of the mean. Fewer than 3 values gives no interval."""
    a = np.asarray([v for v in x if v is not None and not (isinstance(v, float) and math.isnan(v))], float)
    out = {"n": int(len(a)), "mean": float(a.mean()) if len(a) else None,
           "median": float(np.median(a)) if len(a) else None, "ci_low": None, "ci_high": None,
           "excludes_zero": None, "seed": seed, "n_boot": n_boot}
    if len(a) < 3:
        return out
    rng = np.random.default_rng(seed)
    means = np.empty(n_boot)
    step = max(1, 2_000_000 // max(len(a), 1))       # bound memory on large samples
    for i in range(0, n_boot, step):
        k = min(step, n_boot - i)
        means[i:i + k] = a[rng.integers(0, len(a), size=(k, len(a)))].mean(axis=1)
    lo, hi = np.percentile(means, [100 * alpha / 2, 100 * (1 - alpha / 2)])
    out.update(ci_low=float(lo), ci_high=float(hi), excludes_zero=bool(lo > 0 or hi < 0))
    return out


def paired_ci(a, b, **kw) -> dict:
    """Interval for mean(a - b) resampling PAIRS, so both forecasters see the same bootstrap rows."""
    pairs = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
    return mean_ci([x - y for x, y in pairs], **kw)


def brier_terms(p, y) -> list[float]:
    return [(pi - yi) ** 2 for pi, yi in zip(p, y)]


def log_loss_terms(p, y, eps: float = 1e-9) -> list[float]:
    out = []
    for pi, yi in zip(p, y):
        q = min(max(pi, eps), 1 - eps)
        out.append(-(yi * math.log(q) + (1 - yi) * math.log(1 - q)))
    return out
