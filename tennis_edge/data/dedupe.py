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


# --------------------------------------------------------------------------------------------- split opponents
def _names_related(a: str, b: str) -> bool:
    """True when two normalised names are demonstrably one person written two ways: the same letters
    ("o connell" / "oconnell", "ma yexin" / "ye xin ma", "mukund sasikumar" / "sasi kumar mukund"), two or more
    shared tokens ("coleman wong" / "chak lam coleman wong"), or the same surname with a given name that is a
    prefix of the other's ("sam weissborn" / "tristan samuel weissborn")."""
    if not a or not b:
        return False
    if sorted(a.replace(" ", "")) == sorted(b.replace(" ", "")):
        return True
    ta, tb = a.split(), b.split()
    if len(set(ta) & set(tb)) >= 2:
        return True
    if ta[-1] == tb[-1] and len(ta) > 1 and len(tb) > 1:
        return any(x.startswith(y) or y.startswith(x) for x in ta[:-1] for y in tb[:-1] if min(len(x), len(y)) >= 3)
    return False


_GENERIC_EVENT_TOKENS = frozenset({"open", "ch", "cup", "tennis", "wta", "atp", "125", "250", "500", "challenger", "the",
                                    "international", "championships", "presented", "by", "itf", "w15", "w35", "w50",
                                    "w75", "w100", "m15", "m25", "1", "2", "3", "4"})


def _same_event(a, b) -> bool:
    """Two sources' names for one tournament share a distinctive token ("AITO Hangzhou Open" / "Hangzhou")."""
    from tennis_edge.identity.names import normalize_name
    ta = set(normalize_name(a).split()) - _GENERIC_EVENT_TOKENS
    tb = set(normalize_name(b).split()) - _GENERIC_EVENT_TOKENS
    return bool(ta & tb)


def drop_split_opponent_duplicates(df: pd.DataFrame, alias_ids: set, window_days: int = 7) -> tuple[pd.DataFrame, pd.DataFrame]:
    """The same match reported by two sources, where the OPPONENT carries two canonical ids. Scoped to rows of
    foreign ids bound by a human-reviewed alias (canonical_v2.3, 2026-10-06).

    `drop_cross_source_duplicates` pairs rows by the ordered canonical (winner, loser) pair, so it cannot see a
    duplicate whose opponent is split across two ids -- Sackmann's own duplicates (Coleman Wong 209409 /
    "Chak Lam Coleman Wong" 208597, Ji Sung Nam 106227 / 210079) or a minted twin ("Christopher O'Connell" tml:O483
    next to Sackmann's "Christopher Oconnell"). Accepting a reviewed alias admits that player's foreign rows, and
    with them ~17 such double-counted results (found in the 2026-10-06 live review). A row of a reviewed-alias id is
    dropped only when ALL hold (fail closed otherwise):

    * another MAPPED row from a DIFFERENT id system has the same canonical player on the SAME side (same result);
    * the dates are within `window_days`; the score is identical (sets and games, both present); the two event
      names share a distinctive token (TML's "Burnie" and Sackmann's "Launceston CH" a week apart stay two matches);
    * the two opponents' canonical ids differ but their names are demonstrably one person (`_names_related`).

    The lower-priority row (sackmann > tml > espn) is dropped. `alias_ids` = {(id system, foreign id)}."""
    cols = ["tour", "tourney_date", "tourney_name", "id_system", "winner_id", "loser_id", "winner_name", "loser_name",
            "canonical_winner_id", "canonical_loser_id", "canonical_id_status", "sets_w", "sets_l", "games_w", "games_l"]
    empty = pd.DataFrame(columns=["index_dropped", "index_kept", "player", "opponent_dropped", "opponent_kept", "reason"])
    if not alias_ids or any(c not in df.columns for c in cols):
        return df, empty
    from tennis_edge.identity.names import normalize_name
    m = df[df["canonical_id_status"] == "MAPPED"]
    d = pd.to_datetime(m["tourney_date"], errors="coerce")
    is_alias_w = [(s, str(w)) in alias_ids for s, w in zip(m["id_system"], m["winner_id"])]
    is_alias_l = [(s, str(l)) in alias_ids for s, l in zip(m["id_system"], m["loser_id"])]
    seeds = m[np.array(is_alias_w) | np.array(is_alias_l)]
    if seeds.empty:
        return df, empty
    players = set(seeds["canonical_winner_id"]) | set(seeds["canonical_loser_id"])
    pool = m[m["canonical_winner_id"].isin(players) | m["canonical_loser_id"].isin(players)]
    pool_d = d.loc[pool.index]
    out, dropped = [], set()
    for i, r in seeds.iterrows():
        if i in dropped or pd.isna(d[i]) or pd.isna(r["games_w"]) or pd.isna(r["sets_w"]):
            continue
        for side, opp_side in (("winner", "loser"), ("loser", "winner")):
            if (r["id_system"], str(r[f"{side}_id"])) not in alias_ids:
                continue
            pid = r[f"canonical_{side}_id"]
            c = pool[(pool[f"canonical_{side}_id"] == pid) & (pool["tour"] == r["tour"]) & (pool["id_system"] != r["id_system"])
                     & ((pool_d - d[i]).abs() <= pd.Timedelta(days=window_days))
                     & (pool["sets_w"] == r["sets_w"]) & (pool["sets_l"] == r["sets_l"])
                     & (pool["games_w"] == r["games_w"]) & (pool["games_l"] == r["games_l"])
                     & (pool[f"canonical_{opp_side}_id"] != r[f"canonical_{opp_side}_id"])]
            for j, q in c.iterrows():
                if j in dropped or not _names_related(normalize_name(r[f"{opp_side}_name"]), normalize_name(q[f"{opp_side}_name"])) \
                        or not _same_event(r.get("tourney_name"), q.get("tourney_name")):
                    continue
                keep, drop = (j, i) if PRIORITY.get(q["id_system"], 9) <= PRIORITY.get(r["id_system"], 9) else (i, j)
                dropped.add(drop)
                out.append({"index_dropped": drop, "index_kept": keep, "player": pid,
                            "opponent_dropped": f"{df.at[drop, opp_side + '_name']} ({df.at[drop, 'canonical_' + opp_side + '_id']}, {df.at[drop, 'id_system']})",
                            "opponent_kept": f"{df.at[keep, opp_side + '_name']} ({df.at[keep, 'canonical_' + opp_side + '_id']}, {df.at[keep, 'id_system']})",
                            "reason": "same match, opponent split across two canonical ids"})
                break
    audit = pd.DataFrame(out, columns=empty.columns)
    return df.drop(index=sorted(dropped)), audit
