def parse_input():
    with open("input.txt", 'r') as file:
        lines = file.readlines()
    return lines


def part_one(input_data):
    return 0


def part_two(input_data):
    return 0


def test_part_one(num):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    example_input_data = parse_input("example_part_one.txt")
    expected_output = num
    actual_output = part_one(example_input_data)

    if actual_output == expected_output:
        print(f"Test for part I : {GREEN}PASSED{RESET}")
    else:
        print(f"Test for part I : {RED}FAILED: expected {expected_output}, got {actual_output}{RESET}")


def test_part_two(num):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    example_input_data = parse_input("example_part_two.txt")
    expected_output = num
    actual_output = part_two(example_input_data)

    if actual_output == expected_output:
        print(f"Test for part II: {GREEN}PASSED{RESET}")
    else:
        print(f"Test for part II: {RED}FAILED: expected {expected_output}, got {actual_output}{RESET}")


if __name__ == "__main__":
    input_data = parse_input()
    test_part_one(0)
    print(f"Part 1 = {part_one(input_data)}")
    test_part_two(0)
    print(f"Part 2 = {part_two(input_data)}")
