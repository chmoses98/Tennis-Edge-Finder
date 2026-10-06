"""Reviewed foreign-id aliases (2026-10-06): an explicit allowlist that can only fill a gap, never widen matching.

Fixtures reproduce the real cases from the mint-twin review (research/projection_v2/ALIAS_REVIEW_DECISION.json):
the Lu Jia Jing and Zhou Yi ambiguities, a Chinese family-name-first reversal (Zheng Qinwen), a compound Spanish /
Latin surname (Murkel Dellien), an old inactive namesake (Augusto Ricciardi), and the Merida / Dellien / Bu class
that was minted as a second rating entity during V2 verification."""
import inspect
import json
from datetime import date

import pandas as pd
import pytest

from tennis_edge.identity import crosswalk as X
from tennis_edge.identity import kalshi_map as K
from tennis_edge.identity import reviewed_aliases as R

SACKMANN = [  # (id, name) -- each plays one match against a common opponent
    ("201582", "Jing Jing Lu"), ("203288", "Jia Jing Lu"),
    ("201609", "Yi Miao Zhou"), ("207528", "Yi Zhou Liu"), ("212044", "Yi Zhou"),
    ("221012", "Qinwen Zheng"), ("123961", "Murkel Alejandro Dellien Velasco"),
    ("210017", "Daniel Merida Aguilar"), ("207352", "Bu Yunchaokete"),
    ("108943", "Augusto Ricciardi Castelli"), ("104925", "Novak Djokovic"),
]
FOREIGN = [  # (system, id, name)
    ("espn", "espn:2509", "Lu Jia Jing"), ("espn", "espn:13444", "Zhou Yi"), ("espn", "espn:6048", "Zheng Qinwen"),
    ("espn", "espn:10239", "Daniel Merida"), ("tml", "DC48", "Murkel Dellien"), ("tml", "Y09V", "Yunchaokete Bu"),
    ("tml", "R438", "Augusto Ricciardi"), ("tml", "D643", "Novak Djokovic"), ("tml", "N3W1", "Brand Newplayer"),
]


ATP_IDS = {"123961", "210017", "207352", "108943", "104925", "tml", "espn:10239", "DC48", "Y09V", "R438", "D643", "N3W1"}


def _tour(pid):
    return "ATP" if (pid in ATP_IDS or pid.startswith("tml")) else "WTA"


def _matches():
    rows = [{"id_system": "sackmann", "tour": _tour(pid), "winner_id": pid, "winner_name": n, "loser_id": "999", "loser_name": "Some Opponent"}
            for pid, n in SACKMANN]
    rows += [{"id_system": s, "tour": _tour(fid), "winner_id": fid, "winner_name": n, "loser_id": f"{s}-opp-{_tour(fid)}", "loser_name": "Other Opponent"}
             for s, fid, n in FOREIGN]
    # a foreign row where the reviewed player LOST: orientation must survive the alias
    rows.append({"id_system": "espn", "tour": "WTA", "winner_id": "espn:6048", "winner_name": "Zheng Qinwen", "loser_id": "espn:13444", "loser_name": "Zhou Yi"})
    rows.append({"id_system": "tml", "tour": "ATP", "winner_id": "D643", "winner_name": "Novak Djokovic", "loser_id": "DC48", "loser_name": "Murkel Dellien"})
    return pd.DataFrame(rows)


def _crosswalk(m):
    cw = pd.concat([X.build_crosswalk(m, foreign=s) for s in ("tml", "espn")], ignore_index=True)
    return X.mint_new_players(m, cw)


def _alias(sysname, fid, fname, cid, cname, status="ACCEPTED", tour="WTA"):
    return {"foreign_system": sysname, "foreign_id": fid, "foreign_name": fname, "canonical_id": cid,
            "canonical_name": cname, "review_status": status, "tour": tour}


ACCEPTED = [_alias("espn", "espn:6048", "zheng qinwen", "221012", "qinwen zheng"),
            _alias("tml", "DC48", "murkel dellien", "123961", "murkel alejandro dellien velasco", tour="ATP"),
            _alias("tml", "Y09V", "yunchaokete bu", "207352", "bu yunchaokete", tour="ATP"),
            _alias("espn", "espn:10239", "daniel merida", "210017", "daniel merida aguilar", tour="ATP")]
