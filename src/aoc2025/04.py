from input_fetcher import get_input
import numpy as np

def parse_input(text: str) -> np.ndarray:
    """Parse raw puzzle input into a numpy matrix"""
    positions: list[list[int]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        positions.append([0 if ch == "." else 1 for ch in line])
    positions = np.array(positions, dtype=int)
    return positions

def part1(positions: np.ndarray) -> int:
    """Compute number of rolls accessed by forklift
    """
    p = np.pad(positions, 1, mode="constant")  # pad with zeros around
    neighbor_counts = (
        p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +
        p[1:-1, :-2] + p[1:-1, 2:] +
        p[2:, :-2]  + p[2:, 1:-1] + p[2:, 2:]
    ) 
    rolls = positions[neighbor_counts<4]
    return(np.sum(rolls))

def part2(positions: np.ndarray) -> int:
    """Compute number of rolls accessed by forklift with removal
    """
    total = 0
    while True:
        p = np.pad(positions, 1, mode="constant")  # pad with zeros around
        neighbor_counts = (
            p[:-2, :-2] + p[:-2, 1:-1] + p[:-2, 2:] +
            p[1:-1, :-2] + p[1:-1, 2:] +
            p[2:, :-2]  + p[2:, 1:-1] + p[2:, 2:]
        ) 

        rolls = np.sum(positions[neighbor_counts<4])
        if rolls<1:
            break
        total += rolls
        positions=np.logical_not(np.logical_or(np.logical_not(positions),(neighbor_counts<4)))*1
    return(np.sum(total))


def main() -> None:
    raw = get_input(year=2025, day=4)
    positions = parse_input(raw)

    answer1 = part1(positions)
    print("Solution Part One:")
    print(answer1)

    answer2 = part2(positions)
    print("Solution Part Two:")
    print(answer2)


if __name__ == "__main__":
    main()