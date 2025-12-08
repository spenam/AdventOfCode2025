from typing import Iterable
from input_fetcher import get_input


def parse_input(text: str) -> list[list[int]]:
    """Parse raw puzzle input into a list of 'batteries', each a list of digits."""
    batteries: list[list[int]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",") if p.strip()]
        for part in parts:
            batteries.append([int(ch) for ch in part])
    return batteries



def part1(batteries: Iterable[list[int]]) -> int:
    """Compute the total voltage for part 1."""
    total_voltage = 0

    for battery in batteries:
        digits = list(battery)
        if len(digits) < 2:
            continue

        sorted_digits = sorted(digits)
        max_number = sorted_digits[-1]
        second_max_number = sorted_digits[-2]

        index_max = digits.index(max_number)
        if index_max == len(digits) - 1:
            index_max = digits.index(second_max_number)

        first = digits[index_max]
        second = max(digits[index_max + 1 :])
        jolt = int(f"{first}{second}")
        total_voltage += jolt

    return total_voltage

def part2(batteries: Iterable[list[int]]) -> int:
    total_voltage = 0

    for battery in batteries:
        digits = list(battery)
        jolt = 0

        for i in range(12):
            if not digits:
                break
            i = int(-1 * (11 - i))
            if i>-1:
                temp=digits[:]
            else:
                temp=digits[:i]

            nmax = max(temp)
            nindex = temp.index(nmax)
            digits = digits[nindex + 1 :]
            jolt = jolt * 10 + nmax

        total_voltage += jolt

    return total_voltage

def main() -> None:
    raw = get_input(year=2025, day=3)
    batteries = parse_input(raw)

    answer1 = part1(batteries)
    answer2 = part2(batteries)

    print("Solution Part One:")
    print(answer1)
    print("#" * 30)
    print("Solution Part Two:")
    print(answer2)


if __name__ == "__main__":
    main()