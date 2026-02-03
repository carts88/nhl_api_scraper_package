from .utils import fetch_nhl_api

def fetch_standings(date):
    """Fetch the current NHL standings from the NHL records API
    PARAMS: 
        date: The date for which to fetch standings (format: YYYY-MM-DD)

    API: https://api-web.nhle.com/v1/standings/{date}
    """
    print(f"Fetching NHL standings")
    api_url = f'https://api-web.nhle.com/v1/standings/{date}'
    return fetch_nhl_api(api_url)

def fetch_team_schedule(team_tricode, season):
    """Fetch the schedule for a specific NHL team from the NHL records API
    PARAMS: 
        team_tricode = 3 letter team code representing the NHL team
        season: ex: 20232024

    API: https://api-web.nhle.com/v1/club-schedule-season/{team_tricode}/{season}
    """
    print(f"Fetching schedule for team: {team_tricode} - {season}")
    api_url = f'https://api-web.nhle.com/v1/club-schedule-season/{team_tricode}/{season}'
    return fetch_nhl_api(api_url)

def fetch_team_roster(team_tricode, season):
    """Fetch the roster for a specific NHL team from the NHL records API
    PARAMS: 
        team_tricode = 3 letter team code representing the NHL team
        season: ex: 20232024

    API: https://api-web.nhle.com/v1/roster/{team_tricode}/{season}
    """
    print(f"Fetching roster for team & season: {team_tricode} - {season}")
    api_url = f'https://api-web.nhle.com/v1/roster/{team_tricode}/{season}'
    return fetch_nhl_api(api_url)

def fetch_team_prospects(team_tricode):
    """Fetch the prospects for a specific NHL team from the NHL records API (note there is no season parameter)
    PARAMS: 
        team_tricode = 3 letter team code representing the NHL team
        
    API:'https://api-web.nhle.com/v1/prospects/{team_tricode}'

    """
    print(f"Fetching prospects for team & season: {team_tricode}")
    api_url = f'https://api-web.nhle.com/v1/prospects/{team_tricode}'
    return fetch_nhl_api(api_url)


def fetch_all_franchises():
    """Fetch all NHL franchises from the NHL records API"""
    print(f"Fetching all NHL franchises")
    api_url = 'https://api.nhle.com/stats/rest/en/franchise'
    return fetch_nhl_api(api_url)
