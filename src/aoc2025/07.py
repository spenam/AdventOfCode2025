from input_fetcher import get_input
import numpy as np

def parse_input(text: str) -> np.ndarray:
    """Parse raw puzzle input into a numpy matrix"""
    positions: list[list[int]] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        positions.append([1 if ch == "S" else 3 if ch == "^" else 0 for ch in line])
    positions = np.array(positions, dtype=int)
    return positions

def part1(positions: np.ndarray) -> int:
    count = 0
    for i in range(len(positions)-1):
        index_beam = np.where(positions[i] == 1)[0]
        index_split = np.where(positions[i+1] == 3)[0]
        for j in index_beam:
            if j in index_split:
                positions[i+1,j+1] = 1
                positions[i+1,j-1] = 1
                count +=1
            else:
                positions[i+1,j] = 1
    return(count)

def part2(positions: np.ndarray) -> int:
    n_levels, n_channels = positions.shape
    dp = np.zeros_like(positions, dtype=int)
    
    dp[0] = (positions[0] == 1).astype(int)
    
    for i in range(n_levels - 1):
        for j in range(n_channels):
            if dp[i, j] == 0:
                continue
            if positions[i+1, j] == 3: 
                if j > 0:
                    dp[i+1, j-1] += dp[i, j]
                if j < n_channels - 1:
                    dp[i+1, j+1] += dp[i, j]
            else: 
                dp[i+1, j] += dp[i, j]
    
    return dp[-1].sum()


def main() -> None:
    raw = get_input(year=2025, day=7)
    positions = parse_input(raw)

    answer1 = part1(positions)
    print("Solution Part One:")
    print(answer1)

    answer2 = part2(positions)
    print("Solution Part Two:")
    print(answer2)


if __name__ == "__main__":
    main()