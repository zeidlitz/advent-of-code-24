from itertools import chain

def parse_input(input_data="input.txt"):
    res = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        res = line.strip().split()
        res = [int(item) for item in res]
    return res

def evaluate_stone(input_data, stone, t):
    if (stone,t) in input_data:
        return input_data[(stone,t)]
    if t==0:
        ret = 1
    elif stone==0:
        ret = evaluate_stone(1, t-1)
    elif len(str(stone))%2==0:
        dstr = str(stone)
        left = dstr[:len(dstr)//2]
        right = dstr[len(dstr)//2:]
        left, right = (int(left), int(right))
        ret = evaluate_stone(input_data, left, t-1) + evaluate_stone(input_data, right, t-1)
    else:
        ret = evaluate_stone(input_data, stone*2024, t-1)
    input_data[(stone,t)] = ret
    return ret

def evaluate_stones(input_data, iteration):
    return sum(evaluate_stone(input_data, stone, iteration) for stone in input_data)



def part_one(input_data):
    input_data = parse_input()
    return sum(evaluate_stones(input_data,25))

def part_one(input_data):
    input_data = parse_input()
    return sum(evaluate_stones(input_data,75))


def test_solution(func, input_data, result):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    example_input_data = parse_input(input_data)
    expected_output = result
    actual_output = func(example_input_data)

    if actual_output == expected_output:
        print(f"Test for {func.__name__} - {GREEN}PASSED{RESET}: expected {actual_output}, got {actual_output}")
    else:
        print(f"Test for {func.__name__} - {RED}FAILED{RESET}: expected {expected_output}, got {actual_output}")


if __name__ == "__main__":
    input_data = parse_input()
    test_solution(part_one, "example.txt", 55312)
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")
