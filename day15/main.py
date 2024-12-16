import pdb


def parse_input(input_data="input.txt"):
    with open(input_data, 'r') as file:
        text = file.read()
    grid, directions = text.strip().split("\n\n")
    grid = [list(line) for line in grid.splitlines()]
    directions = list(directions)
    return (grid, directions)


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def locate(grid, target="@"):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == target:
                return (y, x)
    return None


def move_to(grid, r, c, dr, dc):
    if grid[dr][dc] == "#":
        return
    if grid[dr][dc] == "0":
        move_to
    # if grid[dr][dc] == "0" or grid[dr][dc] == "#":
    #     return grid
    # grid[dr][dc] = grid[r][c]
    # grid[r][c] = "."
    return grid


def move(grid, source, direction):
    print("moving : ", direction)
    directions = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0)
    }
    r, c = source
    dr, dc = directions[direction]
    target = grid[r+dr][c+dc]

    if target == "#":
        return grid

    if target == "O":
        grid = move_to(grid, r, c, r+dr, c+dc)
        return grid

    if target == ".":
        grid = move_to(grid, r, c, r+dr, c+dc)
        return grid


def part_one(input_data):
    grid, directions = input_data
    for d in directions:
        r = locate(grid)
        grid = move(grid, r, d)
        print_grid(grid)
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
    test_solution(part_one, "example.txt", 2028)
    # print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
