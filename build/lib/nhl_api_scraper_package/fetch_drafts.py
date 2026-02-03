from .utils import fetch_nhl_api


# ======== helper functions ========
def parse_for_original_owner(history: str):
    """
    Extract the original owning team from NHL API's teamPickHistory field.
    
    Handles two main formats:
      - "NYI (from BUF)"          → "BUF"
      - "NYI-ANA-BUF"             → "BUF"
      - Also works with single team "TOR" → "TOR"
    
    Returns None if format is unrecognizable.
    """
    if not history or not isinstance(history, str):
        return None
    
    history = history.strip()
    
    # Format 1: "Something (from XXX)"
    if "from" in history:
        # Look for the 3-letter code inside (from ... )
        start = history.rfind("(from") 
        if start != -1:
            # Grab everything after "from " until ")" or end
            candidate = history[start + 5:].strip()  # skip "(from"
            # Remove trailing ) if present
            if candidate.endswith(")"):
                candidate = candidate[:-1].strip()
            # Take last 3 uppercase letters (handles extra spaces/junk)
            words = candidate.split()
            for word in reversed(words):
                if len(word) == 3 and word.isupper() and word.isalpha():
                    return word
    # Format 2: "AAA-BBB-CCC" or single "DDD"
    else:
        parts = history.split("-")
        last_part = parts[-1].strip()
        if len(last_part) == 3 and last_part.isupper() and last_part.isalpha():
            return last_part
    
    # Fallback: if the whole string is already a 3-letter code
    if len(history) == 3 and history.isupper() and history.isalpha():
        return history
    
    return None  # couldn't parse

def format_number_suffix(number: int):
    """
    Returns the English ordinal suffix for a given integer.
    
    Examples:
        1  -> "st"
        2  -> "nd"
        3  -> "rd"
        11 -> "th"
        12 -> "th"
        13 -> "th"
        21 -> "st"
        22 -> "nd"
        23 -> "rd"
        24 -> "th"
    """
    # Handle the absolute value to deal with negative numbers correctly
    abs_number = abs(number)
    
    # Get the last two digits to check for teen exceptions (11, 12, 13)
    last_two = abs_number % 100
    
    if 11 <= last_two <= 13:
        return f"{number}th"
    
    # Get the last digit
    last_digit = abs_number % 10
    
    if last_digit == 1:
        return f"{number}st"
    elif last_digit == 2:
        return f"{number}nd"
    elif last_digit == 3:
        return f"{number}rd"
    else:  # 0, 4-9
        return f"{number}th"    


def fetch_draft_for_year(year):
    """Fetch draft data for a specific year from the NHL records API"""
    print(f"Fetching draft data for year: {year}")
    api_url  =  "https://records.nhl.com/site/api/draft?cayenneExp=%20draftYear%20=%20" + str(year)
    return fetch_nhl_api(api_url)



