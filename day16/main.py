from astar import AStar
import pdb


class GridAStar(AStar):
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic_cost_estimate(self, current, goal):
        return 1

    def neighbors(self, node):
        x, y = node
        neighbor_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        return [
            (nx, ny)
            for nx, ny in neighbor_positions
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == "."
        ]

    def distance_between(self, n1, n2):
        return 1


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


def locate(grid, target):
    for y, row in enumerate(grid):
        for x, value in enumerate(row):
            if value == target:
                grid[y][x] = "."
                return grid, (y, x)
    return None


def part_one(input_data):
    grid = input_data
    start = locate(grid, "S")
    end = locate(grid, "E")
    astar_solver = GridAStar(grid)
    print_grid(grid)
    path = list(astar_solver.astar(start, end))
    print(path)
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
    test_solution(part_one, "example.txt", 7036)
    # print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