NOT_ACCEPTED = [_alias("espn", "espn:2509", "lu jia jing", "203288", "jia jing lu", status="AMBIGUOUS"),
                _alias("espn", "espn:13444", "zhou yi", "212044", "yi zhou", status="AMBIGUOUS"),
                _alias("tml", "R438", "augusto ricciardi", "108943", "augusto ricciardi castelli", status="INSUFFICIENT_EVIDENCE", tour="ATP")]


@pytest.fixture
def alias_file(tmp_path):
    def write(entries):
        p = tmp_path / "reviewed_aliases.json"
        json.dump({"schema_version": 2, "aliases": [], "crosswalk_aliases": entries}, open(p, "w"))
        return str(p)
    return write


def _apply(entries, path):
    m = _matches()
    cw = _crosswalk(m)
    out, problems = X.apply_reviewed_aliases(m, cw, R.load_crosswalk_aliases(path))
    return m, cw, out.set_index(["foreign_id_system", "foreign_id"]), problems


def test_before_review_every_mint_twin_is_unmapped_and_nothing_is_minted_for_them():
    cw = _crosswalk(_matches()).set_index(["foreign_id_system", "foreign_id"])
    for key in [("espn", "espn:2509"), ("espn", "espn:13444"), ("espn", "espn:6048"), ("espn", "espn:10239"),
                ("tml", "DC48"), ("tml", "Y09V"), ("tml", "R438")]:
        assert cw.loc[key, "status"] == X.NEAR_CANONICAL and pd.isna(cw.loc[key, "canonical_id"]), key
    assert cw.loc[("tml", "N3W1"), "status"] == X.MINTED            # a genuinely new player is still minted


def test_accepted_alias_resolves_only_to_the_approved_canonical_id(alias_file):
    _m, _cw, out, problems = _apply(None, alias_file(ACCEPTED + NOT_ACCEPTED))
    assert problems == []
    assert out.loc[("espn", "espn:6048"), "status"] == X.REVIEWED_ALIAS and out.loc[("espn", "espn:6048"), "canonical_id"] == "221012"
    assert out.loc[("tml", "DC48"), "canonical_id"] == "123961"           # compound Latin surname
    assert out.loc[("tml", "Y09V"), "canonical_id"] == "207352"           # family name first
    assert out.loc[("espn", "espn:10239"), "canonical_id"] == "210017"    # second surname dropped


@pytest.mark.parametrize("key", [("espn", "espn:2509"), ("espn", "espn:13444"), ("tml", "R438")])
def test_ambiguous_and_insufficient_candidates_stay_unmapped(alias_file, key):
    """Lu Jia Jing (two Sackmann Lus), Zhou Yi (three Sackmann Zhous), Augusto Ricciardi (namesake last seen 2005)."""
    _m, _cw, out, _p = _apply(None, alias_file(ACCEPTED + NOT_ACCEPTED))
    assert out.loc[key, "status"] == X.NEAR_CANONICAL and pd.isna(out.loc[key, "canonical_id"])


def test_rejected_or_pending_entries_are_inert(alias_file):
    assert R.load_crosswalk_aliases(alias_file(NOT_ACCEPTED)) == {}


def test_foreign_ids_are_source_specific(alias_file):
    """An alias for ESPN id X never binds a TML id X (or the same NAME in another system)."""
    path = alias_file([_alias("tml", "espn:6048", "zheng qinwen", "221012", "qinwen zheng")])
    _m, _cw, out, problems = _apply(None, path)
    assert out.loc[("espn", "espn:6048"), "status"] == X.NEAR_CANONICAL
    assert problems and "not in the data" in problems[0]["problem"]


def test_alias_never_overwrites_an_automated_identity(alias_file):
    # Djokovic's TML id is MAPPED by exact name; a reviewed alias pointing it elsewhere is refused
    path = alias_file([_alias("tml", "D643", "novak djokovic", "212044", "yi zhou", tour="ATP")])
    _m, _cw, out, problems = _apply(None, path)
    assert out.loc[("tml", "D643"), "status"] == X.MAPPED and out.loc[("tml", "D643"), "canonical_id"] == "104925"
    assert "never overwrites" in problems[0]["problem"]


