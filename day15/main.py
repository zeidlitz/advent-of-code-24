import pdb


def parse_input(input_data="input.txt"):
    with open(input_data, 'r') as file:
        text = file.read()
    grid, directions = text.strip().split("\n\n")
    grid = [list(line) for line in grid.splitlines()]
    directions = list(directions)
    directions = [item for item in directions if item != '\n']
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


def move_target_to_source(grid, target, source):
    source_r, source_c = source
    target_r, target_c = target
    grid[target_r][target_c] = grid[source_r][source_c]
    grid[source_r][source_c] = "."
    return grid


def can_target_be_moved(grid, r, c, dr, dc):
    boxes = [(r, c)]
    r, c = r + dr, c + dc
    while (grid[r][c] != "#"):
        if grid[r][c] == "O":
            boxes.append((r,c))
        if grid[r][c] == ".":
            return True, boxes
        r, c = r + dr, c + dc
    return False, boxes


def move(grid, source, direction):
    directions = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0)
    }
    source_r, source_c = source
    dr, dc = directions[direction]

    target_r, target_c = source_r + dr, source_c + dc
    target = grid[target_r][target_c]

    if target == "#":
        return grid

    if target == ".":
        grid = move_target_to_source(grid, (target_r, target_c), source)
        return grid

    if target == "O":
        can_move, boxes = can_target_be_moved(grid, target_r, target_c, dr, dc)
        if can_move:
            boxes = list(reversed(boxes))
            for box in boxes:
                grid = move_target_to_source(grid, (box[0] + dr, box[1] + dc), box)
            grid = move_target_to_source(grid, (target_r, target_c), source)
        return grid


def GPS(grid):
    coordinates = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                coordinates.append((100 * r) + c)
    return sum(coordinates)


def part_one(input_data):
    grid, directions = input_data
    for d in directions:
        r = locate(grid)
        grid = move(grid, r, d)
    print_grid(grid)
    return GPS(grid)


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
    test_solution(part_one, "example.txt", 10092)
    print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
