from itertools import chain
from concurrent.futures import ThreadPoolExecutor


def parse_input(input_data="input.txt"):
    res = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        res = line.strip().split()
        res = [int(item) for item in res]
    return res


def evaluate_stone(stone):
    if stone == 0:
        return [1]
    stone_str = str(stone)
    if len(stone_str) % 2 == 0:
        mid = len(stone_str) // 2
        left = int(stone_str[:mid])
        right = int(stone_str[mid:])
        return [left, right]
    return [stone * 2024]


def evaluate_stones(stones):
    res = []
    for stone in stones:
        res.append(evaluate_stone(stone))
    return res


def part_one(input_data):
    for i in range(25):
        input_data = evaluate_stones(input_data)
        input_data = list(chain.from_iterable([item] if not isinstance(item, list) else item for item in input_data))
    return len(input_data)


def part_two(input_data):
    def process_half(data):
        return list(chain.from_iterable(
            [item] if not isinstance(item, list) else item for item in evaluate_stones(data)
        ))

    for i in range(75):
        print("Iteration :", i)
        mid = len(input_data) // 2
        first_half = input_data[:mid]
        second_half = input_data[mid:]

        with ThreadPoolExecutor() as executor:
            future_first = executor.submit(process_half, first_half)
            future_second = executor.submit(process_half, second_half)

            first_half_result = future_first.result()
            second_half_result = future_second.result()

        input_data = first_half_result + second_half_result

    return len(input_data)


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
