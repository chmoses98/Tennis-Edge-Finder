"""ESPN scoreboard parsing.

The feed is results-only and its shape is not ours, so the risks worth pinning down are the ones that
would quietly corrupt a rating: a men's draw filed under the WTA, a doubles pair read as a singles
player, and ESPN's event-level "best of five" applied to a best-of-three qualifier.
"""
from tennis_edge.data.espn_results import parse_scoreboard


def _comp(cid, winner, loser, *, completed=True, sets=((6, 4), (6, 3))):
    return {
        "id": cid,
        "date": "2026-07-01T11:00Z",
        "status": {"type": {"state": "post" if completed else "in", "completed": completed}},
        "competitors": [
            {"id": f"{cid}w", "winner": True, "athlete": {"id": f"{cid}w", "displayName": winner},
             "linescores": [{"value": s[0]} for s in sets]},
            {"id": f"{cid}l", "winner": False, "athlete": {"id": f"{cid}l", "displayName": loser},
             "linescores": [{"value": s[1]} for s in sets]},
        ],
    }


def _payload(*groupings):
    return {"events": [{"id": "1", "name": "Wimbledon", "date": "2026-07-01T00:00:00Z",
                        "groupings": [{"grouping": {"id": str(i), "slug": slug}, "competitions": comps}
                                      for i, (slug, comps) in enumerate(groupings)]}]}


def test_combined_event_on_the_wta_board_does_not_file_men_as_wta():
    """A slam appears on both league boards carrying both draws; the grouping decides the tour."""
    payload = _payload(("mens-singles", [_comp("m1", "Alpha Man", "Beta Man")]),
                       ("womens-singles", [_comp("w1", "Gamma Woman", "Delta Woman")]))
    by_name = dict(zip(*[parse_scoreboard(payload, "wta")[c] for c in ("winner_name", "_tour")]))
    assert by_name == {"Alpha Man": "ATP", "Gamma Woman": "WTA"}
    other = parse_scoreboard(payload, "atp")
    assert dict(zip(other["winner_name"], other["_tour"])) == by_name


def test_a_board_with_no_grouping_slug_falls_back_to_the_league():
    payload = {"events": [{"id": "2", "name": "Some 250", "date": "2026-07-01T00:00:00Z",
                           "competitions": [_comp("x1", "Alpha", "Beta")]}]}
    assert list(parse_scoreboard(payload, "wta")["_tour"]) == ["WTA"]
    assert list(parse_scoreboard(payload, "atp")["_tour"]) == ["ATP"]


def test_doubles_and_unfinished_matches_are_skipped():
    payload = _payload(("mens-doubles", [_comp("d1", "A/B", "C/D")]),
                       ("mens-singles", [_comp("m2", "Alpha", "Beta", completed=False)]))
    df = parse_scoreboard(payload, "atp")
    assert df.empty
    assert df.attrs["skipped"]["doubles"] == 1 and df.attrs["skipped"]["not_final"] == 1


def test_best_of_is_left_empty_rather_than_carrying_the_events_regulation_length():
    df = parse_scoreboard(_payload(("mens-singles", [_comp("m3", "Alpha", "Beta")])), "atp")
    assert df["best_of"].isna().all()


def test_score_is_written_from_the_match_winners_perspective_with_tiebreaks():
    comp = _comp("m4", "Alpha", "Beta", sets=((7, 6), (6, 3)))
    comp["competitors"][0]["linescores"][0]["tiebreak"] = 7
    comp["competitors"][1]["linescores"][0]["tiebreak"] = 3
    df = parse_scoreboard(_payload(("mens-singles", [comp])), "atp")
    assert df.loc[0, "score"] == "7-6(3) 6-3"
