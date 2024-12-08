import sys

def parse_input(input_file="input.txt"):
    with open(input_file, 'r') as file:
        grid = []
        lines = file.readlines()
        for line in lines:
            grid.append(line.strip())
        grid = [list(row) for row in grid]
    return grid


def is_within_bounds(r, c, rows, columns):
    if r < 0 or r >= rows:
        return False
    if c < 0 or c >= columns:
        return False
    return True


def place_signal(r0, c0, r1, c1, dr, dc, rows, columns, result):
    north_r = -1 * dr
    north_c = -1 * dc
    south_r = dr
    south_c = dc
    north_signal_r = r0 + north_r
    north_signal_c = c0 + north_c
    south_signal_r = r1 + south_r
    south_signal_c = c1 + south_c
    if (is_within_bounds(north_signal_r, north_signal_c, rows, columns)):
        result.append((north_signal_r, north_signal_c))
    if (is_within_bounds(south_signal_r, south_signal_c, rows, columns)):
        result.append((south_signal_r, south_signal_c))


def find_signals(grid):
    result = []
    from collections import defaultdict
    positions = defaultdict(list)
    rows = len(grid)
    columns = len(grid[0])
    for row in range(rows):
        for col in range(columns):
            element = grid[row][col]
            if element != ".":
                positions[element].append((row, col))

    for element, pos_list in positions.items():
        for i in range(len(pos_list)):
            for j in range(i + 1, len(pos_list)):
                r0 = pos_list[i][0]
                c0 = pos_list[i][1]
                r1 = pos_list[j][0]
                c1 = pos_list[j][1]
                row_diff = r1 - r0
                col_diff = c1 - c0
                place_signal(r0, c0, r1, c1, row_diff, col_diff, rows, columns, result)
    return result


def place_harmonic(r0, c0, r1, c1, dr, dc, rows, columns, result):
    north_r = -1 * dr
    north_c = -1 * dc
    south_r = dr
    south_c = dc
    north_signal_r = r0 + north_r
    north_signal_c = c0 + north_c
    south_signal_r = r1 + south_r
    south_signal_c = c1 + south_c

    while (is_within_bounds(north_signal_r, north_signal_c, rows, columns)):
        result.append((north_signal_r, north_signal_c))
        north_signal_r += + north_r
        north_signal_c += + north_c
    while (is_within_bounds(south_signal_r, south_signal_c, rows, columns)):
        result.append((south_signal_r, south_signal_c))
        south_signal_r += south_r
        south_signal_c += south_c


def find_harmonics(grid):
    result = []
    antennas = []
    from collections import defaultdict
    positions = defaultdict(list)
    rows = len(grid)
    columns = len(grid[0])
    for row in range(rows):
        for col in range(columns):
            element = grid[row][col]
            if element != ".":
                antennas.append((row, col))
                positions[element].append((row, col))

    for element, pos_list in positions.items():
        for i in range(len(pos_list)):
            for j in range(i + 1, len(pos_list)):
                r0 = pos_list[i][0]
                c0 = pos_list[i][1]
                r1 = pos_list[j][0]
                c1 = pos_list[j][1]
                row_diff = r1 - r0
                col_diff = c1 - c0
                place_harmonic(r0, c0, r1, c1, row_diff, col_diff, rows, columns, result)
    return antennas, result


def part_one(input_data):
    antenna_grid = input_data
    result = find_signals(antenna_grid)
    result = list(set(result))
    return len(result)


def part_two(input_data):
    antenna_grid = input_data
    antennas, result = find_harmonics(antenna_grid)
    result = [item for item in result if item not in antennas]
    result = list(set(result))
    return len(antennas) + len(result)


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
    test_part_one(14)
    print(f"Part 1 = {part_one(input_data)}")
    test_part_two(9)
    print(f"Part 2 = {part_two(input_data)}")
