# Advent of Code 2025 – Python Solutions

This repository contains Python solutions to Advent of Code 2025, organized as a small, well-structured project with automated input fetching, type hints, and tests.
Project goals

    Practice fast, readable problem solving in Python.

    Showcase clean code, testing, and basic tooling for prospective employers.

    Provide easily reusable templates for future Advent of Code editions.

Repository structure

A typical layout (adapt names if yours differ):

* `src/aoc2025/`
    * `01.py`, `02.py`, … – solution modules for each day.

    * `input_fetcher.py` – helper for downloading and caching inputs.

* `inputs/2025/`
    * `input_01.txt`, `input_02.txt`, … – cached puzzle inputs.
* `tests/`
    * `test_01.py`, `test_02.py`, … – tests using the official examples.
    `requirements.txt` – dependencies.
    `.gitignore` – ignores virtualenvs, caches, etc.
    `.github/workflows/ci.yml` – run tests and linters on each push.

## Installation

Use virtualenv to install:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Advent of Code session setup

Puzzle input is fetched from the Advent of Code website using your personal session cookie and cached under inputs/. The session is treated as a secret and never stored in the repository.

1. Log into https://adventofcode.com in your browser.

2. Find your session cookie (via browser dev tools).

3. Set it as an environment variable (for example in your shell profile):

```bash
export AOC_SESSION="your_session_token_here"
```

Do not commit this value or any file containing it.

## Fetching inputs

Inputs are retrieved lazily by a shared helper in `input_fetcher.py`.

Example usage in a solution file:

```python
from aoc2025.input_fetcher import get_input


def parse_input(text: str):
    return text.splitlines()


def part1(data):
    ...


def part2(data):
    ...


if __name__ == "__main__":
    raw = get_input(year=2025, day=1)
    data = parse_input(raw)
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
```

On first run, the helper downloads the input from the Advent of Code URL for the given year and day and saves it under `inputs/2025/day01.txt`, then reads from the cached file on subsequent runs.

## Running solutions

From the project root, after installing dependencies and setting `AOC_SESSION`:

```bash
python -m aoc2025.day01
python -m aoc2025.day02
# etc.
```

Each module prints the answers for part 1 and part 2 to standard output.

## Running tests

Tests use pytest and verify both the parsing and the expected answers for the examples from the problem statements (and optionally the full inputs).

```bash
pytest
```

You can run tests for a single day:

```bash
pytest tests/test_day01.py
```

This project is maintained as a public showcase of Python problem-solving and coding practices. 