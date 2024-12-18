import pdb
from astar import AStar

DIRECTIONS = {
    (0, 1): "WEST",
    (0, -1): "EAST",
    (-1, 0): "SOUTH",
    (1, 0): "NORTH"
}


class GridAStar(AStar):
    def __init__(self, current_node, grid):
        self.current_node = current_node
        self.direction = "EAST"
        self.history = []
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic_cost_estimate(self, current, goal):
        return abs(current[0] - goal[0]) + abs(current[1] - goal[1])

    def neighbors(self, node):
        x, y = node
        neighbor_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
        valid_neighbors = [
            (nx, ny)
            for nx, ny in neighbor_positions
            if 0 <= nx < self.rows and 0 <= ny < self.cols and self.grid[nx][ny] == "."
        ]
        return valid_neighbors

    def print_grid(self):
        r = self.current_node[0]
        c = self.current_node[1]
        self.grid[r][c] = self.direction[0]
        for row in self.grid:
            print("".join(row))
        print()

    def find_direction(self):
        # pdb.set_trace()
        n0 = self.history[-2][0]
        n1 = self.history[-2][1]
        return DIRECTIONS[(n0[0] - n1[0], n0[1] - n1[1])]

    def distance_between(self, n1, n2):
        dr = n1[0] - n2[0]
        dc = n1[1] - n2[1]
        self.history.append((n1, n2))
        new_direction = DIRECTIONS[(dr, dc)]
        self.print_grid()
        if self.current_node != n1:
            self.current_node = n1
            self.direction = self.find_direction()
        if new_direction != self.direction:
            return 100
        return 1


def parse_input(input_data="input.txt"):
    grid = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        grid.append(list(line.strip()))
    return grid


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
    score = 0
    current_direction = 'EAST'
    for i in range(1, len(coordinates)):
        dr = coordinates[i][0] - coordinates[i - 1][0]
        dc = coordinates[i][1] - coordinates[i - 1][1]
        new_direction = DIRECTIONS[(dr, dc)]
        if new_direction != current_direction:
            current_direction = new_direction
            score += 1000
        score += 1
    return score


def is_valid(grid, x, y):
    return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.'


def part_one(input_data):
    grid = input_data
    start = locate(grid, "S")
    end = locate(grid, "E")
    astar_solver = GridAStar(start, grid)
    path = list(astar_solver.astar(start, end))
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
    # print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
