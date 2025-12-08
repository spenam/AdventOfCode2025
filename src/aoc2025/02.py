from dataclasses import dataclass
from input_fetcher import get_input


@dataclass
class Range:
    """Inclusive integer range [start, end]."""

    start: int
    end: int

def parse_input(text: str) -> list[Range]:
    """Parse raw puzzle input into a list of inclusive ranges."""
    ranges: list[Range] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        for part in line.split(","):
            part = part.strip()
            if not part:
                continue
            left, right = part.split("-")
            ranges.append(Range(start=int(left), end=int(right)))
    return ranges

def is_two_block_repeat(n: int) -> bool:
    """Check if n has even length and is of the form AA (two identical halves)."""
    s = str(n)
    length = len(s)
    if length % 2 != 0:
        return False
    half = length // 2
    return s[:half] == s[half:]

def is_repeated_pattern(n: int) -> bool:
    """Check if n is a repetition of some shorter prefix pattern."""
    s = str(n)
    length = len(s)
    for size in range(1, length // 2 + 1):
        if length % size != 0:
            continue
        pattern = s[:size]
        if pattern * (length // size) == s:
            return True
    return False

def iter_range(r: Range):
    """Iterate over all integers in the inclusive range."""
    # original loops used range(r2 - r1) and then added r1,
    # which effectively iterates [r1, r2 - 1]
    return range(r.start, r.end)

def part1(ranges: list[Range]) -> int:
    """Sum all 'invalid' numbers for part 1."""
    invalids: list[int] = []

    for r in ranges:
        for value in iter_range(r):
            if is_two_block_repeat(value):
                invalids.append(value)

    return sum(invalids)

def part2(ranges: list[Range]) -> int:
    """Sum distinct 'invalid' numbers for part 2."""
    invalids: set[int] = set()

    for r in ranges:
        for value in iter_range(r):
            if is_repeated_pattern(value):
                invalids.add(value)

    return sum(invalids)


def main() -> None:
    raw = get_input(year=2025, day=2)
    ranges = parse_input(raw)

    answer1 = part1(ranges)
    answer2 = part2(ranges)

    print("Solution Part One:")
    print(answer1)
    print("#" * 40)
    print("Solution Part Two:")
    print(answer2)


if __name__ == "__main__":
    main()