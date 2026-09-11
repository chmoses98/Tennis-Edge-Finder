"""Candidate sources for ACTUAL first-ball truth, as a declarative probe catalogue.

This file is a research artefact, not a production source list. Nothing here is trusted until
scripts/firstball/probe_sources.py has probed it from a GitHub Actions runner and the evidence has been
written into docs/FIRST_BALL_SOURCES.md. One successful request is NOT evidence that an undocumented
endpoint is production-safe; the prober therefore repeats every probe across rounds separated in time and
records status, latency, payload shape, rate-limit headers and robots.txt for every host.

`answers` records which of the mission's five questions a source could plausibly answer, so that a source
that only gives a schedule is never mistaken for one that proves play began:
  1 actual_start        explicit actual start / first point timestamp
  2 first_event_ts      timestamp of the first live scoring event
  3 live_state          current match state proving play began
  4 status_transition   event status transitions (scheduled -> in progress -> finished)
  5 progression         point/game/set progression with timestamps
"""
from __future__ import annotations

from dataclasses import dataclass, field

UA_BROWSERISH = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
                 "Chrome/124.0 Safari/537.36 tennis-edge-finder/0.2 (research; github.com/chmoses98/tennis-edge-finder)")


@dataclass(frozen=True)
class Candidate:
    id: str
    name: str
    host_class: str                  # official_tour | official_event | broadcaster | aggregator | exchange
    url: str                         # may contain {date_ymd} {date_iso} {date_dash}
    levels: tuple                    # tours/levels the source is expected to cover
    answers: tuple                   # subset of (1,2,3,4,5) above
    auth: str = "none"
    accept: str = "application/json"
    notes: str = ""
    referer: str = ""
    needs_browser_ua: bool = True
    expect: str = "json"             # json | html | unknown


