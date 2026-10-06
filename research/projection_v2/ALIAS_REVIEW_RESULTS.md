# Alias review results (2026-10-06)

Machine-readable record: `ALIAS_REVIEW_DECISION.json`. Raw external evidence: `alias_review/evidence_raw/` (fetched on a GitHub runner by `.github/workflows/tennis-identity-evidence.yml`; the research sandbox cannot reach ESPN, Wikidata or the tours). Data-derived evidence: `alias_review/local_evidence.json`. Flattened per pair: `alias_review/evidence_summary.json`.

Reviewer: Claude (AI reviewer acting for the repository owner, session 2026-10-06); evidence-based, not name-based. Nothing was accepted from name similarity; no automated threshold was changed. Accepted pairs are the only new entries in `data/identity/reviewed_aliases.json` (`crosswalk_aliases`, bound by source-specific id and tour).

## Summary

| | foreign ids |
|---|---|
| reviewed (mint-twin list) | 82 |
| ACCEPTED | 77 |
| REJECTED | 2 |
| AMBIGUOUS | 1 |
| INSUFFICIENT_EVIDENCE | 2 |

## Acceptance criteria

```
(all must hold):
  A1  exactly one proposed canonical id survives on the foreign id's own tour;
  A2  no conflicting evidence: dates of birth do not disagree, nationality does not disagree (unless a reviewer
      note explains a documented source error), the foreign id is not shared by two people;
  A3  identity is established by at least one DIRECT link:
        - EXACT date of birth from a foreign-side source (ESPN athlete record for that ESPN id; the ATP-site
          database record for that TML/ATP id) equal to the canonical player's date of birth, or
        - the governing-body id: the canonical player's Wikidata ATP id (P536) equals the TML (ATP-site) id, or
        - SHARED MATCHES: the same match (same opponent, same result, same week) recorded under both ids,
      AND by a second, independent line (nationality agreement, an official WTA profile with the same date of birth,
      shared matches, or a date of birth implied by the source's own per-match ages within 22 days).
Rejected: a candidate whose date of birth or nationality contradicts the foreign record with no shared match.
Ambiguous: evidence lines contradict each other, or more than one candidate survives.
Insufficient evidence: none of the A3 links is available.
```

## Not accepted (still fail-closed)

| foreign id | name | candidate | decision | why |
|---|---|---|---|---|
| espn/espn:15260 | hu jia | ATP 213165 Jia Hu | INSUFFICIENT_EVIDENCE | no direct link (no exact date of birth, governing-body id or shared match) on both sides |
| espn/espn:2509 | lu jia jing | WTA 201582 Jing Jing Lu | REJECTED | Sackmann 201582 / WTA 313765 'Jing-Jing Lu' is born 1989-05-05 -- a different player from ESPN 2509 (born 1989-11-18); no shared match. |
| espn/espn:17802 | sara alejandra lozano avellaneda | WTA 205957 Alejandra Lozano | REJECTED | Different people: ESPN 17802 'Sara Alejandra Lozano Avellaneda' is born 2011-04-02, COL; Sackmann 205957 'Alejandra Lozano' is born 1991-06-14, MEX, last result 2010. |
| espn/espn:15544 | wang jiaqi | WTA 221181 Jiaqi Wang | AMBIGUOUS | Contradictory evidence. ESPN 15544 'Wang Jiaqi' is born 2007-09-08; Sackmann 221181 'Jiaqi Wang' is born 2002-03-25 -- yet two of ESPN's matches (Huzhou 2026 qualifying) are matches Sackmann records under 221181. Either a source has the wrong date of birth or Sackmann merged two Chinese players named Jiaqi Wang. Left fail-closed. |
| espn/espn:13444 | zhou yi | ATP 201609 Fabien Boudet | REJECTED | 201609 'Yi Miao Zhou' is a WTA player (WTA 313280, born 1991-02-07); ESPN 13444 plays ATP. (As an ATP id, 201609 is an unrelated player.) |
| espn/espn:13444 | zhou yi | ATP 207528 Yi Zhou Liu | REJECTED | 207528 'Yi Zhou Liu' (ATP) is born 1998-10-14 and last played 2017; ESPN 13444 is born 2005-03-14. |
| tml/A0JF | hernandez aguila abel | ATP 119643 Abel Hernandez Aguila | REJECTED | Rejected as an ALIAS, not as an identity: TML carries this player twice. TML H811 'Abel Hernandez-Aguila' already maps to Sackmann 119643 by exact name; A0JF ('Hernandez Aguila Abel', one row, Troyes 2022, a match Sackmann already records) is a second TML id for the same man. Binding a second id of one source to one canonical player is the duplicate identity the build refuses (apply_reviewed_aliases: 'already bound to another tml id'). No live impact. |
| tml/S0H7 | marcelo sepulveda | ATP 208095 Marcelo Sepulveda Garza | INSUFFICIENT_EVIDENCE | TML S0H7 has one row (Puerto Vallarta CH 2018) with no age, no nationality and no ATP-database record; Sackmann 208095's only row is a different match (Mexico F2 2018). Nothing links the two ids. No live impact. |