def test_wrong_or_stale_names_fail_closed(alias_file):
    path = alias_file([_alias("espn", "espn:2509", "lu jia jing", "201582", "jia jing lu"),        # 201582 is JING jing lu
                       _alias("espn", "espn:13444", "zhou yi miao", "201609", "yi miao zhou")])     # not the id's name
    _m, _cw, out, problems = _apply(None, path)
    assert out.loc[("espn", "espn:2509"), "status"] == X.NEAR_CANONICAL
    assert out.loc[("espn", "espn:13444"), "status"] == X.NEAR_CANONICAL
    assert len(problems) == 2


def test_nonexistent_canonical_is_refused(alias_file):
    _m, _cw, out, problems = _apply(None, alias_file([_alias("espn", "espn:6048", "zheng qinwen", "999999", "qinwen zheng")]))
    assert out.loc[("espn", "espn:6048"), "status"] == X.NEAR_CANONICAL and "not in sackmann WTA" in problems[0]["problem"]


def test_sackmann_ids_repeat_across_tours_so_aliases_are_tour_bound(alias_file):
    """Sackmann 212044 is an ATP man ("Yi Zhou") AND a WTA woman (Katharina Gerlach in the real players files).
    A WTA foreign id may never bind the ATP player with that number, nor an alias without a tour."""
    m = _matches()
    m = pd.concat([m, pd.DataFrame([{"id_system": "sackmann", "tour": "ATP", "winner_id": "212044", "winner_name": "Yi Zhou",
                                     "loser_id": "998", "loser_name": "Atp Opponent"}])], ignore_index=True)
    m.loc[(m.id_system == "sackmann") & (m.winner_id == "212044") & (m.winner_name == "Yi Zhou") & (m.tour == "WTA"), "winner_name"] = "Katharina Gerlach"
    cw = _crosswalk(m)
    wrong_tour = R.load_crosswalk_aliases(alias_file([_alias("espn", "espn:13444", "zhou yi", "212044", "yi zhou", tour="WTA")]))
    out, problems = X.apply_reviewed_aliases(m, cw, wrong_tour)
    assert out.set_index("foreign_id").loc["espn:13444", "status"] != X.REVIEWED_ALIAS and problems
    atp_alias = R.load_crosswalk_aliases(alias_file([_alias("espn", "espn:13444", "zhou yi", "212044", "yi zhou", tour="ATP")]))
    out, problems = X.apply_reviewed_aliases(m, cw, atp_alias)       # the ESPN id plays WTA: refused
    assert out.set_index("foreign_id").loc["espn:13444", "status"] != X.REVIEWED_ALIAS and "plays on ['WTA']" in problems[0]["problem"]
    with pytest.raises(R.CrosswalkAliasError):
        R.load_crosswalk_aliases(alias_file([{**_alias("espn", "espn:6048", "zheng qinwen", "221012", "qinwen zheng"), "tour": None}]))


def test_duplicate_identity_cannot_be_created(alias_file):
    # two ESPN ids for one Sackmann player: the whole file is refused, not silently half-applied
    with pytest.raises(R.CrosswalkAliasError):
        R.load_crosswalk_aliases(alias_file([_alias("espn", "espn:6048", "zheng qinwen", "221012", "qinwen zheng"),
                                             _alias("espn", "espn:13444", "zhou yi", "221012", "qinwen zheng")]))
    with pytest.raises(R.CrosswalkAliasError):     # one foreign id, two canonical ids
        R.load_crosswalk_aliases(alias_file([_alias("espn", "espn:2509", "lu jia jing", "201582", "jing jing lu"),
                                             _alias("espn", "espn:2509", "lu jia jing", "203288", "jia jing lu")]))
    with pytest.raises(R.CrosswalkAliasError):     # an alias may never target a minted id
        R.load_crosswalk_aliases(alias_file([_alias("espn", "espn:6048", "zheng qinwen", "tml:N3W1", "brand newplayer")]))


