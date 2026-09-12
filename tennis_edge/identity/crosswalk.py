"""Crosswalk player ids between source id systems, or refuse to.

Why this exists
---------------
The canonical table carries rows from two id systems. Sackmann ids are the production universe; the
TML-format mirror uses ATP-site ids. Early in the project the two were merged naively and Zverev appeared
twice, so production ratings were restricted to Sackmann ids only. That was the right emergency fix and
the wrong permanent answer: as of 2026-09-12 the Sackmann forks are frozen (upstream is gone, and every
fork stopped within days of it), while the mirror carries ATP results three months fresher. Excluding it
means rating on four-month-old evidence.

This module builds the crosswalk the exclusion was standing in for, and it fails closed at every step:

* a foreign id is represented by the single normalised name it uses most; if its names do not collapse to
  one key the ambiguity is recorded, not resolved;
* a name key is crosswalked only when it identifies exactly ONE canonical id AND exactly ONE foreign id.
  A name shared by two players in either system maps to nothing;
* nothing is matched on surname alone, on fuzzy distance, or on a tie broken by row counts.

The output is auditable: every foreign id appears in the table with a status and a reason, so the rows
that were NOT crosswalked are as visible as the rows that were.
"""
from __future__ import annotations

import pandas as pd

from .names import normalize_name

MAPPED = "MAPPED"
AMBIGUOUS_NAME = "AMBIGUOUS_NAME"          # the name identifies more than one player in one of the systems
NO_CANONICAL = "NO_CANONICAL_MATCH"        # nobody in the canonical system uses this name
NO_NAME = "NO_USABLE_NAME"

CROSSWALK_COLUMNS = ["foreign_id_system", "foreign_id", "canonical_id", "name_key", "display_name",
                     "status", "reason", "n_foreign_rows", "n_canonical_rows"]


def player_rows(matches: pd.DataFrame, id_system: str) -> pd.DataFrame:
    """One row per (player id, name) appearance, with a normalised name key."""
    m = matches[matches["id_system"] == id_system]
    parts = []
    for idc, namec in (("winner_id", "winner_name"), ("loser_id", "loser_name")):
        p = m[[idc, namec]].rename(columns={idc: "pid", namec: "name"})
        parts.append(p)
    out = pd.concat(parts, ignore_index=True)
    out["pid"] = out["pid"].astype(str)
    out["name_key"] = out["name"].map(normalize_name)
    return out[(out["name_key"] != "") & (out["pid"] != "") & (out["pid"] != "None")]


def _dominant_names(rows: pd.DataFrame) -> pd.DataFrame:
    """pid -> its most-used name key, with how many distinct keys it used and how many rows."""
    g = rows.groupby(["pid", "name_key"]).size().rename("n").reset_index()
    g = g.sort_values(["pid", "n"], ascending=[True, False], kind="mergesort")
    top = g.drop_duplicates("pid", keep="first").rename(columns={"n": "n_rows"})
    keys = g.groupby("pid")["name_key"].nunique().rename("n_keys")
    disp = rows.drop_duplicates("pid")[["pid", "name"]].rename(columns={"name": "display_name"})
    return top.merge(keys, on="pid").merge(disp, on="pid", how="left")


def build_crosswalk(matches: pd.DataFrame, canonical: str = "sackmann", foreign: str = "tml") -> pd.DataFrame:
    can_rows, for_rows = player_rows(matches, canonical), player_rows(matches, foreign)
    if for_rows.empty:
        return pd.DataFrame(columns=CROSSWALK_COLUMNS)
    can = _dominant_names(can_rows)
    frn = _dominant_names(for_rows)

    # a name key is usable only when it belongs to exactly one player on each side
    can_key_ids = can_rows.groupby("name_key")["pid"].nunique()
    for_key_ids = for_rows.groupby("name_key")["pid"].nunique()
    unique_can = set(can_key_ids[can_key_ids == 1].index)
    unique_for = set(for_key_ids[for_key_ids == 1].index)
    can_by_key = can_rows.drop_duplicates("name_key").set_index("name_key")["pid"].to_dict()
    can_n = can_rows.groupby("name_key").size().to_dict()

    out = []
    for r in frn.itertuples(index=False):
        key = r.name_key
        if not key:
            out.append((foreign, r.pid, None, key, r.display_name, NO_NAME, "no usable name", int(r.n_rows), 0))
            continue
        if key not in unique_for:
            out.append((foreign, r.pid, None, key, r.display_name, AMBIGUOUS_NAME,
                        f"{int(for_key_ids[key])} {foreign} players share this name", int(r.n_rows), int(can_n.get(key, 0))))
            continue
        if key not in can_key_ids.index:
            out.append((foreign, r.pid, None, key, r.display_name, NO_CANONICAL,
                        f"no {canonical} player uses this name", int(r.n_rows), 0))
            continue
        if key not in unique_can:
            out.append((foreign, r.pid, None, key, r.display_name, AMBIGUOUS_NAME,
                        f"{int(can_key_ids[key])} {canonical} players share this name", int(r.n_rows), int(can_n.get(key, 0))))
            continue
        out.append((foreign, r.pid, str(can_by_key[key]), key, r.display_name, MAPPED, "", int(r.n_rows), int(can_n.get(key, 0))))
    return pd.DataFrame(out, columns=CROSSWALK_COLUMNS)


def apply_crosswalk(matches: pd.DataFrame, crosswalk: pd.DataFrame, canonical: str = "sackmann") -> pd.DataFrame:
    """Add canonical_winner_id / canonical_loser_id / canonical_id_status to every row.

    Canonical-system rows keep their own ids. Foreign rows get canonical ids only when BOTH players
    crosswalk; a row with one unmapped player is left unmapped as a whole, because half a match is not
    usable evidence about either player.
    """
    m = matches.copy()
    mp = {}
    if len(crosswalk):
        ok = crosswalk[crosswalk["status"] == MAPPED]
        mp = {(r.foreign_id_system, str(r.foreign_id)): str(r.canonical_id) for r in ok.itertuples(index=False)}

    def resolve(row_ids, row_sys):
        out = []
        for pid, sys in zip(row_ids, row_sys):
            if sys == canonical:
                out.append(str(pid))
            else:
                out.append(mp.get((sys, str(pid))))
        return out

    m["canonical_winner_id"] = resolve(m["winner_id"].astype(str), m["id_system"])
    m["canonical_loser_id"] = resolve(m["loser_id"].astype(str), m["id_system"])
    both = m["canonical_winner_id"].notna() & m["canonical_loser_id"].notna()
    m["canonical_id_status"] = ["MAPPED" if b else "UNMAPPED" for b in both]
    m.loc[~both, ["canonical_winner_id", "canonical_loser_id"]] = None
    return m


def summarise(crosswalk: pd.DataFrame, applied: pd.DataFrame | None = None) -> dict:
    s = {"foreign_players": int(len(crosswalk)),
         "by_status": {k: int(v) for k, v in crosswalk["status"].value_counts().items()} if len(crosswalk) else {}}
    if applied is not None and len(applied):
        s["rows_total"] = int(len(applied))
        s["rows_canonical_id"] = int((applied["canonical_id_status"] == "MAPPED").sum())
        foreign = applied[applied["id_system"] != "sackmann"]
        s["foreign_rows"] = int(len(foreign))
        s["foreign_rows_mapped"] = int((foreign["canonical_id_status"] == "MAPPED").sum())
    return s
