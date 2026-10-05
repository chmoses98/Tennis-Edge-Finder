"""Vectorised exact match-win probabilities: the same recursion as `analytic.match_win_prob`, over arrays.

Why: walk-forward studies price every model on every match (1.5M matches x several models). The scalar
engine costs ~0.65 ms per call and its inversion ~13 ms, which makes honest studies take hours or forces
rounding caches that quietly change the numbers. This module evaluates the identical recursion on numpy
arrays; `tests/test_vectorized_engine.py` asserts agreement with `analytic` to 1e-9 on random inputs for
every supported format, so it is a speed-up and never a second model.

Conventions are exactly those of `analytic`:
    pa = P(A wins a point on A's serve)        pb = P(A wins a point on B's serve)
  * serve alternates by game; inside a tiebreak the pattern is 1-2-2-2 (A, B, B, A, A, ...);
  * the next set is served first by the set's first server iff the set had an even number of games,
    a tiebreak counting as one game;
  * the match probability averages over the coin toss for the first server.
"""
from __future__ import annotations

import numpy as np

from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3

_EPS = 1e-12


def _clip(x):
    return np.clip(np.asarray(x, dtype=float), _EPS, 1.0 - _EPS)


def game_win_prob(p, no_ad: bool = False):
    p = _clip(p)
    q = 1.0 - p
    if no_ad:
        return p ** 4 * (1 + 4 * q + 10 * q ** 2) + 20 * p ** 3 * q ** 3 * p
    deuce = p * p / (p * p + q * q)
    return p ** 4 * (1 + 4 * q + 10 * q ** 2) + 20 * p ** 3 * q ** 3 * deuce


