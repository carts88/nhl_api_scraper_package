from .utils import fetch_nhl_api


def fetch_player_info(player_id):
    """Fetch player information from the NHL records API
    PARAMS: 
        player_id = id representing player within the NHL's database
    """
    print(f"Fetching player information for player ID: {player_id}")
    api_url = f'https://api-web.nhle.com/v1/player/{player_id}/landing'
    return fetch_nhl_api(api_url)


def fetch_player_game_logs(player_id, season, game_type_id):
    """Fetch player game logs for a specific season from the NHL records API
    PARAMS: 
        player_id = id representing player within the NHL's database
        season: 8 digit code represent a season: ex -> 20232024
        game_type_id: 2 for regular season, 3 for playoffs
    """
    print(f"Fetching game logs for player ID: {player_id} for season: {season}")
    api_url = f'https://api-web.nhle.com/v1/player/{player_id}/game-log/{season}/{game_type_id}'
    return fetch_nhl_api(api_url)