def test_alias_target_already_held_by_a_same_system_id_is_refused(alias_file):
    # the TML id D643 is already MAPPED to 104925; another TML id may not also become 104925
    m = _matches()
    m = pd.concat([m, pd.DataFrame([{"id_system": "tml", "tour": "ATP", "winner_id": "XX99", "winner_name": "Nole Djokovic",
                                     "loser_id": "tml-opp-ATP", "loser_name": "Other Opponent"}])], ignore_index=True)
    cw = _crosswalk(m)
    out, problems = X.apply_reviewed_aliases(m, cw, R.load_crosswalk_aliases(
        alias_file([_alias("tml", "XX99", "nole djokovic", "104925", "novak djokovic", tour="ATP")])))
    assert out.set_index("foreign_id").loc["XX99", "status"] != X.REVIEWED_ALIAS
    assert "already bound" in problems[0]["problem"]


def test_alias_does_not_mint_and_mint_rules_are_unchanged(alias_file):
    _m, cw, out, _p = _apply(None, alias_file(ACCEPTED))
    assert not out["canonical_id"].dropna().astype(str).str.startswith(("espn:2509", "espn:6048", "tml:DC48", "tml:Y09V")).any()
    # every row the alias file does not name is exactly what the automated steps produced
    named = {(a["foreign_system"], a["foreign_id"]) for a in ACCEPTED}
    before = cw.set_index(["foreign_id_system", "foreign_id"])
    for key in before.index:
        if key not in named:
            assert before.loc[key, "status"] == out.loc[key, "status"]


def test_no_threshold_was_loosened():
    assert R.ALIAS_CONFIDENCE == 0.95
    src = inspect.getsource(K.KalshiPlayerMapper)
    assert '"confidence": 0.9, "name": nm' in src and '"confidence": 0.85' in src
    assert "timedelta(days=730)" in src and "timedelta(days=548)" in src
    rel = inspect.getsource(X._TokenIndex.related)
    assert "range(2, len(toks) + 1)" in rel and "len(f) < 2" in rel


def test_orientation_is_preserved(alias_file):
    m, _cw, out, _p = _apply(None, alias_file(ACCEPTED))
    applied = X.apply_crosswalk(m, out.reset_index())
    r = applied[(applied.id_system == "tml") & (applied.loser_id == "DC48")].iloc[0]
    assert r.canonical_winner_id == "104925" and r.canonical_loser_id == "123961"     # Dellien LOST, still the loser
    r = applied[(applied.id_system == "espn") & (applied.loser_id == "espn:13444")].iloc[0]
    assert r.canonical_id_status == "UNMAPPED"          # Zhou Yi unresolved: the whole match stays out


def test_disabling_the_file_reproduces_the_prior_crosswalk(alias_file):
    """Historical evidence stays reproducible: no aliases == the pre-review crosswalk, byte for byte."""
    m = _matches()
    cw = _crosswalk(m)
    same, problems = X.apply_reviewed_aliases(m, cw, {})
    assert problems == [] and same.equals(cw)


def test_kalshi_name_of_a_reviewed_foreign_id_maps_at_alias_confidence_and_keeps_sides(alias_file):
    path = alias_file(ACCEPTED + NOT_ACCEPTED)
    states = {"WTA": {"players": {"221012": {"name": "Qinwen Zheng", "last_date": "2026-04-21"},
                                  "212044": {"name": "Yi Zhou", "last_date": "2026-05-11"},
                                  "203288": {"name": "Jia Jing Lu", "last_date": "2026-04-27"},
                                  "201582": {"name": "Jing Jing Lu", "last_date": "2026-04-06"}}},
              "ATP": {"players": {"123961": {"name": "Murkel Alejandro Dellien Velasco", "last_date": "2026-05-11"}}}}
    mp = K.KalshiPlayerMapper.__new__(K.KalshiPlayerMapper)
    K.KalshiPlayerMapper.__init__(mp, states, cache_path="/nonexistent/cache.json")
    mp.aliases = R.load(path)
    a = mp.resolve("WTA", "Zheng Qinwen", today=date(2026, 10, 6))
    b = mp.resolve("WTA", "Zhou Yi", today=date(2026, 10, 6))
    c = mp.resolve("WTA", "Lu Jia Jing", today=date(2026, 10, 6))
    d = mp.resolve("ATP", "Murkel Dellien", today=date(2026, 10, 6))
    assert a["status"] == "MAPPED" and a["player_id"] == "221012" and a["confidence"] == R.ALIAS_CONFIDENCE
    assert b["status"] == "UNMAPPED" and c["status"] == "UNMAPPED"
    assert d["player_id"] == "123961"
    assert mp.resolve("ATP", "Zheng Qinwen", today=date(2026, 10, 6))["status"] == "UNMAPPED"   # tour-specific


