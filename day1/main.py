def parse_input(input_data="input.txt"):
    with open(input_data, 'r') as file:
        lines = file.readlines()
    return lines


def part_one(input_data):
    left_list = []
    right_list = []
    distances = []

    for line in input_data:
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    for number in range(len(left_list)):
        left_number = left_list[number]
        right_number = right_list[number]
        distances.append(abs(left_number - right_number))

    return sum(distances)


def part_two(input_data):
    left_list = []
    right_list = []
    similarity_list = []

    for line in input_data:
        left, right = line.strip().split()
        left_list.append(int(left))
        right_list.append(int(right))

    left_list.sort()
    right_list.sort()

    for number in left_list:
        similarity_list.append(number * right_list.count(number))
    return sum(similarity_list)


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
    test_solution(part_one, "example.txt", 11)
    print(f"Part 1 = {part_one(input_data)}")
    test_solution(part_two, "example.txt", 31)
    print(f"Part 2 = {part_two(input_data)}")
