import pdb
from collections import deque


DIRECTIONS = {
    "EAST": (0, 1),
    "WEST": (0, -1),
    "NORTH": (-1, 0),
    "SOUTH": (1, 0),
}


def parse_input(input_data="input.txt"):
    grid = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        grid.append(list(line.strip()))
    return grid


def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()


def trace_grid(grid, path):
    traced_grid = grid
    for x, y in path:
        traced_grid[x][y] = " "
    return traced_grid


def locate(grid, target):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == target:
                grid[y][x] = "."
                return (y, x)
    return None


def compute_score(coordinates):
    directions = {'EAST': (0, 1), 'WEST': (0, -1), 'NORTH': (-1, 0), 'SOUTH': (1, 0)}
    if not coordinates or len(coordinates) < 2:
        return 0
    score = 0

    current_direction = 'EAST'
    for i in range(1, len(coordinates)):
        dr = coordinates[i][0] - coordinates[i - 1][0]
        dc = coordinates[i][1] - coordinates[i - 1][1]
        movement = (dr, dc)
        pdb.set_trace()
        if movement not in DIRECTIONS:
            raise ValueError(f"Invalid movement between {coordinates[i-1]} and {coordinates[i]}.")
        new_direction = DIRECTIONS[movement]
        if new_direction != current_direction:
            score += 1000
            current_direction = new_direction
        score += 1
    return score


def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.'


def grid_search_min_turns(grid, start, end):
    start_x, start_y = start
    end_x, end_y = end
    queue = deque([(start_x, start_y, "EAST", 0, [(start_x, start_y)])])
    visited = set()
    visited.add((start_x, start_y, "EAST"))
    while queue:
        x, y, direction, turns, path = queue.popleft()
        if (x, y) == (end_x, end_y):
            return path
        for new_direction, (dx, dy) in DIRECTIONS.items():
            nx, ny = x + dx, y + dy
            if is_valid(grid, nx, ny):
                new_turns = turns + (1 if new_direction != direction else 0)
                state = (nx, ny, new_direction)
                if state not in visited:
                    visited.add(state)
                    queue.append((nx, ny, new_direction, new_turns, path + [(nx, ny)]))
    return []


def part_one(input_data):
    grid = input_data
    start = locate(grid, "S")
    end = locate(grid, "E")
    path = grid_search_min_turns(grid, start, end)
    return compute_score(path)


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
    test_solution(part_one, "example.txt", 7036)
    print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
