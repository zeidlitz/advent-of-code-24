import pdb

KEYPAD = [
    ["7", "8", "9"],
    ["4", "5", "6"],
    ["1", "2", "3"],
    ["D", "0", "A"]
]

ARROWPAD = [
    ["D", "^", "A"],
    ["<", "v", ">"]
]


def parse_input(input_data="input.txt"):
    res = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = line.strip()
        line = [char for pair in line for char in pair]
        res.append(line)
    return res


def get_rows_and_columns(grid, s, d):
    for i in range(len(grid)):
        for j in range(len(grid[0])):

            if grid[i][j] == s:
                sr = i
                sc = j

            if grid[i][j] == d:
                dr = i
                dc = j
    return sr, sc, dr, dc


def get_keypad_path(grid, start_row, start_col, dest_row, dest_col):
    path = ""

    def move_around_d(grid, curr_row, curr_col, next_row):
        nonlocal path
        if grid[next_row][curr_col] == "D":
            if curr_col + 1 < len(grid[0]):
                path += ">"
                curr_col += 1
            elif curr_col - 1 >= 0:
                path += "<"
                curr_col -= 1
        return curr_col

    while start_col < dest_col:
        start_row = move_around_d(grid, start_row, start_col, start_col - 1)
        path += ">"
        start_col += 1

    while start_col > dest_col:
        path += "<"
        start_col -= 1

    while start_row > dest_row:
        # start_col = move_around_d(grid, start_row, start_col, start_row - 1)
        path += "^"
        start_row -= 1

    while start_row < dest_row:
        path += "v"
        start_row += 1


    return path


def find_keypad_strings(input_data):
    start_key = "A"
    keypad_strings = {}
    for keys in input_data:
        keypad_string = ""
        for destination_key in keys:
            sr, sc, dr, dc = get_rows_and_columns(KEYPAD, start_key, destination_key)
            start_key = destination_key
            keypad_string += get_keypad_path(KEYPAD, sr, sc, dr, dc) + "A"
        keypad_strings["".join(keys)] = keypad_string
    return keypad_strings


def find_arrowpad_strings(keypad_strings):
    start_key = "A"
    arrowpad_strings = {}
    for k, v in keypad_strings.items():
        arrowpad_string = ""
        for destination_key in v:
            sr, sc, dr, dc = get_rows_and_columns(ARROWPAD, start_key, destination_key)
            start_key = destination_key
            arrowpad_string += get_keypad_path(ARROWPAD, sr, sc, dr, dc) + "A"
        arrowpad_strings[k] = arrowpad_string
    return arrowpad_strings


def compute_complexity(arrowpad_strings):
    res = []
    for k, v in arrowpad_strings.items():
        res.append(len(v) * int(k[:3]))
        print(len(v), "*", int(k[:3]), "=", res)
    return sum(res)


def print_map(m):
    for k, v in m.items():
        print(k, ": ", v)


def part_one(input_data):
    keypad_strings = find_keypad_strings(input_data)
    print_map(keypad_strings)
    print()
    arrowpad_strings = find_arrowpad_strings(keypad_strings)
    print_map(arrowpad_strings)
    print()
    arrowpad_strings = find_arrowpad_strings(arrowpad_strings)
    print_map(arrowpad_strings)
    print()
    return compute_complexity(arrowpad_strings)


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
    test_solution(part_one, "example.txt", 126384)
    # print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