def tiebreak_win_prob(pa, pb, to: int = 7, a_serves_first: bool = True):
    pa, pb = _clip(pa), _clip(pb)
    tie = pa * pb / (pa * pb + (1 - pa) * (1 - pb))
    # forward DP over point scores; absorbing at a decided score or at a tie >= (to-1, to-1)
    reach = {(0, 0): np.ones_like(pa)}
    win = np.zeros_like(pa)
    for k in range(0, 2 * to):
        nxt: dict = {}
        for (a, b), pr in reach.items():
            if a + b != k:
                continue
            if a >= to - 1 and b >= to - 1 and a == b:
                win = win + pr * tie
                continue
            first = (k == 0) or (((k + 1) // 2) % 2 == 0)
            a_serving = first if a_serves_first else not first
            p = pa if a_serving else pb
            for (na, nb, m) in ((a + 1, b, pr * p), (a, b + 1, pr * (1 - p))):
                if na >= to and na - nb >= 2:
                    win = win + m
                elif nb >= to and nb - na >= 2:
                    pass
                else:
                    nxt[(na, nb)] = nxt.get((na, nb), 0.0) + m
        for key, v in nxt.items():
            reach[key] = v
        reach = {key: v for key, v in reach.items() if key[0] + key[1] > k}
        if not reach:
            break
    return win


def _set_outcomes(pa, pb, tiebreak_at, tiebreak_to, no_ad, a_first: bool):
    """Return dict (a_won: bool, next_first_is_a: bool) -> prob array for one set."""
    ga = game_win_prob(pa, no_ad)               # A holds
    gb = 1.0 - game_win_prob(1.0 - pb, no_ad)   # A breaks
    out = {(True, True): 0.0, (True, False): 0.0, (False, True): 0.0, (False, False): 0.0}

    def add(a_won, n_games, m):
        nf = a_first if (n_games % 2 == 0) else (not a_first)
        out[(a_won, nf)] = out[(a_won, nf)] + m

    layer = {(0, 0): np.ones_like(ga)}
    while layer:
        nxt: dict = {}
        for (a, b), pr in layer.items():
            g = a + b
            a_serving = ((g % 2) == 0) == a_first
            pw = ga if a_serving else gb
            for da, db, q in ((1, 0, pw), (0, 1, 1 - pw)):
                na, nb = a + da, b + db
                m = pr * q
                if tiebreak_at is not None and na == tiebreak_at and nb == tiebreak_at:
                    tb_first_a = (((na + nb) % 2) == 0) == a_first
                    t = tiebreak_win_prob(pa, pb, tiebreak_to, tb_first_a)
                    add(True, na + nb + 1, m * t)
                    add(False, na + nb + 1, m * (1 - t))
                    continue
                if na >= 6 and na - nb >= 2:
                    add(True, na + nb, m); continue
                if nb >= 6 and nb - na >= 2:
                    add(False, na + nb, m); continue
                if tiebreak_at is None and na == nb and na >= 5:
                    # advantage set from an even tie: two games, one on each serve, decide or re-tie.
                    # A tie at k-k has 2k games played, so the eventual total is even -> next-first unchanged.
                    den = ga * gb + (1 - ga) * (1 - gb)
                    tie = np.where(den > 0, ga * gb / np.where(den > 0, den, 1.0), 0.5)
                    add(True, 2 * na + 2, m * tie)
                    add(False, 2 * na + 2, m * (1 - tie))
                    continue
                nxt[(na, nb)] = nxt.get((na, nb), 0.0) + m
        layer = nxt
    return out


def match_win_prob(pa, pb, fmt: MatchFormat = TOUR_SINGLES_BO3):
    """P(A wins the match), elementwise over arrays pa, pb."""
    pa, pb = _clip(pa), _clip(pb)
    fs_at, fs_to = fmt.final_set_rule()
    n_win = fmt.sets_to_win
    cache: dict = {}

    def set_out(is_final, a_first):
        key = (is_final, a_first)
        if key not in cache:
            if is_final and fmt.final_set == "MATCH_TB10":
                t = tiebreak_win_prob(pa, pb, 10, a_first)
                cache[key] = {(True, not a_first): t, (False, not a_first): 1 - t,
                              (True, a_first): 0.0, (False, a_first): 0.0}
            elif is_final:
                cache[key] = _set_outcomes(pa, pb, fs_at, fs_to, fmt.no_ad, a_first)
            else:
                cache[key] = _set_outcomes(pa, pb, fmt.tiebreak_at, fmt.tiebreak_to, fmt.no_ad, a_first)
        return cache[key]

    memo: dict = {}

    def rec(sa, sb, a_first):
        if sa == n_win:
            return 1.0
        if sb == n_win:
            return 0.0
        k = (sa, sb, a_first)
        if k in memo:
            return memo[k]
        is_final = (sa + sb + 1 == fmt.best_of)
        tot = 0.0
        for (a_won, nf), q in set_out(is_final, a_first).items():
            tot = tot + q * rec(sa + (1 if a_won else 0), sb + (0 if a_won else 1), nf)
        memo[k] = tot
        return tot

    return 0.5 * (rec(0, 0, True) + rec(0, 0, False))


def point_probs_from_match_prob(target, spw_sum, fmt: MatchFormat = TOUR_SINGLES_BO3, iters: int = 60):
    """Vectorised `analytic.point_probs_from_match_prob`: bisection on the serve-strength gap with
    pa + (1 - pb) = spw_sum, elementwise."""
    target = _clip(target)
    spw_sum = np.broadcast_to(np.asarray(spw_sum, dtype=float), target.shape)
    lo = np.full(target.shape, -0.5)
    hi = np.full(target.shape, 0.5)
    for _ in range(iters):
        mid = 0.5 * (lo + hi)
        f = match_win_prob(_clip(spw_sum / 2 + mid), _clip(1 - (spw_sum / 2 - mid)), fmt)
        below = f < target
        lo = np.where(below, mid, lo)
        hi = np.where(below, hi, mid)
    d = 0.5 * (lo + hi)
    return _clip(spw_sum / 2 + d), _clip(1 - (spw_sum / 2 - d))


def reformat_match_prob(p_bo3, spw_sum, fmt: MatchFormat):
    """Translate a format-agnostic (best-of-3 basis) match probability to `fmt` through the point
    probabilities it implies -- exactly what production does for Elo (bo5 amplifies the favourite)."""
    p_bo3 = np.asarray(p_bo3, dtype=float)
    if fmt == TOUR_SINGLES_BO3:
        return p_bo3.copy()
    pa, pb = point_probs_from_match_prob(p_bo3, spw_sum, TOUR_SINGLES_BO3)
    return match_win_prob(pa, pb, fmt)
