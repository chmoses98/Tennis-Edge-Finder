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

from itertools import combinations

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
        ok = crosswalk[crosswalk["status"].isin([MAPPED, "MINTED_NEW_PLAYER", "REVIEWED_ALIAS"])]
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


MINTED = "MINTED_NEW_PLAYER"               # no canonical player could be this person; a new canonical id is minted
NEAR_CANONICAL = "NEAR_CANONICAL_MATCH"    # a canonical player shares surname + first initial: maybe an alias


def _surname_initial(key: str) -> tuple[str, str] | None:
    toks = key.split()
    if len(toks) < 2:
        return None
    return toks[-1], toks[0][:1]


class _TokenIndex:
    """Canonical names as token sets, for the 'same person, other form of the name' test below."""

    def __init__(self, keys):
        self.sets = set()
        self.post: dict = {}
        for k in keys:
            toks = frozenset(str(k).split())
            if len(toks) < 2:
                continue
            self.sets.add(toks)
            for t in toks:
                self.post.setdefault(t, set()).add(toks)

    def related(self, key: str) -> bool:
        """True when some canonical name, as a SET of tokens (order ignored), contains this name or is contained
        in it, with at least two tokens shared: "Daniel Merida" / "Daniel Merida Aguilar" (second surname),
        "Murkel Dellien" / "Murkel Alejandro Dellien Velasco" (middle name, second surname), "Yunchaokete Bu" /
        "Bu Yunchaokete" (family name first). Such a player may already have a rating; minting would split it."""
        f = frozenset(key.split())
        if len(f) < 2:
            return False
        posts = [self.post.get(t, set()) for t in f]
        if all(posts) and set.intersection(*posts):                      # canonical name contains every token
            return True
        toks = sorted(f)
        for r in range(2, len(toks) + 1):                               # canonical name is a subset (>= 2 tokens)
            for combo in combinations(toks, r):
                if frozenset(combo) in self.sets:
                    return True
        return False


def mint_new_players(matches: pd.DataFrame, crosswalk: pd.DataFrame, canonical: str = "sackmann") -> pd.DataFrame:
    """Give players who exist ONLY in a foreign system their own canonical id -- or refuse to.

    Since the Sackmann forks froze, every player who turned professional afterwards appears only in TML or
    ESPN rows. The crosswalk (correctly) cannot map them to a Sackmann id, so before this pass their
    matches were excluded from every rating: a new player had no rating however many matches they won.

    A foreign player is minted a canonical id (``<system>:<foreign id>``) only when ALL of these hold:

    * the crosswalk found NO canonical player with the name (status NO_CANONICAL_MATCH), and the name is
      unique inside its own system;
    * no canonical player shares the surname AND the first initial. "Pyotr Nesterov" next to an existing
      "Petr Nesterov" is a possible transliteration of one person, so it is left UNMAPPED
      (NEAR_CANONICAL_MATCH) for human review instead of becoming a second rating entity;
    * no canonical player's name contains this name or is contained in it as a set of tokens (>= 2 shared;
      order ignored). Added 2026-10-05 after the first live V2 run: "Daniel Merida" (ESPN), "Murkel Dellien" and
      "Yunchaokete Bu" (TML) had been minted although Sackmann rates them as "Daniel Merida Aguilar", "Murkel
      Alejandro Dellien Velasco" and "Bu Yunchaokete" -- each became a second rating entity for one person.
      They are NEAR_CANONICAL_MATCH now: unmapped until a person accepts an alias.
    * if the same name is unmatched in TWO foreign systems (a new player seen by both ESPN and TML), both
      ids collapse onto ONE minted id -- otherwise the same newcomer would be rated twice. If either system
      has two players with that name, nobody is minted.
    """
    if crosswalk.empty:
        return crosswalk
    can_rows = player_rows(matches, canonical)
    near = set()
    for k in can_rows["name_key"].unique():
        si = _surname_initial(k)
        if si:
            near.add(si)
    tokens = _TokenIndex(can_rows["name_key"].unique())
    cw = crosswalk.copy()
    cand = cw[cw["status"] == NO_CANONICAL]
    # a name minted in one system must not be ambiguous in any other foreign system
    per_name = cand.groupby("name_key")
    preferred = {"tml": 0, "espn": 1}
    for name_key, grp in per_name:
        si = _surname_initial(name_key)
        if si is None:
            continue
        if si in near:
            cw.loc[grp.index, "status"] = NEAR_CANONICAL
            cw.loc[grp.index, "reason"] = "a canonical player shares surname and first initial; possible alias -- review"
            continue
        if tokens.related(name_key):
            cw.loc[grp.index, "status"] = NEAR_CANONICAL
            cw.loc[grp.index, "reason"] = "a canonical name contains / is contained in this one (token set); possible alias -- review"
            continue
        if grp.groupby("foreign_id_system")["foreign_id"].nunique().max() > 1:
            continue
        anchor = grp.sort_values("foreign_id_system", key=lambda s: s.map(lambda x: preferred.get(x, 9))).iloc[0]
        new_id = f"{anchor.foreign_id_system}:{anchor.foreign_id}"
        cw.loc[grp.index, "canonical_id"] = new_id
        cw.loc[grp.index, "status"] = MINTED
        cw.loc[grp.index, "reason"] = "foreign-only player; minted canonical id"
    return cw


