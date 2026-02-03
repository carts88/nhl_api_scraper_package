# NHL API Wrapper

A Python wrapper for accessing NHL statistics and data through official NHL APIs.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [API Functions](#api-functions)
  - [Draft Functions](#draft-functions)
  - [Player Functions](#player-functions)
  - [Game Functions](#game-functions)
  - [Team Functions](#team-functions)
  - [Management Functions](#management-functions)
  - [League Functions](#league-functions)
- [Usage Examples](#usage-examples)
- [API Endpoints](#api-endpoints)

## Overview

This library provides easy access to NHL data including player statistics, team information, draft history, game data, and more through the official NHL API endpoints.

## Features

- 🏒 Fetch draft information and pick histories
- 👤 Access player information and game logs
- 📊 Retrieve game statistics (box scores, play-by-play, shift charts)
- 🏆 Get team rosters, schedules, and standings
- 👔 Access GM and coach biographical data and tenure information
- 🔍 Query prospects by team
- 📅 Season-specific and date-specific data retrieval


## API Functions

### Draft Functions

#### `fetch_draft(year)`

Fetches NHL draft information for a specific year.

**Parameters:**
- `year` (int): The draft year

---

#### `parse_pick_for_original_owner`

Gets the original owner of a draft pick based on team pick history key in the draft JSON.

**Returns:** Original team information for traded picks

---

### Player Functions

#### `fetch_player_info(player_id)`

Retrieves detailed information about a specific NHL player.

**Parameters:**
- `player_id` (int): NHL database player identifier

---

#### `fetch_player_game_logs(player_id, season, game_type_id)`

Fetch player game logs for a specific season from the NHL records API.

**Parameters:**
- `player_id` (int): ID representing player within the NHL's database
- `season` (str): 8-digit season code (e.g., `"20232024"`)
- `game_type_id` (int): Game type identifier
  - `2` = Regular season
  - `3` = Playoffs

**Example:**
```python
logs = fetch_player_game_logs(8478402, "20232024", 2)
```

---

### Game Functions

#### `fetch_shift_charts(game_id)`

Retrieves shift chart data for a specific game.

**Parameters:**
- `game_id` (int): NHL game identifier

---

#### `fetch_box_score(game_id)`

Fetches the box score for a specific game.

**Parameters:**
- `game_id` (int): NHL game identifier

---

#### `fetch_play_by_play(game_id)`

Gets play-by-play data for a specific game.

**Parameters:**
- `game_id` (int): NHL game identifier

---

#### `get_regular_season_game_ids(season)`

Retrieves all regular season game IDs for a given season.

**Parameters:**
- `season` (str): 8-digit season code (e.g., `"20232024"`)

---

### Team Functions

#### `fetch_standings(date)`

Fetch the current NHL standings from the NHL records API.

**Parameters:**
- `date` (str): Date for standings in `YYYY-MM-DD` format

**API Endpoint:** `https://api-web.nhle.com/v1/standings/{date}`

**Example:**
```python
standings = fetch_standings("2024-01-15")
```

---

#### `fetch_team_schedule(team_tricode, season)`

Fetch the schedule for a specific NHL team.

**Parameters:**
- `team_tricode` (str): 3-letter team code (e.g., `"TOR"`, `"NYR"`, `"VGK"`)
- `season` (str): 8-digit season code (e.g., `"20232024"`)

**API Endpoint:** `https://api-web.nhle.com/v1/club-schedule-season/{team_tricode}/{season}`

**Example:**
```python
schedule = fetch_team_schedule("TOR", "20232024")
```

---

#### `fetch_team_roster(team_tricode, season)`

Fetch the roster for a specific NHL team.

**Parameters:**
- `team_tricode` (str): 3-letter team code representing the NHL team
- `season` (str): 8-digit season code (e.g., `"20232024"`)

**API Endpoint:** `https://api-web.nhle.com/v1/roster/{team_tricode}/{season}`

**Example:**
```python
roster = fetch_team_roster("BOS", "20232024")
```

---

#### `fetch_team_prospects(team_tricode)`

Fetch the prospects for a specific NHL team (no season parameter required).

**Parameters:**
- `team_tricode` (str): 3-letter team code representing the NHL team

**API Endpoint:** `https://api-web.nhle.com/v1/prospects/{team_tricode}`

**Example:**
```python
prospects = fetch_team_prospects("CHI")
```

---

### Management Functions

#### `fetch_gm_tenures()`

Retrieves tenure information for all NHL general managers.

**Returns:** Historical and current GM tenure data

---

#### `fetch_gm_bios()`

Fetches biographical information for NHL general managers.

**Returns:** GM biographical data

---

#### `fetch_coach_bios()`

Retrieves biographical information for NHL coaches.

**Returns:** Coach biographical data

---

#### `fetch_coach_tenures()`

Gets tenure information for all NHL coaches.

**Returns:** Historical and current coach tenure data

---

### League Functions

#### `fetch_all_franchises()`

Fetch all NHL franchises from the NHL records API.

**API Endpoint:** `https://api.nhle.com/stats/rest/en/franchise`

**Returns:** Complete list of all NHL franchises (past and present)

**Example:**
```python
franchises = fetch_all_franchises()
```

---

## Usage Examples

### Get Current Standings
```python
from datetime import date

today = date.today().strftime("%Y-%m-%d")
current_standings = fetch_standings(today)
```

### Fetch Player Season Stats
```python
# Connor McDavid's 2023-24 regular season
mcdavid_logs = fetch_player_game_logs(8478402, "20232024", 2)
```

### Get Team Information
```python
# Toronto Maple Leafs 2023-24 season
tor_roster = fetch_team_roster("TOR", 20232024)
tor_schedule = fetch_team_schedule("TOR", 20232024)
tor_prospects = fetch_team_prospects("TOR")
```

### Access Game Data
```python
# Specific game analysis
box_score = fetch_box_score(2023020001)
pbp_data = fetch_play_by_play(2023020001)
shift_data = fetch_shift_charts(2023020001)
```

## API Endpoints

This wrapper utilizes the following NHL API endpoints:

| Endpoint | Base URL |
|----------|----------|
| Web API | `https://api-web.nhle.com/v1/` |
| Stats API | `https://api.nhle.com/stats/rest/en/` |

## 📝 Notes

- All season parameters use an 8-digit format combining two years (e.g., `"20232024"` for the 2023-24 season)
- Team tricodes are 3-letter abbreviations (e.g., `"TOR"`, `"MTL"`, `"NYR"`)
- Game type IDs: `2` = Regular Season, `3` = Playoffs
- Date formats follow `YYYY-MM-DD` standard

## 🤝 Contributing

Contributions are welcome! Please ensure all functions include proper documentation and follow the existing code style.

## 📄 License

Please refer to NHL's API terms of service for data usage guidelines.

---

**Note:** This is an unofficial wrapper and is not affiliated with or endorsed by the National Hockey League.