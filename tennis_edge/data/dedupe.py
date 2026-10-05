"""Cross-source near-duplicate removal: the same physical match reported by two id systems.

Why this exists
---------------
`build.py` dedupes on an EXACT key (tour | tourney_date | round | winner | loser). That key only works when
both sources date a match the same way and name its round the same way, and they do not:

* the TML Challenger mirror dates every match on the Sunday its tournament ENDS, Sackmann on the Monday it
  STARTS -- six days apart, so ~78,600 ATP Challenger matches (2000-2026) entered the table twice;
* TML main-tour files date some events differently from Sackmann (~1,700 pairs);
* ESPN dates each match on the day it was played and names rounds "Round 2" / "1st round", so every match
  it shares with Sackmann or TML (~1,100 in 2026) escaped the exact key.

A duplicate is not harmless. Every rating model in this repository updates once per row, so a duplicated
match moves both players twice; in a walk-forward backtest the second copy is also "predicted" after the
model has already learnt its result, which is leakage that flatters the score.

The rule (fail closed: a pair that does not satisfy it is kept as two matches)
-----------------------------------------------------------------------------
Two rows are the same match only if ALL of these hold:

1. both rows have canonical ids (after the crosswalk) and the SAME ordered (winner, loser) pair on the same
   tour -- a match cannot be duplicated with the result reversed;
2. they come from DIFFERENT id systems (sackmann / tml / espn). Two rows inside one system are separate
   matches: the same two ITF players meeting in consecutive weeks is common, and a single source does not
   list one match twice under different dates;
3. their dates are within `window_days` (default 16: a Slam final is played 13 days after the Slam's
   start date, which is the date Sackmann gives it);
4. their result is identical -- the same sets AND games for each player -- or, failing that, they share the
   tournament id AND the round code (Sackmann and TML share tournament ids).

The surviving row is the one with serve statistics if only one has them, otherwise the higher-priority id
system (sackmann > tml > espn). Every dropped row is returned with the key of the row it duplicated, so the
removal is auditable.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

PRIORITY = {"sackmann": 0, "tml": 1, "espn": 2}


def _has_stats(df: pd.DataFrame) -> np.ndarray:
    if "w_svpt" not in df.columns:
        return np.zeros(len(df), dtype=bool)
    return (pd.to_numeric(df["w_svpt"], errors="coerce").fillna(0) > 0).to_numpy()


def find_cross_source_duplicates(df: pd.DataFrame, window_days: int = 16) -> pd.DataFrame:
    """Return one row per DROPPED duplicate: index_dropped, index_kept, reason."""
    need = ["tour", "tourney_date", "canonical_winner_id", "canonical_loser_id", "canonical_id_status", "id_system"]
    if any(c not in df.columns for c in need):
        return pd.DataFrame(columns=["index_dropped", "index_kept", "reason"])
    m = df[df["canonical_id_status"] == "MAPPED"]
    if m.empty:
        return pd.DataFrame(columns=["index_dropped", "index_kept", "reason"])
    d = pd.to_datetime(m["tourney_date"], errors="coerce")
    key = m["tour"].astype(str) + "|" + m["canonical_winner_id"].astype(str) + "|" + m["canonical_loser_id"].astype(str)
    # only keys that occur in more than one id system can hold a cross-source duplicate
    sys_per_key = m.groupby(key)["id_system"].nunique()
    multi = set(sys_per_key[sys_per_key > 1].index)
    sel = key.isin(multi).to_numpy()
    if not sel.any():
        return pd.DataFrame(columns=["index_dropped", "index_kept", "reason"])
    sub = m.loc[sel]
    sub_key = key[sel]
    sub_d = d[sel]
    stats = _has_stats(sub)
    cols = {c: sub[c].to_numpy() if c in sub.columns else np.full(len(sub), None)
            for c in ("id_system", "sets_w", "sets_l", "games_w", "games_l", "tourney_id", "round")}
    order = np.lexsort((sub_d.to_numpy(), sub_key.to_numpy()))
    idx = sub.index.to_numpy()[order]
    keys = sub_key.to_numpy()[order]
    dates = sub_d.to_numpy()[order]
    pos = {c: v[order] for c, v in cols.items()}
    st = stats[order]
    dropped: dict = {}
    out = []
    n = len(idx)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and keys[j + 1] == keys[i]:
            j += 1
        for a in range(i, j + 1):
            if idx[a] in dropped:
                continue
            for b in range(a + 1, j + 1):
                if idx[b] in dropped:
                    continue
                gap = (dates[b] - dates[a]) / np.timedelta64(1, "D")
                if gap > window_days:
                    break
                if pos["id_system"][a] == pos["id_system"][b]:
                    continue
                same_result = all(_eq(pos[c][a], pos[c][b]) for c in ("sets_w", "sets_l", "games_w", "games_l"))
                same_slot = _eq(pos["tourney_id"][a], pos["tourney_id"][b]) and _eq(pos["round"][a], pos["round"][b])
                if not (same_result or same_slot):
                    continue
                # keep the row carrying serve statistics; otherwise the higher-priority id system
                ka = (0 if st[a] else 1, PRIORITY.get(pos["id_system"][a], 9))
                kb = (0 if st[b] else 1, PRIORITY.get(pos["id_system"][b], 9))
                keep, drop = (a, b) if ka <= kb else (b, a)
                dropped[idx[drop]] = idx[keep]
                out.append((idx[drop], idx[keep], "same_result" if same_result else "same_tournament_round",
                            pos["id_system"][drop], pos["id_system"][keep]))
                if drop == a:
                    break
        i = j + 1
    return pd.DataFrame(out, columns=["index_dropped", "index_kept", "reason", "system_dropped", "system_kept"])


def _eq(x, y) -> bool:
    if x is None or y is None:
        return False
    try:
        if pd.isna(x) or pd.isna(y):
            return False
    except (TypeError, ValueError):
        pass
    try:
        return float(x) == float(y)
    except (TypeError, ValueError):
        return str(x) == str(y)


def drop_cross_source_duplicates(df: pd.DataFrame, window_days: int = 16) -> tuple[pd.DataFrame, pd.DataFrame]:
    """(deduplicated frame, audit of dropped rows with the match_key each one duplicated)."""
    dup = find_cross_source_duplicates(df, window_days)
    if dup.empty:
        return df, dup
    audit = dup.copy()
    if "match_key" in df.columns:
        audit["match_key_dropped"] = df.loc[dup["index_dropped"], "match_key"].to_numpy()
        audit["match_key_kept"] = df.loc[dup["index_kept"], "match_key"].to_numpy()
    if "source_label" in df.columns:
        audit["source_dropped"] = df.loc[dup["index_dropped"], "source_label"].to_numpy()
        audit["source_kept"] = df.loc[dup["index_kept"], "source_label"].to_numpy()
    return df.drop(index=dup["index_dropped"]), audit
