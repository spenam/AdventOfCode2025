import os
from pathlib import Path

import requests


AOC_BASE_URL = "https://adventofcode.com"
AOC_SESSION_ENV = "AOC_SESSION"
INPUTS_DIR = Path("inputs")  # adjust if you prefer a different root


class AdventOfCodeError(RuntimeError):
    pass


def get_input(year: int, day: int, *, force_refresh: bool = False) -> str:
    """
    Fetch Advent of Code puzzle input for given year and day.

    - Uses local cache in inputs/{year}/input_{dd}.txt
    - Downloads from AoC if file is missing or force_refresh=True
    """
    if not (1 <= day <= 25):
        raise ValueError(f"day must be between 1 and 25, got {day}")

    day_str = f"{day:02d}"
    target_dir = INPUTS_DIR / str(year)
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / f"input_{day_str}.txt"

    # Return cached file if present and not forcing refresh
    if target_file.exists() and not force_refresh:
        return target_file.read_text(encoding="utf-8")

    session_token = os.getenv(AOC_SESSION_ENV)
    if not session_token:
        raise AdventOfCodeError(
            f"Environment variable {AOC_SESSION_ENV} is not set. "
            "Set it to your Advent of Code session cookie."
        )

    url = f"{AOC_BASE_URL}/{year}/day/{day}/input"
    headers = {
        "User-Agent": "aoc-input-fetcher (github portfolio project)",
        "Cookie": f"session={session_token}",
    }

    response = requests.get(url, headers=headers, timeout=10)
    if response.status_code != 200:
        raise AdventOfCodeError(
            f"Failed to fetch input: HTTP {response.status_code}. "
            "Check that your session token is valid and you are logged in."
        )

    text = response.text.rstrip("\n")
    target_file.write_text(text, encoding="utf-8")
    return text