from utils import fetch_nhl_api

# ────────────────────────────────────────────────
# Specific fetch functions (minimal)
# ────────────────────────────────────────────────

def fetch_gm_tenures():
    """fetch general manager tenures within the nhl records api"""
    params = {"include": ["generalManager.id", "team.triCode"]}
    return fetch_nhl_api("https://records.nhl.com/site/api/general-manager-franchise-records", params)


def fetch_gm_bios():
    """fetch general manager bios within the nhl records api"""
    return fetch_nhl_api("https://records.nhl.com/site/api/general-manager")


def fetch_coach_tenures():
    """fetch coach tenures within the nhl records api"""

    params = {"cayenneExp": "gameTypeId=2", "include": "coach.id"}
    return fetch_nhl_api("https://records.nhl.com/site/api/coach-franchise-records", params)


def fetch_coach_bios():
    """fetch coach bios within the nhl records api"""
    return fetch_nhl_api("https://records.nhl.com/site/api/coach")
