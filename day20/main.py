def parse_input(input_data="input.txt"):
    with open(input_data, 'r') as file:
        lines = file.readlines()
    return lines


def part_one(input_data):
    return 0


def part_two(input_data):
    return 0


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
    test_solution(part_one, "example.txt", 0)
    print(f"Part 1 = {part_one(input_data)}")
    test_solution(part_two, "example.txt", 0)
    print(f"Part 2 = {part_two(input_data)}")
