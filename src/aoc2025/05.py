from input_fetcher import get_input

def parse_input(text: str) -> [list[tuple[int]], list[int]]:
    """Parse raw puzzle input"""
    fresh: list[int] = []
    available: list[int] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.find("-")>-1:
            left, right = line.split("-")
            fresh.append([int(left), int(right)])
        else:
            available.append(int(line))
    
    return fresh, available

def part1(fresh: list[tuple[int]], available: list[int]) -> int:
    """Find which available elements are fresh
    """
    count = 0
    for a in available:
        is_fresh = False
        for fr in fresh:
            if a>=fr[0] and a<fr[1]+1:
                is_fresh = True
                break
        if is_fresh:
            count += 1


    return(count)

def part2(fresh: list[tuple[int]]) -> int:
    """Find fresh ids
    """
    fresh_ids=[]
    for begin,end in sorted(fresh):
        if fresh_ids and fresh_ids[-1][1] >= begin - 1:
            fresh_ids[-1][1] = max(fresh_ids[-1][1], end)
        else:
            fresh_ids.append([begin, end])

    count = 0
    for fr in fresh_ids:
        count += fr[1]-fr[0]+1


    return(count)


def main() -> None:
    raw = get_input(year=2025, day=5)
    fresh, available = parse_input(raw)

    answer1 = part1(fresh, available)
    print("Solution Part One:")
    print(answer1)

    answer2 = part2(fresh)
    print("Solution Part Two:")
    print(answer2)


if __name__ == "__main__":
    main()