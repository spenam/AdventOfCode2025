from input_fetcher import get_input



def parse_input_1(text: str) -> list[list[int]] | list[str]:
    """Parse raw puzzle input into a list of Instructions."""
    counter=0
    numbers=[]
    operators=[]
    for line in text.splitlines():
        line = line.strip()
        line_nospace = ' '.join(line.split())
        if not line:
            continue
        if counter==0:
            line_list = list(map(int,line_nospace.split(" ")))
            for i in range(len(line_list)):
                numbers.append([line_list[i]])
        else:
            if "*" in line:
                line_list = line_nospace.split(" ")
                for i in range(len(line_list)):
                    operators.append(line_list[i])
            else:
                line_list = list(map(int,line_nospace.split(" ")))
                for i in range(len(line_list)):
                    numbers[i].append(line_list[i])
        counter+=1
                
    return numbers, operators

def parse_input_2(text: str) -> list[list[int]] | list[str]:
    """Parse raw puzzle input into a list of Instructions."""
    numbers=[]
    operators=[]
    transposed_numbers=[]
    for line in text.splitlines():
        if not line:
            continue
        if line.find("+")>-1:
            line=line.strip()
            line_nospace = ' '.join(line.split())
            line_list = line_nospace.split(" ")
            for i in range(len(line_list)):
                operators.append(line_list[i])
        else:
            numbers.append(line)
    common_ws_positions = set.intersection(
    *[ {i for i, ch in enumerate(s) if ch.isspace()} for s in numbers ]
)

    common_ws_positions = sorted(common_ws_positions)
    split_strings = [split_at_positions(s, common_ws_positions) for s in numbers]
    for i in numbers:
        print(i)
        print("#"*20)
    print(split_strings[-1])
    for i in range(len(split_strings[0])):
        transposed_numbers.append(list(map(int,[''.join(s) for s in zip(*[l[i] for l in split_strings])])))
    return transposed_numbers, operators
    
                

def split_at_positions(s, positions):
    parts = []
    prev = 0
    for pos in positions:
        parts.append(s[prev:pos])
        prev = pos + 1
    parts.append(s[prev:])
    return parts



def operation(numbers,operator):
    result=0
    for i in range(len(numbers)):
        if "*" in operator:
            if i==0:
                result=1
            result *= numbers[i]
        elif "+" in operator:
            result += numbers[i]
        elif "-" in operator:
            result -= numbers[i]
    return result

def part1(numbers:list[list[int]], operators:list[str]) -> int:
    total = 0
    for i in range(len(operators)):
        total += operation(numbers[i],operators[i])
    return  total
        


def main() -> None:
    raw = get_input(year=2025, day=6)
    numbers, operators = parse_input_1(raw)

    answer1 = part1(numbers, operators)
    print("Answer to part one:")
    print(answer1)

    numbers, operators = parse_input_2(raw)

    answer2 = part1(numbers, operators) # part1 logic reused
    print("Answer to part two:")
    print(answer2)


if __name__ == "__main__":
    main()