from dataclasses import dataclass
from input_fetcher import get_input
import numpy as np


@dataclass
class Position:
    """Junction box postion in X,Y,Z."""

    X: int
    Y: int
    Z: int

    def distance_to(self, other: "Position") -> float:
        """Calculate Euclidean distance squared to another position."""
        return ((self.X - other.X) ** 2 + (self.Y - other.Y) ** 2 + (self.Z - other.Z) ** 2) 

def parse_input(text: str) -> list[Position]:
    """Parse raw puzzle input into a list of junction boxes positions."""
    positions: list[Position] = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        X,Y,Z = line.split(",")
        new_position = Position(X=int(X), Y=int(Y), Z=int(Z))
        positions.append(new_position)
    return positions

def part1(positions: list[Position]) -> int:
    """Compute the answer for part 1."""
    n = len(positions)
    distance = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance[i, j] = positions[i].distance_to(positions[j])

    rows, cols = np.indices(distance.shape)
    flat_vals = distance.flatten()
    flat_rows = rows.flatten()
    flat_cols = cols.flatten()
    order = np.argsort(flat_vals)
    
    top_indices = list(zip(flat_rows[order[n:n+2000:2]],
                           flat_cols[order[n:n+2000:2]]))

    connected_sets: list[set[int]] = []
    for i, j in top_indices:
            
        set_i = set_j = None
        for s in connected_sets:
            if i in s:
                set_i = s
            if j in s:
                set_j = s
        
        if set_i and set_j:
            if set_i is not set_j:
                set_i |= set_j
                connected_sets.remove(set_j)
        elif set_i:
            set_i.add(j)
        elif set_j:
            set_j.add(i)
        else:
            connected_sets.append({i, j})

    sizes = sorted([len(s) for s in connected_sets], reverse=True)
    return sizes[0] * sizes[1] * sizes[2]

def part2(positions: list[Position]) -> int:
    """Compute the answer for part 2."""
    n = len(positions)
    distance = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            distance[i, j] = positions[i].distance_to(positions[j])

    rows, cols = np.indices(distance.shape)
    flat_vals = distance.flatten()
    flat_rows = rows.flatten()
    flat_cols = cols.flatten()
    order = np.argsort(flat_vals)
    
    top_indices = list(zip(flat_rows[order[n::2]],
                           flat_cols[order[n::2]]))

    connected_sets: list[set[int]] = []
    counter = 0
    for i, j in top_indices:
            
        set_i = set_j = None
        for s in connected_sets:
            if i in s:
                set_i = s
            if j in s:
                set_j = s
        if set_i and set_j:
            if set_i is not set_j:
                set_i |= set_j
                connected_sets.remove(set_j)
        elif set_i:
            set_i.add(j)
        elif set_j:
            set_j.add(i)
        else:
            connected_sets.append({i, j})
        if len(connected_sets)==1:
            is_break=True
            for k in range(n):
                if k not in connected_sets[0]:
                    is_break=False 
            if is_break:
                print(i,j)
                last_pair=(i,j)
                break
        counter+=1


    return positions[last_pair[0]].X*positions[last_pair[1]].X

def main() -> None:
    raw = get_input(year=2025, day=8,test=False)
    positions = parse_input(raw)

    answer1 = part1(positions)

    print("Solution Part One:")
    print(answer1)
    print("#" * 40)

    answer2 = part2(positions)
    print("Solution Part Two:")
    print(answer2)


if __name__ == "__main__":
    main()