C = Candidate
CANDIDATES: tuple[Candidate, ...] = (
    # ---------------------------------------------------------------- broadcaster (ESPN public site API)
    C("espn_site_atp_scoreboard", "ESPN site API - ATP scoreboard", "broadcaster",
      "https://site.api.espn.com/apis/site/v2/sports/tennis/atp/scoreboard?dates={date_ymd}",
      ("ATP", "GRAND_SLAM"), (1, 3, 4), notes="undocumented but long-lived public JSON behind espn.com"),
    C("espn_site_wta_scoreboard", "ESPN site API - WTA scoreboard", "broadcaster",
      "https://site.api.espn.com/apis/site/v2/sports/tennis/wta/scoreboard?dates={date_ymd}",
      ("WTA", "GRAND_SLAM"), (1, 3, 4)),
    C("espn_core_atp_events", "ESPN core API - ATP events", "broadcaster",
      "https://sports.core.api.espn.com/v2/sports/tennis/leagues/atp/events?dates={date_ymd}",
      ("ATP",), (1, 4)),
    C("espn_site_leagues", "ESPN site API - tennis leagues list", "broadcaster",
      "https://site.api.espn.com/apis/site/v2/sports/tennis/atp/teams", ("ATP",), (), notes="coverage probe only"),

    # ---------------------------------------------------------------- official tour
    C("atp_live_scores", "ATP Tour - live scores feed", "official_tour",
      "https://www.atptour.com/en/-/www/scores/live", ("ATP", "GRAND_SLAM"), (3, 4, 5),
      referer="https://www.atptour.com/en/scores/current"),
    C("atp_current_scores", "ATP Tour - current tournament scores", "official_tour",
      "https://www.atptour.com/en/-/www/scores/current", ("ATP",), (3, 4, 5),
      referer="https://www.atptour.com/en/scores/current"),
    C("protennislive_oop", "protennislive - official order of play / live", "official_tour",
      "https://www.protennislive.com/posting/livescores.json", ("ATP", "CHALLENGER"), (3, 4),
      notes="ATP/Challenger official posting site"),
    C("wta_live_matches", "WTA - live matches", "official_tour",
      "https://api.wtatennis.com/tennis/live/matches", ("WTA",), (3, 4, 5)),
    C("wta_matches_by_date", "WTA - matches by date", "official_tour",
      "https://api.wtatennis.com/tennis/matches?date={date_dash}", ("WTA",), (1, 4)),
    C("itf_livescores_mt", "ITF - live scores, men's world tennis tour", "official_tour",
      "https://www.itftennis.com/tennis/api/LiveScoresApi/GetLiveScores?circuitCode=MT&searchString=&skip=0&take=100",
      ("ITF_M", "QUALIFYING"), (3, 4, 5), referer="https://www.itftennis.com/en/live-scores/"),
    C("itf_livescores_wt", "ITF - live scores, women's world tennis tour", "official_tour",
      "https://www.itftennis.com/tennis/api/LiveScoresApi/GetLiveScores?circuitCode=WT&searchString=&skip=0&take=100",
      ("ITF_W", "QUALIFYING"), (3, 4, 5), referer="https://www.itftennis.com/en/live-scores/"),
    C("itf_calendar", "ITF - tournament calendar API", "official_tour",
      "https://www.itftennis.com/tennis/api/TournamentApi/GetCalendar?circuitCode=MT&searchString=&skip=0&take=50",
      ("ITF_M",), (4,), referer="https://www.itftennis.com/en/tournament-calendar/"),

    # ---------------------------------------------------------------- official grand-slam scoreboards
    C("usopen_live", "US Open - live scores feed", "official_event",
      "https://www.usopen.org/en_US/scores/feed/live.json", ("GRAND_SLAM",), (3, 4, 5)),
    C("wimbledon_live", "Wimbledon - live scores feed", "official_event",
      "https://www.wimbledon.com/en_GB/scores/feed/live.json", ("GRAND_SLAM",), (3, 4, 5)),
    C("ausopen_live", "Australian Open - live scores", "official_event",
      "https://ausopen.com/api/live-scores", ("GRAND_SLAM",), (3, 4, 5)),
    C("rolandgarros_live", "Roland-Garros - live scores", "official_event",
      "https://www.rolandgarros.com/api/en-us/live-scores", ("GRAND_SLAM",), (3, 4, 5)),

    # ---------------------------------------------------------------- aggregators
    C("sofascore_live", "SofaScore - live tennis events", "aggregator",
      "https://api.sofascore.com/api/v1/sport/tennis/events/live",
      ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W", "QUALIFYING", "DOUBLES"), (1, 3, 4, 5),
      referer="https://www.sofascore.com/", notes="deepest coverage; check terms + anti-bot"),
    C("sofascore_scheduled", "SofaScore - scheduled tennis events for a date", "aggregator",
      "https://api.sofascore.com/api/v1/sport/tennis/scheduled-events/{date_dash}",
      ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W", "QUALIFYING", "DOUBLES"), (1, 4),
      referer="https://www.sofascore.com/"),
    C("livescore_tennis", "livescore.com public react API", "aggregator",
      "https://prod-public-api.livescore.com/v1/api/react/date/tennis/{date_ymd}/0",
      ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W"), (3, 4)),
    C("thesportsdb_tennis", "TheSportsDB - events on a day", "aggregator",
      "https://www.thesportsdb.com/api/v1/json/3/eventsday.php?d={date_dash}&s=Tennis",
      ("ATP", "WTA"), (1, 4), notes="free public key 3"),
    C("tennisexplorer_html", "tennisexplorer.com - results page", "aggregator",
      "https://www.tennisexplorer.com/matches/?type=all&year={year}&month={month}&day={day}",
      ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W"), (4,), expect="html", accept="text/html"),
    C("flashscore_feed", "flashscore data feed", "aggregator",
      "https://local-global.flashscore.ninja/2/x/feed/f_2_0_1_en_1", ("ATP", "WTA"), (3, 4),
      expect="unknown", accept="*/*", referer="https://www.flashscore.com/"),
    C("tennis_api_io", "tennisapi.io public endpoint", "aggregator",
      "https://api.tennisapi.io/v1/matches/live", ("ATP", "WTA"), (3,), notes="existence unverified"),

    # ---------------------------------------------------------------- exchange (corroboration only)
    C("kalshi_exchange_status", "Kalshi exchange status (corroboration only)", "exchange",
      "https://api.elections.kalshi.com/trade-api/v2/exchange/status", ("ALL",), (),
      notes="EXCHANGE_TRUTH; may corroborate but never be sole sports-truth authority"),
)

# ---------------------------------------------------------------------------------------------------
# Round 2, added after the 2026-09-11T19:36Z probe. That round established: ESPN's site API is reachable
# and rich; ATP, SofaScore and flashscore block runner IPs (Cloudflare / 401); the ITF API root works but
# the live-scores controller name was wrong; several guessed slam feeds are stale paths. These candidates
# chase the gaps that matter -- above all ITF/Challenger/qualifying, which nothing reachable covers yet.
ROUND2: tuple[Candidate, ...] = (
    C("espn_leagues", "ESPN core - every tennis league ESPN carries", "broadcaster",
      "https://sports.core.api.espn.com/v2/sports/tennis/leagues?limit=100", ("ALL",), (),
      notes="does ESPN carry Challenger/ITF at all?"),
    C("espn_site_atp_chal", "ESPN site API - ATP Challenger scoreboard", "broadcaster",
      "https://site.api.espn.com/apis/site/v2/sports/tennis/atp-challenger/scoreboard?dates={date_ymd}",
      ("CHALLENGER",), (1, 3, 4)),
    C("espn_site_itf_men", "ESPN site API - ITF men scoreboard", "broadcaster",
      "https://site.api.espn.com/apis/site/v2/sports/tennis/itf-men/scoreboard?dates={date_ymd}",
      ("ITF_M",), (1, 3, 4)),
    C("itf_livescores_page", "ITF live-scores page (to discover the real API path)", "official_tour",
      "https://www.itftennis.com/en/live-scores/", ("ITF_M", "ITF_W", "QUALIFYING"), (3, 4),
      expect="html", accept="text/html"),
    C("itf_livescore_api_v2", "ITF - LiveScoresApi alternate controller", "official_tour",
      "https://www.itftennis.com/tennis/api/LiveScoresApi/GetLiveScores?circuitCode=MT",
      ("ITF_M",), (3, 4), referer="https://www.itftennis.com/en/live-scores/"),
    C("itf_matches_api", "ITF - MatchesApi live scores", "official_tour",
      "https://www.itftennis.com/tennis/api/MatchesApi/GetLiveScores?circuitCode=MT",
      ("ITF_M",), (3, 4), referer="https://www.itftennis.com/en/live-scores/"),
    C("protennislive_home", "protennislive home (to discover its feed)", "official_tour",
      "https://www.protennislive.com/", ("ATP", "CHALLENGER"), (3, 4), expect="html", accept="text/html"),
    C("tennisexplorer_live", "tennisexplorer live page", "aggregator",
      "https://www.tennisexplorer.com/live/", ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W", "QUALIFYING"),
      (3, 4), expect="html", accept="text/html", notes="robots.txt allows /live/"),
    C("sofascore_www_host", "SofaScore via www host", "aggregator",
      "https://www.sofascore.com/api/v1/sport/tennis/events/live",
      ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W"), (1, 3, 4, 5), referer="https://www.sofascore.com/"),
    C("sofascore_app_host", "SofaScore via app host", "aggregator",
      "https://api.sofascore.app/api/v1/sport/tennis/events/live",
      ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W"), (1, 3, 4, 5), referer="https://www.sofascore.com/"),
)

CANDIDATES = CANDIDATES + ROUND2

HOSTS = tuple(sorted({c.url.split("/")[2] for c in CANDIDATES}))
