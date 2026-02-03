import sys
sys.stdout.reconfigure(encoding='utf-8')
from .utils import fetch_nhl_api


# REGULAR SEASON GAMES
# PART 1 = First 4 Digits of SeasonId EX: 20232024 would be 2023
# PART 2 = 02
# PART 3 = (TOTAL_LEAGUE_SIZE / 2) * 82 0001 to 1312

def get_total_teams_for_season(season):
    """
    Get the total number of teams for a given NHL season.
    """
    if season >= 20212022:
        return 32
    elif season >= 20172018:
        return 31
    elif season >= 20002001:
        return 30

def get_total_games_for_season(season):
    """
    Calculate the total number of regular season games for a given NHL season.

    Args:
        season (int): The NHL season in the format 'YYYYYYYY'.

    Returns:
        int: The total number of regular season games.
    """
    if season == 20192020:
        return 1082
    elif season == 20212022:
        return 868
    else:
        total_league_size = get_total_teams_for_season(season)
        total_games_in_season = 82
        return (total_league_size / 2) * total_games_in_season

    

def get_regular_season_game_ids(season: int):
    """
    Generate all game IDs for a given NHL season.

    Args:
        season (str): The NHL season in the format 'YYYYYYYY'. EX: 20232024

    Returns:
        list: A list of game IDs for the specified season.
    """
    part1 = str(season)[:4]
    part2 = '02'
    part3 = get_total_games_for_season(season) 

    game_ids = []
    for i in range(1, int(part3) + 1):
        game_id = f"{part1}{part2}{i:04d}"
        game_ids.append(game_id)

    return game_ids

# Fetch game specific data

def fetch_wsc_play_by_play(game_id):
    """Fetch play-by-play data for a specific game from the NHL records API"""
    print(f"Fetching play-by-play data for game ID: {game_id}")

    api_url = f'https://api-web.nhle.com/v1/wsc/play-by-play/{game_id}/'
    return fetch_nhl_api(api_url)


def fetch_play_by_play(game_id):
    """Fetch play-by-play data for a specific game from the NHL records API"""
    print(f"Fetching play-by-play data for game ID: {game_id}")

    api_url = f'https://api-web.nhle.com/v1/gamecenter/{game_id}/play-by-play'
    return fetch_nhl_api(api_url)

def fetch_shift_charts(game_id):
    """Fetch shift charts data for a specific game from the NHL records API"""
    print(f"Fetching shift charts data for game ID: {game_id}")
    params = {
        "cayenneExp": f"gameId={game_id}"
    }
    api_url =  f'https://api.nhle.com/stats/rest/en/shiftcharts'
    return fetch_nhl_api(api_url, params=params)

def fetch_box_score(game_id):
    """Fetch box score data for a specific game from the NHL records API"""
    print(f"Fetching box score data for game ID: {game_id}")
    api_url = f'https://api-web.nhle.com/v1/gamecenter/{game_id}/boxscore'
    return fetch_nhl_api(api_url)


def fetch_daily_scores(date):
    """Fetch daily scores for a specific date from the NHL records API"""
    print(f"Fetching daily scores for date: {date}")
    api_url = f'https://api-web.nhle.com/v1/score/' + date
    return fetch_nhl_api(api_url)