REVIEWED_ALIAS = "REVIEWED_ALIAS"          # a person accepted (system, foreign id) -> canonical id, with evidence
#: only an id the automated steps left UNMAPPED may be bound by a reviewed alias; a mapped/minted id never is
_REVIEWABLE = (NEAR_CANONICAL, NO_CANONICAL, AMBIGUOUS_NAME)


def apply_reviewed_aliases(matches: pd.DataFrame, crosswalk: pd.DataFrame, aliases: dict,
                           canonical: str = "sackmann") -> tuple[pd.DataFrame, list]:
    """Bind foreign ids a PERSON accepted (data/identity/reviewed_aliases.json `crosswalk_aliases`) -- or refuse.

    `aliases` is {(foreign system, foreign id): entry} (reviewed_aliases.load_crosswalk_aliases). Matching is by the
    SOURCE-SPECIFIC id only, never by name; names are only cross-checked. An entry is refused (and listed in the
    returned problems, the id staying unmapped) when:

    * its foreign id is not in the crosswalk, or the crosswalk already MAPPED / MINTED it -- an alias never
      overwrites an automated identity, it can only fill a gap the automation refused to fill;
    * the foreign id's name in the data is no longer the name the reviewer saw (the id was reused / data changed);
    * the canonical id does not exist in the canonical system, or no longer carries the reviewed name;
    * the canonical id is already the target of ANOTHER foreign id of the same system (a duplicate identity).
    """
    problems: list = []
    if crosswalk.empty or not aliases:
        return crosswalk, problems
    cw = crosswalk.copy()
    # Sackmann ATP and WTA ids share one numeric range (212044 is an ATP man AND a WTA woman), so every check is
    # made inside the alias's tour: the foreign id must play on that tour and the canonical id must exist there.
    tours: dict = {}
    can_names: dict = {}
    for idc, namec in (("winner_id", "winner_name"), ("loser_id", "loser_name")):
        sub = matches[[idc, namec, "id_system", "tour"]].drop_duplicates()
        for pid, nm, sysname, tour in sub.itertuples(index=False):
            if sysname == canonical:
                can_names.setdefault((tour, str(pid)), set()).add(normalize_name(nm))
            else:
                tours.setdefault((sysname, str(pid)), set()).add(tour)
    taken = set()
    for r in cw.itertuples(index=False):
        if r.status in (MAPPED, MINTED, REVIEWED_ALIAS) and r.canonical_id is not None:
            for t in tours.get((r.foreign_id_system, str(r.foreign_id)), ()):
                taken.add((r.foreign_id_system, t, str(r.canonical_id)))
    idx = {(r.foreign_id_system, str(r.foreign_id)): i for i, r in zip(cw.index, cw.itertuples(index=False))}
    for (sysname, fid), a in sorted(aliases.items()):
        cid, tour = str(a["canonical_id"]), a.get("tour")
        i = idx.get((sysname, fid))
        if i is None:
            problems.append({"foreign": f"{sysname}/{fid}", "problem": "foreign id not in the data"}); continue
        row = cw.loc[i]
        if row["status"] not in _REVIEWABLE:
            if not (row["status"] == MAPPED and str(row["canonical_id"]) == cid):
                problems.append({"foreign": f"{sysname}/{fid}", "problem": f"already {row['status']} -> {row['canonical_id']}; a reviewed alias never overwrites it"})
            continue
        if normalize_name(a.get("foreign_name") or "") != row["name_key"]:
            problems.append({"foreign": f"{sysname}/{fid}", "problem": f"name in data {row['name_key']!r} != reviewed {a.get('foreign_name')!r}"}); continue
        if tours.get((sysname, fid)) != {tour}:
            problems.append({"foreign": f"{sysname}/{fid}", "problem": f"foreign id plays on {sorted(tours.get((sysname, fid), []))}, alias is for {tour!r}"}); continue
        if (tour, cid) not in can_names:
            problems.append({"foreign": f"{sysname}/{fid}", "problem": f"canonical {cid} not in {canonical} {tour}"}); continue
        if normalize_name(a.get("canonical_name") or "") not in can_names[(tour, cid)]:
            problems.append({"foreign": f"{sysname}/{fid}", "problem": f"canonical {tour} {cid} no longer named {a.get('canonical_name')!r}"}); continue
        if (sysname, tour, cid) in taken:
            problems.append({"foreign": f"{sysname}/{fid}", "problem": f"canonical {tour} {cid} already bound to another {sysname} id"}); continue
        cw.loc[i, "canonical_id"] = cid
        cw.loc[i, "status"] = REVIEWED_ALIAS
        cw.loc[i, "reason"] = f"human-reviewed alias ({a.get('decision_ref') or 'reviewed_aliases.json'})"
        taken.add((sysname, tour, cid))
    return cw, problems
