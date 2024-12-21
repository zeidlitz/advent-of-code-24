import pdb
from astar import AStar

DIRECTIONS = {
    (0, 1): "WEST",
    (0, -1): "EAST",
    (-1, 0): "SOUTH",
    (1, 0): "NORTH"
}


def parse_input(input_data="input.txt"):
    grid = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        grid.append(list(line.strip()))
    return grid


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


def countsegs(segset):
    ret, points = 0,set()
    for a, b,c,d in segset:
        ret += abs(a-c) + abs(b-d) + 1 - ((a, b) in points) - ((c,d) in points)
        points.update({(a, b),(c,d)})
    return ret


def dijkstra(data, start,end):
    import heapq
    from collections import defaultdict
    dirs = [(1, 0),(0,1),(-1,0),(0,-1)]
    distances = defaultdict(lambda:(float("inf"), set()))
    distances[*start, 1] = (0, set())
    queue = [(0, * start, 1)]
    while queue:
        dist, px,py,di = heapq.heappop(queue)
        _, p_set = distances[(px, py, di)]
        for ndi in range(-1, 2):
            dix, diy = dirs[(di + ndi) % 4]
            npx, npy, ndist = px + dix, py + diy, dist + 1 + 1000 * (ndi != 0)
            while (data[npx][npy] != "#" and data[npx + diy][npy+dix] == "#" and data[npx-diy][npy-dix] == "#"):
                npx, npy, ndist = npx + dix, npy + diy, ndist + 1

            nset = p_set | {seg(px, py, npx, npy)}

            if (npx, npy) == end:
                return (ndist, countsegs(nset))

            if data[npx][npy] != "#":
                o_dist, o_set = distances[(npx, npy, (di + ndi) % 4)]
                if o_dist == ndist:
                    if any((pos not in o_set) for pos in nset):
                        o_set.update(nset)
                        heapq.heappush(queue, (ndist,npx,npy,(di + ndi) % 4))
                elif o_dist > ndist:
                    distances[(npx, npy, (di + ndi) % 4)] = (ndist, nset)
                    heapq.heappush(queue, (ndist, npx, npy, (di + ndi) % 4))
    return distances


def part_one(input_data):
    grid = input_data
    start = locate(grid, "S")
    end = locate(grid, "E")
    print(dijkstra(grid, start, end))
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
