from collections import deque
import pdb


def parse_input(input_data="input.txt"):
    grid = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        line = [int(item) for item in line.strip()]
        grid.append(line)
    grid = [list(row) for row in grid]
    return grid


def print_grid(grid):
    for line in grid:
        print(line)


def find_start_positions(grid):
    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                res.append((i,j))
    return res


def find_trail_score(grid, start_position):
    start_position = [start_position]
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque(start_position)
    visited = set(start_position)
    reachable_nines = 0

    while queue:
        x, y = queue.popleft()
        current_value = grid[x][y]

        if current_value == 9:
            reachable_nines += 1
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == current_value + 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    return reachable_nines


def find_trail_rating(grid, start):
    rows, cols = len(grid), len(grid[0])
    start_x, start_y = start
    paths_count = 0

    def is_valid(x, y, current_value):
        return 0 <= x < rows and 0 <= y < cols and grid[x][y] == current_value + 1

    def dfs(x, y, current_path):
        nonlocal paths_count

        if grid[x][y] == 9:
            paths_count += 1
            return

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, grid[x][y]):
                dfs(nx, ny, current_path + [(nx, ny)])

    dfs(start_x, start_y, [start])

    return paths_count


def part_one(input_data):
    start_positions = find_start_positions(input_data)
    res = []
    for pos in start_positions:
        res.append(find_trail_score(input_data, pos))
    return sum(res)


def part_two(input_data):
    start_positions = find_start_positions(input_data)
    res = []
    for pos in start_positions:
        res.append(find_trail_rating(input_data, pos))
    return sum(res)


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
    test_solution(part_one, "example.txt", 36)
    print(f"Part 1 = {part_one(input_data)}")
    test_solution(part_two, "example.txt", 81)
    print(f"Part 2 = {part_two(input_data)}")
