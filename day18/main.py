from astar import AStar
import pdb


def parse_input(input_data="input.txt"):
    res = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        res.append(line.strip().split(","))
    res = [[int(element) for element in sublist] for sublist in res]
    return res


class PathFinder(AStar):
    def __init__(self, grid):
        self.grid = grid
        self.width = len(self.grid[0])
        self.height = len(self.grid)

    def neighbors(self, node):
        (x, y) = node
        possible_neighbors = [
            (x + 1, y), (x - 1, y),
            (x, y + 1), (x, y - 1)
        ]

        return [
            # pdb.set_trace()
            (nx, ny) for nx, ny in possible_neighbors
            if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[ny][nx] == '.'
        ]

    def distance_between(self, n1, n2):
        return 1

    def heuristic_cost_estimate(self, current, goal):
        return 1


def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print()


def corrupt_memory(grid, nr_bytes, input_data):
    new_grid = grid
    for data in range(nr_bytes):
        row = input_data[data][1]
        col = input_data[data][0]
        new_grid[row][col] = "#"
    return new_grid


def part_one(input_data):
    grid = [["." for _ in range(71)] for _ in range(71)]
    print("Before")
    print_grid(grid)
    corrupted_grid = corrupt_memory(grid, 1024, input_data)
    print("After")
    print_grid(corrupted_grid)
    pf = PathFinder(corrupted_grid)
    path = pf.astar((0,0),(70, 70))
    steps = len(list(path))
    return (steps - 1)


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
    # test_solution(part_one, "example.txt", 22)
    print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
