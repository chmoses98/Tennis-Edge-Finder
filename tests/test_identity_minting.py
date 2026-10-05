"""Minting a canonical id for a foreign-only player must never split one person into two rating entities."""
import pandas as pd

from tennis_edge.identity.crosswalk import MINTED, NEAR_CANONICAL, NO_CANONICAL, mint_new_players


def _matches(names):
    rows = [{"id_system": "sackmann", "winner_id": str(100 + i), "winner_name": n, "loser_id": "999", "loser_name": "Some Opponent"}
            for i, n in enumerate(names)]
    return pd.DataFrame(rows)


def _cw(entries):
    return pd.DataFrame([{"foreign_id_system": sys_, "foreign_id": fid, "canonical_id": None, "name_key": key,
                          "display_name": key.title(), "status": NO_CANONICAL, "reason": "", "n_foreign_rows": 10,
                          "n_canonical_rows": 0} for sys_, fid, key in entries])


def test_other_forms_of_an_existing_name_are_not_minted():
    # 2026-10-05, first live V2 run: each of these had been minted next to the Sackmann record of the same person
    m = _matches(["Daniel Merida Aguilar", "Murkel Alejandro Dellien Velasco", "Bu Yunchaokete"])
    cw = _cw([("espn", "espn:10239", "daniel merida"),          # second surname dropped
              ("tml", "DC48", "murkel dellien"),                # middle name and second surname dropped
              ("tml", "Y09V", "yunchaokete bu"),                # family name first vs last
              ("tml", "N3W1", "brand newplayer")])              # genuinely new: still minted
    out = mint_new_players(m, cw).set_index("name_key")
    for k in ("daniel merida", "murkel dellien", "yunchaokete bu"):
        assert out.at[k, "status"] == NEAR_CANONICAL and pd.isna(out.at[k, "canonical_id"]), k
    assert out.at["brand newplayer", "status"] == MINTED and out.at["brand newplayer", "canonical_id"] == "tml:N3W1"


def test_one_shared_token_is_not_enough_to_block_a_mint():
    m = _matches(["Daniel Evans"])
    out = mint_new_players(m, _cw([("tml", "X1", "daniel merida")])).set_index("name_key")
    assert out.at["daniel merida", "status"] == MINTED