def test_a_name_claimed_for_two_players_maps_to_neither(alias_file):
    path = alias_file([_alias("espn", "espn:1", "zhang ying", "213947", "ying zhang"),
                       _alias("tml", "Z1", "zhang ying", "999", "ying zhang")])
    assert ("WTA", "zhang ying") not in R.load(path)


def test_production_alias_file_is_consistent():
    """The committed file loads without error and every accepted entry carries evidence and a reviewer."""
    acc = R.load_crosswalk_aliases()
    for (_s, _f), a in acc.items():
        assert a.get("evidence") and a.get("reviewed_at") and a.get("reviewer"), a
        assert a.get("tour") in ("ATP", "WTA")
    obj = json.load(open(R.DEFAULT_PATH))
    mimi = [a for a in obj["aliases"] if a.get("source_name") == "Mimi Xu"]
    assert len(mimi) == 1                                   # never deleted to tidy the metrics


def test_alias_never_bypasses_the_namesake_check(alias_file):
    """An accepted alias name ("Zhang Ying" -> 213947) must fail closed while the registry holds ANOTHER player whose
    name has the same tokens in another order: the exact-name path would have called that ambiguous too."""
    path = alias_file([_alias("espn", "espn:2594", "zhang ying", "213947", "ying zhang")])
    states = {"WTA": {"players": {"213947": {"name": "Ying Zhang", "last_date": "2026-04-27"},
                                  "299999": {"name": "Zhang Ying", "last_date": "2026-05-01"}}}}
    mp = K.KalshiPlayerMapper.__new__(K.KalshiPlayerMapper)
    K.KalshiPlayerMapper.__init__(mp, states, cache_path="/nonexistent/cache.json")
    mp.aliases = R.load(path)
    # "Zhang Ying" is an exact registry name here, so the alias is not even consulted
    assert mp.resolve("WTA", "Zhang Ying", today=date(2026, 10, 6))["player_id"] == "299999"
    states["WTA"]["players"]["299999"]["name"] = "Ying Zhang"            # now two "Ying Zhang"s and no "Zhang Ying"
    K.KalshiPlayerMapper.__init__(mp, states, cache_path="/nonexistent/cache.json")
    mp.aliases = R.load(path)
    r = mp.resolve("WTA", "Zhang Ying", today=date(2026, 10, 6))
    assert r["status"] == "AMBIGUOUS" and r["player_id"] is None


def test_an_alias_never_renames_the_canonical_player():
    """Regression (found in the 2026-10-06 dry run): once ESPN's "Zheng Qinwen" rows were bound to Sackmann 221012, the
    rating state named her after the newest row, and Kalshi's "Qinwen Zheng" stopped resolving. The canonical spelling
    must win; a minted (foreign-only) player keeps its foreign name."""
    from tennis_edge.models.state import player_names
    m = pd.DataFrame([
        {"id_system": "sackmann", "winner_id": "221012", "winner_name": "Qinwen Zheng", "loser_id": "1", "loser_name": "Opp One"},
        {"id_system": "espn", "winner_id": "221012", "winner_name": "Zheng Qinwen", "loser_id": "espn:9", "loser_name": "New Player"},
        {"id_system": "espn", "winner_id": "1", "winner_name": "Opp One", "loser_id": "221012", "loser_name": "Zheng Qinwen"}])
    n = player_names(m)
    assert n["221012"] == "Qinwen Zheng" and n["espn:9"] == "New Player"
