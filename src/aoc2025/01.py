from dataclasses import dataclass
from input_fetcher import get_input

@dataclass
class Instruction:
    """Single move instruction with direction and number of steps."""

    direction: str  # "L" or "R"
    steps: int

def parse_input(text: str) -> list[Instruction]:
    """Parse raw puzzle input into a list of Instructions."""
    instructions: list[Instruction] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if "L" in line:
            direction = "L"
            value = int(line.split("L")[-1])
        else:
            direction = "R"
            value = int(line.split("R")[-1])
        instructions.append(Instruction(direction=direction, steps=value))
    return instructions

def part1(instructions: list[Instruction]) -> int:
    """Compute the answer for part 1."""
    position = 50
    counts = 0

    for instr in instructions:
        step = -instr.steps if instr.direction == "L" else instr.steps
        new_position = (position + step) % 100
        if new_position < 1:
            counts += 1
        position = new_position

    return counts

def part2(instructions: list[Instruction]) -> int:
    """Compute the answer for part 2."""
    position = 50
    counts = 0

    for instr in instructions:
        sign = -1 if instr.direction == "L" else 1
        val = instr.steps

        # Full laps.
        counts += val // 100

        # Remaining steps.
        remainder = val % 100

        if remainder > 0:
            new_position = position + remainder * sign
            crossed_boundary = (
                (sign > 0 and new_position >= 100)
                or (sign < 0 and new_position < 1 and position > 0)
            )
            if crossed_boundary:
                counts += 1

            position = (new_position + 100) % 100

    return counts


def main() -> None:
    raw = get_input(year=2025, day=1)
    instructions = parse_input(raw)

    answer1 = part1(instructions)
    answer2 = part2(instructions)

    print("Answer to part one:", answer1)
    print("Answer to part two:", answer2)


if __name__ == "__main__":
    main()