Unresolved foreign ids: espn/espn:15260 (hu jia), espn/espn:17802 (sara alejandra lozano avellaneda), espn/espn:15544 (wang jiaqi), tml/A0JF (hernandez aguila abel), tml/S0H7 (marcelo sepulveda)

## Accepted

| foreign id | name | -> canonical | DOB check | nationality | ATP id link | shared matches | live tickers | basis |
|---|---|---|---|---|---|---|---|---|
| espn/espn:5712 | bai zhuoxuan | WTA 222296 Zhuoxuan Bai | EXACT (2002-11-16 / 2002-11-16) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:3797 | cui jie | ATP 200666 Jie Cui | EXACT (1998-01-24 / 1998-01-24) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:13617 | dang yiming | WTA 222330 Yiming Dang | EXACT (2004-08-30 / 2004-08-30) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality |
| espn/espn:10239 | daniel merida | ATP 210017 Daniel Merida Aguilar | EXACT (2004-09-26 / 2004-09-26) | MATCH | UNAVAILABLE | 14 | 16 | exact date of birth; 14 shared match(es); nationality |
| espn/espn:14709 | diego dedura | ATP 212309 Diego Dedura Palomero | EXACT (2008-03-12 / 2008-03-12) | MATCH | UNAVAILABLE | 5 | 0 | exact date of birth; 5 shared match(es); nationality |
| espn/espn:5256 | feng shuo | WTA 215937 Shuo Feng | EXACT (1998-01-15 / 1998-01-15) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality; official WTA profile date of birth |
| espn/espn:12315 | gao xinyu | WTA 214386 Xinyu Gao | EXACT (1997-11-21 / 1997-11-21) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:3149 | guo hanyu | WTA 215250 Hanyu Guo | EXACT (1998-05-18 / 1998-05-18) | MATCH | UNAVAILABLE | 4 | 0 | exact date of birth; 4 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:5490 | guo meiqi | WTA 216162 Meiqi Guo | EXACT (2000-01-09 / 2000-01-09) | MATCH | UNAVAILABLE | 2 | 0 | exact date of birth; 2 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:4546 | irene burillo | WTA 213706 Irene Burillo Escorihuela | EXACT (1997-07-23 / 1997-07-23) | MATCH | UNAVAILABLE | 3 | 0 | exact date of birth; 3 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:4389 | iva primorac pavicic | WTA 206248 Iva Primorac | EXACT (1996-04-10 / 1996-04-10) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality; official WTA profile date of birth |
| espn/espn:13680 | li zongyu | WTA 252493 Zongyu Li | EXACT (2003-05-27 / 2003-05-27) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:2509 | lu jia jing | WTA 203288 Jia Jing Lu | EXACT (1989-11-18 / 1989-11-18) | MATCH | UNAVAILABLE | 2 | 0 | Flagged ambiguity (two Sackmann Lus). ESPN's athlete record for 2509 is 'Lu Jia-Jing', born 1989-11-18 in Liaoning, CHN. Sackmann 203288 'Jia Jing Lu' and the o |
| espn/espn:15421 | qu yihan | WTA 264086 Yihan Qu | EXACT (2009-03-22 / 2009-03-22) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:13681 | ren yufei | WTA 260913 Yufei Ren | EXACT (2006-04-11 / 2006-04-11) | MATCH | UNAVAILABLE | 2 | 0 | exact date of birth; 2 shared match(es); nationality |
| espn/espn:10073 | shang juncheng | ATP 209992 Juncheng Shang | EXACT (2005-02-02 / 2005-02-02) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:15422 | shao yushan | WTA 269253 Yushan Shao | EXACT (2008-12-26 / 2008-12-26) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:2567 | sun fajing | ATP 111806 Fajing Sun | EXACT (1996-10-03 / 1996-10-03) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:3478 | tang qianhui | WTA 215043 Qianhui Tang | EXACT (2000-09-10 / 2000-09-10) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality; official WTA profile date of birth |
| espn/espn:2856 | te rigele | ATP 144751 Rigele Te | EXACT (1997-10-09 / 1997-10-09) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:13708 | tian fangran | WTA 221885 Fangran Tian | EXACT (2003-08-10 / 2003-08-10) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:3992 | wang meiling | WTA 216062 Meiling Wang | EXACT (2000-02-22 / 2000-02-22) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:3155 | wang xiyu | WTA 216016 Xiyu Wang | EXACT (2001-03-28 / 2001-03-28) | MATCH | UNAVAILABLE | 4 | 0 | exact date of birth; 4 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:13765 | wang yuhan | WTA 264205 Yuhan Wang | EXACT (2007-06-21 / 2007-06-21) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:6189 | wei sijia | WTA 221096 Sijia Wei | EXACT (2003-12-05 / 2003-12-05) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality |
| espn/espn:15424 | wei zhang qian | WTA 268781 Zhang Qian Wei | UNAVAILABLE (2008-01-30 / -) | MATCH | UNAVAILABLE | 2 | 0 | 2 shared match(es); nationality |
| espn/espn:2875 | wu yibing | ATP 200059 Yibing Wu | EXACT (1999-10-14 / 1999-10-14) | MATCH | UNAVAILABLE | 4 | 0 | exact date of birth; 4 shared match(es); nationality |
| espn/espn:13482 | xiao linang | ATP 209038 Linang Xiao | EXACT (2000-03-18 / 2000-03-18) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:4943 | yang yidi | WTA 215820 Yidi Yang | EXACT (1999-12-21 / 1999-12-21) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:13682 | yao xinxin | WTA 252587 Xinxin Yao | EXACT (2003-10-20 / 2003-10-20) | MATCH | UNAVAILABLE | 2 | 0 | exact date of birth; 2 shared match(es); nationality |
| espn/espn:17856 | ye shiyu | WTA 264085 Shiyu Ye | EXACT (2007-04-20 / 2007-04-20) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality |
| espn/espn:2603 | you xiaodi | WTA 214646 Xiaodi You | EXACT (1996-05-12 / 1996-05-12) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:12587 | younes lalami | ATP 207794 Younes Lalami Laaroussi | EXACT (2001-04-18 / 2001-04-18) | CONFLICT | UNAVAILABLE | 1 | 0 | ESPN lists citizenship 'Laos' (LAO) and birthplace Montreal for 12587, which contradicts every other source; the date of birth (2001-04-18) equals Sackmann 2077 |
| espn/espn:2916 | yuan yue | WTA 206294 Yue Yuan | EXACT (1998-09-25 / 1998-09-25) | MATCH | UNAVAILABLE | 12 | 0 | exact date of birth; 12 shared match(es); nationality |
| espn/espn:15423 | zhang ruien | WTA 263869 Ruien Zhang | EXACT (2008-04-27 / 2008-04-27) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:707 | zhang shuai | WTA 201533 Shuai Zhang | EXACT (1989-01-21 / 1989-01-21) | MATCH | UNAVAILABLE | 5 | 0 | exact date of birth; 5 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:15462 | zhang tianhui | ATP 212221 Tianhui Zhang | EXACT (2006-02-19 / 2006-02-19) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality |
| espn/espn:2594 | zhang ying | WTA 213947 Ying Zhang | EXACT (1996-04-15 / 1996-04-15) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality; official WTA profile date of birth |
| espn/espn:3024 | zhang zhizhen | ATP 111190 Zhizhen Zhang | EXACT (1996-10-16 / 1996-10-16) | MATCH | UNAVAILABLE | 6 | 0 | exact date of birth; 6 shared match(es); nationality |
| espn/espn:6048 | zheng qinwen | WTA 221012 Qinwen Zheng | EXACT (2002-10-08 / 2002-10-08) | MATCH | UNAVAILABLE | 2 | 0 | exact date of birth; 2 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:2608 | zheng wushuang | WTA 213821 Wushuang Zheng | EXACT (1998-11-29 / 1998-11-29) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality; official WTA profile date of birth |
| espn/espn:13444 | zhou yi | ATP 212044 Yi Zhou | EXACT (2005-03-14 / 2005-03-14) | MATCH | UNAVAILABLE | 0 | 0 | Flagged ambiguity (three Sackmann Zhous). ESPN 13444 is an ATP (men's) record: 'Zhou Yi', born 2005-03-14, Beijing, CHN. Sackmann ATP 212044 'Yi Zhou' is born 2 |
| espn/espn:2780 | zhu lin | WTA 202684 Lin Zhu | EXACT (1994-01-28 / 1994-01-28) | MATCH | UNAVAILABLE | 0 | 0 | exact date of birth; nationality; official WTA profile date of birth |
| tml/A09P | alafia ayeni | ATP 200366 Olukayode Alafia Damina Ayeni | AGE_CONSISTENT (- / 1999-08-10) | MATCH | UNAVAILABLE | 62 | 0 | 62 shared match(es); nationality; date of birth implied by per-match ages |
| tml/R772 | albert ramos vinolas | ATP 105077 Albert Ramos | EXACT (1988-01-17 / 1988-01-17) | MATCH | MATCH | 874 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 874 shared match(es); nationality |
| tml/HH32 | alejandro hoyos | ATP 200253 Alejandro Hoyos Franco | AGE_CONSISTENT (- / 1999-09-17) | MATCH | UNAVAILABLE | 4 | 0 | 4 shared match(es); nationality; date of birth implied by per-match ages |
| tml/J468 | alexandru jecan | ATP 121497 Mircea Alexandru Jecan | AGE_CONSISTENT (- / 1988-06-02) | MATCH | UNAVAILABLE | 1 | 0 | 1 shared match(es); nationality; date of birth implied by per-match ages |
| tml/A0G8 | amr elsayed | ATP 209871 Amr Elsayed Abdou Ahmed Mohamed | AGE_CONSISTENT (- / 1999-03-04) | MATCH | UNAVAILABLE | 1 | 0 | 1 shared match(es); nationality; date of birth implied by per-match ages |
| tml/H0C9 | arklon huertas del pino cordova | ATP 207736 Arklon Huertas Del Pino | EXACT (1994-07-16 / 1994-07-16) | MATCH | UNAVAILABLE | 25 | 0 | exact date of birth; 25 shared match(es); nationality |
| tml/R438 | augusto ricciardi | ATP 108943 Augusto Ricciardi Castelli | EXACT (1979-07-15 / 1979-07-15) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality |
| tml/T0FN | benjamin torres | ATP 210301 Benjamin Ignacio Torres Fernandez | AGE_CONSISTENT (- / 2003-10-12) | MATCH | UNAVAILABLE | 1 | 0 | 1 shared match(es); nationality; date of birth implied by per-match ages |
| tml/H0LS | courte heremana | ATP 213705 Heremana Courte | UNAVAILABLE (- / 2007-01-01) | MATCH | UNAVAILABLE | 1 | 0 | 1 shared match(es); nationality |
| tml/S0GM | daniel salazar | ATP 202369 Daniel Salazar Martinez | AGE_CONSISTENT (- / 2001-03-21) | MATCH | UNAVAILABLE | 4 | 0 | 4 shared match(es); nationality; date of birth implied by per-match ages |
| tml/D0LJ | diego dedura | ATP 212309 Diego Dedura Palomero | EXACT (2008-03-12 / 2008-03-12) | MATCH | UNAVAILABLE | 49 | 0 | exact date of birth; 49 shared match(es); nationality |
| tml/RC31 | eduardo russi assumpcao | ATP 111796 Eduardo Russi | AGE_CONSISTENT (- / 1995-02-09) | MATCH | MATCH | 2 | 0 | ATP id on the canonical player's Wikidata item equals the foreign id; 2 shared match(es); nationality; date of birth implied by per-match ages |
| tml/A0F9 | emiliano aguilera | ATP 212510 Emiliano Aguilera Guerrero | AGE_CONSISTENT (- / 2003-02-11) | MATCH | UNAVAILABLE | 1 | 0 | 1 shared match(es); nationality; date of birth implied by per-match ages |
| tml/F512 | favel freyre | ATP 108918 Favel Antonio Freyre Perdomo | UNAVAILABLE (- / 1986-02-26) | MATCH | UNAVAILABLE | 3 | 0 | 3 shared match(es); nationality |
| tml/V0HQ | felipe virgili | ATP 212854 Felipe Virgili Berini | AGE_CONSISTENT (- / 2005-01-20) | MATCH | UNAVAILABLE | 1 | 0 | 1 shared match(es); nationality; date of birth implied by per-match ages |
| tml/M0WY | guto miguel | ATP 213036 Luis Guto Miguel | AGE_CONSISTENT (- / 2009-02-26) | MATCH | UNAVAILABLE | 10 | 0 | 10 shared match(es); nationality; date of birth implied by per-match ages |
| tml/H409 | hira lal | ATP 110825 Hira Lal Rahman | UNAVAILABLE (- / 1971-01-21) | MATCH | UNAVAILABLE | 6 | 0 | 6 shared match(es); nationality |
| tml/P0I5 | ignacio parisca romera | ATP 212306 Ignacio Parisca | EXACT (2005-08-20 / 2005-08-20) | MATCH | UNAVAILABLE | 2 | 0 | exact date of birth; 2 shared match(es); nationality |
| tml/CA33 | inigo cervantes | ATP 105438 Inigo Cervantes Huegun | EXACT (1989-11-30 / 1989-11-30) | MATCH | MATCH | 303 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 303 shared match(es); nationality |
| tml/CN08 | jordan correia | ATP 144756 Jordan Correia Passos Do Carmo | AGE_CONSISTENT (- / 1997-07-05) | MATCH | UNAVAILABLE | 1 | 0 | 1 shared match(es); nationality; date of birth implied by per-match ages |
| tml/PG56 | jorge panta | ATP 106410 Jorge Brian Panta Herreros | EXACT (1995-07-22 / 1995-07-22) | MATCH | MATCH | 20 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 20 shared match(es); nationality |
| tml/L0HN | luca lemaitre | ATP 212507 Luca Lemaitre Vilchis | AGE_CONSISTENT (- / 2005-02-18) | MATCH | UNAVAILABLE | 0 | 0 | date of birth implied by the source's per-match ages agrees within 22 days; nationality |
| tml/CA39 | luis javier cuellar | ATP 108981 Luis Javier Cuellar Contreras | EXACT (1988-02-10 / 1988-02-10) | MATCH | UNAVAILABLE | 1 | 0 | exact date of birth; 1 shared match(es); nationality |
| tml/Z363 | marcelo zormann | ATP 110774 Marcelo Zormann Da Silva | UNAVAILABLE (- / 1996-06-10) | UNAVAILABLE | UNAVAILABLE | 19 | 0 | TML Z363 carries no age or nationality and has no ATP-database record, so no date of birth or nationality can be compared -- but 19 of its 21 matches (2013-2023 |
| tml/DC48 | murkel dellien | ATP 123961 Murkel Alejandro Dellien Velasco | EXACT (1997-09-16 / 1997-09-16) | MATCH | MATCH | 183 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 183 shared match(es); nationality |
| tml/S923 | nasir sherazi | ATP 108846 Syed Nasir Sherazi | EXACT (1980-02-24 / 1980-02-24) | MATCH | UNAVAILABLE | 4 | 0 | exact date of birth; 4 shared match(es); nationality |
| tml/RB00 | ricardo rodriguez pace | ATP 106175 Ricardo Rodriguez | EXACT (1993-04-28 / 1993-04-28) | MATCH | MATCH | 52 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 52 shared match(es); nationality |
| tml/CF88 | roberto cid subervi | ATP 106232 Roberto Cid | EXACT (1993-08-30 / 1993-08-30) | MATCH | MATCH | 132 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 132 shared match(es); nationality |
| tml/SF89 | rubin statham | ATP 104907 Jose Rubin Statham | EXACT (1987-04-25 / 1987-04-25) | MATCH | MATCH | 186 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 186 shared match(es); nationality |
| tml/E224 | victor estrella burgos | ATP 103607 Victor Estrella | EXACT (1980-08-02 / 1980-08-02) | MATCH | MATCH | 416 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 416 shared match(es); nationality |
| tml/PA97 | vijay sundar prashanth | ATP 104822 N Vijay Sundar Prashanth | EXACT (1986-10-27 / 1986-10-27) | MATCH | MATCH | 27 | 0 | exact date of birth; ATP id on the canonical player's Wikidata item equals the foreign id; 27 shared match(es); nationality |
| tml/SM71 | vinayak sharma kaza | ATP 105737 Kaza Vinayak Sharma | AGE_CONSISTENT (- / 1991-03-28) | MATCH | UNAVAILABLE | 2 | 0 | 2 shared match(es); nationality; date of birth implied by per-match ages |
| tml/L0CK | younes lalami | ATP 207794 Younes Lalami Laaroussi | EXACT (2001-04-18 / 2001-04-18) | MATCH | UNAVAILABLE | 4 | 0 | exact date of birth; 4 shared match(es); nationality |
| tml/Y09V | yunchaokete bu | ATP 207352 Bu Yunchaokete | EXACT (2002-01-19 / 2002-01-19) | MATCH | UNAVAILABLE | 157 | 16 | exact date of birth; 157 shared match(es); nationality |

## Kalshi-name queue (prior 9-entry `alias_review_queue`) and Mimi Xu

| Kalshi name | tour | decision | why |
|---|---|---|---|
| Mimi Xu | WTA | INSUFFICIENT_EVIDENCE | No governing-body record reachable from this review ties the name 'Mimi Xu' to the registry's Mingge Xu (259685, GBR, born 2007-10-02): the official WTA lookup and Wikidata search returned no player record for 'Mimi Xu'. Left PENDING_REVIEW, as instructed. |
| Alex Hernandez | ATP | REJECTED | Every candidate is a different person: a different given name (Alejandro Hernandez b.1977 MEX, Antonio J Ayala Hernandez b.1995 ESP, Angel Hernandez b.? VEN). The Kalshi name stays unmapped (no history), which is correct. |
| Andres Pereiro Lopez | ATP | REJECTED | Every candidate is a different person: a different given name (Andres Lopez b.1984 PAR, Allan Lopez b.1973 ESA, Aramis Lopez b.1972 CUB, Alberto Gonzalez Lopez b.1977 ESP, Angel Garcia Lopez b.1981 MEX). The Kalshi name stays unmapped (no history), which is correct. |
| Xin Zhou | ATP | REJECTED | Every candidate is a different person: a different given name (Xinmu Zhou b.2001, Xian Yao Zhou b.2001 CHN, Xiao Feng Zhou b.2007 TPE). The Kalshi name stays unmapped (no history), which is correct. |
| Ailish Garcia Fernandez | WTA | REJECTED | Every candidate is a different person: a different given name (Anna Maria Fernandez b.1960 USA, Adriana Fernandez b.1987 GUA, Ana Ruiz Fernandez b.1989 ESP, Arletis Fernandez b.1990 CUB, Almudena Sanz Llaneza Fernandez b.1991 ESP). The Kalshi name stays unmapped (no history), which is correct. |
| Baotong Xu | WTA | REJECTED | Every candidate is a different person: a different given name (Bao Yi Xu b.1992 CHN). The Kalshi name stays unmapped (no history), which is correct. |
| Bella Bergqvist Larsson | WTA | INSUFFICIENT_EVIDENCE | The registry's Bella Bergkvist Larsson (SWE, born 2006-03-09) is confirmed by the official WTA profile 331422 under the spelling 'Bergkvist'. Kalshi spells it 'Bergqvist' and exposes no date of birth or id, and the registry also holds a different Swede, Wilma Bergqvist. Very probably the same player, but nothing on Kalshi's side identifies her: left PENDING. |
| Jiarui Sun | WTA | REJECTED | Every candidate is a different person: a different given name (Junlu Sun b.? CHN). The Kalshi name stays unmapped (no history), which is correct. |
| Maria Valentina Pop | WTA | REJECTED | Every candidate is a different person: a different given name (Mara Cristiana Pop b.2000 ROU). The Kalshi name stays unmapped (no history), which is correct. |
| aoyi li | WTA | REJECTED | Every candidate is a different person: a different given name (Ann Li b.2000 USA, Augusta Maxima Li b.? TWN). The Kalshi name stays unmapped (no history), which is correct. |

## Live coverage

Pending: measured on the first production RUN TENNIS after merge.
