## Helper Functions
def time_string_to_mins_secs(time_string: str):
    minutes, seconds = map(int, time_string.split(':'))
    return  minutes, seconds

 
def time_string_to_seconds(time_str_series):
    """Convert Series of 'MM:SS' strings to total seconds (vectorized)"""
    mins_secs = time_str_series.str.split(':', expand=True).astype(int)
    return mins_secs[0] * 60 + mins_secs[1]

def time_in_seconds_to_time_string(seconds: int):
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"  # Zero-padded for consistency
