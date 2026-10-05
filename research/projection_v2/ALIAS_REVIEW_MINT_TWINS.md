# Alias review: players refused a minted id (2026-10-05)

These foreign (TML / ESPN) players were minted a NEW canonical id by `canonical_v2` (PR #17) although a Sackmann
player with another form of the same name exists. The guard now refuses (NEAR_CANONICAL_MATCH); their foreign rows
are excluded from ratings, exactly as before #17, until a person accepts an alias in `data/identity/reviewed_aliases.json`
or the crosswalk. Nothing here is mapped automatically.

| foreign system | foreign id | foreign name | Sackmann candidate(s) (id, name, last result) |
|---|---|---|---|
| espn | espn:5712 | bai zhuoxuan | `222296` zhuoxuan bai (2026-04-13) |
| espn | espn:3797 | cui jie | `200666` jie cui (2026-05-18) |
| espn | espn:13617 | dang yiming | `222330` yiming dang (2026-04-27) |
| espn | espn:10239 | daniel merida | `210017` daniel merida aguilar (2026-06-01) |
| espn | espn:14709 | diego dedura | `212309` diego dedura palomero (2026-06-01) |
| espn | espn:5256 | feng shuo | `215937` shuo feng (2025-09-01) |
| espn | espn:12315 | gao xinyu | `214386` xinyu gao (2026-04-27) |
| espn | espn:3149 | guo hanyu | `215250` hanyu guo (2026-04-27) |
| espn | espn:5490 | guo meiqi | `216162` meiqi guo (2026-04-27) |
| espn | espn:15260 | hu jia | `213165` jia hu (2025-08-18) |
| espn | espn:4546 | irene burillo | `213706` irene burillo escorihuela (2026-04-20) |
| espn | espn:4389 | iva primorac pavicic | `206248` iva primorac (2026-03-23) |
| espn | espn:13680 | li zongyu | `252493` zongyu li (2026-04-13) |
| espn | espn:2509 | lu jia jing | `201582` jing jing lu (2026-04-06); `203288` jia jing lu (2026-04-27) |
| espn | espn:15421 | qu yihan | `264086` yihan qu (2025-10-13) |
| espn | espn:13681 | ren yufei | `260913` yufei ren (2026-04-27) |
| espn | espn:17802 | sara alejandra lozano avellaneda | `205957` alejandra lozano (2010-04-19) |
| espn | espn:10073 | shang juncheng | `209992` juncheng shang (2026-02-23) |
| espn | espn:15422 | shao yushan | `269253` yushan shao (2026-04-27) |
| espn | espn:2567 | sun fajing | `111806` fajing sun (2026-06-01) |
| espn | espn:3478 | tang qianhui | `215043` qianhui tang (2025-07-28) |
| espn | espn:2856 | te rigele | `144751` rigele te (2026-05-11) |
| espn | espn:13708 | tian fangran | `221885` fangran tian (2026-04-06) |
| espn | espn:15544 | wang jiaqi | `221181` jiaqi wang (2026-04-27) |
| espn | espn:3992 | wang meiling | `216062` meiling wang (2026-04-27) |
| espn | espn:3155 | wang xiyu | `216016` xiyu wang (2026-04-27) |
| espn | espn:13765 | wang yuhan | `264205` yuhan wang (2026-04-27) |
| espn | espn:6189 | wei sijia | `221096` sijia wei (2026-04-27) |
| espn | espn:15424 | wei zhang qian | `268781` zhang qian wei (2026-04-27) |
| espn | espn:2875 | wu yibing | `200059` yibing wu (2026-05-25) |
| espn | espn:13482 | xiao linang | `209038` linang xiao (2026-05-18) |
| espn | espn:4943 | yang yidi | `215820` yidi yang (2026-04-27) |
| espn | espn:13682 | yao xinxin | `252587` xinxin yao (2026-04-27) |
| espn | espn:17856 | ye shiyu | `264085` shiyu ye (2026-04-27) |
| espn | espn:2603 | you xiaodi | `214646` xiaodi you (2026-04-27) |
| espn | espn:12587 | younes lalami | `207794` younes lalami laaroussi (2026-05-25) |
| espn | espn:2916 | yuan yue | `206294` yue yuan (2026-04-27) |
| espn | espn:15423 | zhang ruien | `263869` ruien zhang (2026-04-06) |
| espn | espn:707 | zhang shuai | `201533` shuai zhang (2026-04-21) |
| espn | espn:15462 | zhang tianhui | `212221` tianhui zhang (2026-06-01) |
| espn | espn:2594 | zhang ying | `213947` ying zhang (2026-04-27) |
| espn | espn:3024 | zhang zhizhen | `111190` zhizhen zhang (2026-06-01) |
| espn | espn:6048 | zheng qinwen | `221012` qinwen zheng (2026-04-21) |
| espn | espn:2608 | zheng wushuang | `213821` wushuang zheng (2026-04-27) |
| espn | espn:13444 | zhou yi | `201609` yi miao zhou (2013-08-26); `207528` yi zhou liu (2017-07-24); `212044` yi zhou (2026-05-11) |
| espn | espn:2780 | zhu lin | `202684` lin zhu (2026-04-27) |
| tml | A09P | alafia ayeni | `200366` olukayode alafia damina ayeni (2026-06-01) |
| tml | R772 | albert ramos vinolas | `105077` albert ramos (2025-10-06) |
| tml | HH32 | alejandro hoyos | `200253` alejandro hoyos franco (2024-04-29) |
| tml | J468 | alexandru jecan | `121497` mircea alexandru jecan (2024-09-02) |
| tml | A0G8 | amr elsayed | `209871` amr elsayed abdou ahmed mohamed (2026-05-11) |
| tml | H0C9 | arklon huertas del pino cordova | `207736` arklon huertas del pino (2026-05-11) |
| tml | R438 | augusto ricciardi | `108943` augusto ricciardi castelli (2005-07-15) |
| tml | T0FN | benjamin torres | `210301` benjamin ignacio torres fernandez (2026-01-12) |
| tml | H0LS | courte heremana | `213705` heremana courte (2024-12-30) |
| tml | S0GM | daniel salazar | `202369` daniel salazar martinez (2026-06-01) |
| tml | D0LJ | diego dedura | `212309` diego dedura palomero (2026-06-01) |
| tml | RC31 | eduardo russi assumpcao | `111796` eduardo russi (2017-10-30) |
| tml | A0F9 | emiliano aguilera | `212510` emiliano aguilera guerrero (2024-11-25) |
| tml | F512 | favel freyre | `108918` favel antonio freyre perdomo (2007-08-20) |
| tml | V0HQ | felipe virgili | `212854` felipe virgili berini (2026-05-18) |
| tml | M0WY | guto miguel | `213036` luis guto miguel (2026-05-11) |
| tml | A0JF | hernandez aguila abel | `119643` abel hernandez aguila (2024-07-01) |
| tml | H409 | hira lal | `110825` hira lal rahman (1995-10-28) |
| tml | P0I5 | ignacio parisca romera | `212306` ignacio parisca (2026-05-18) |
| tml | CA33 | inigo cervantes | `105438` inigo cervantes huegun (2024-09-02) |
| tml | CN08 | jordan correia | `144756` jordan correia passos do carmo (2025-03-17) |
| tml | PG56 | jorge panta | `106410` jorge brian panta herreros (2023-11-06) |
| tml | L0HN | luca lemaitre | `212507` luca lemaitre vilchis (2025-08-12) |
| tml | CA39 | luis javier cuellar | `108981` luis javier cuellar contreras (2008-04-28) |
| tml | S0H7 | marcelo sepulveda | `208095` marcelo sepulveda garza (2018-05-14) |
| tml | Z363 | marcelo zormann | `110774` marcelo zormann da silva (2026-03-02) |
| tml | DC48 | murkel dellien | `123961` murkel alejandro dellien velasco (2026-05-11) |
| tml | S923 | nasir sherazi | `108846` syed nasir sherazi (1999-05-15) |
| tml | RB00 | ricardo rodriguez pace | `106175` ricardo rodriguez (2025-11-24) |
| tml | CF88 | roberto cid subervi | `106232` roberto cid (2026-05-11) |
| tml | SF89 | rubin statham | `104907` jose rubin statham (2024-10-28) |
| tml | E224 | victor estrella burgos | `103607` victor estrella (2019-10-07) |
| tml | PA97 | vijay sundar prashanth | `104822` n vijay sundar prashanth (2025-08-11) |
| tml | SM71 | vinayak sharma kaza | `105737` kaza vinayak sharma (2022-03-21) |
| tml | L0CK | younes lalami | `207794` younes lalami laaroussi (2026-05-25) |
| tml | Y09V | yunchaokete bu | `207352` bu yunchaokete (2026-06-01) |
