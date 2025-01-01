# import pdb
from functools import cache
import heapq


def parse_input(input_data="input.txt"):
    res = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        res.append(line.strip())
    return res


def part_one(input_data):
    grid = input_data
    start = (-1, -1)
    free_spaces = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            space = grid[r][c]
            if space == "E":
                end = (c, r)
                free_spaces.add((c, r))
            elif space == "S":
                start = (c, r)
                free_spaces.add((c, r))
            elif space == ".":
                free_spaces.add((c, r))
    visited = dijkstra(start, frozenset(free_spaces))
    return min(v for k, v in visited.items() if k[0] == end)


@cache
def dijkstra(start, free_spaces):
    deltas = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1),
    }
    rot = ">v<^"

    to_visit = []
    visited = {
        (start, ">"): 0,

    }

    heapq.heappush(to_visit, (0, ">", start))

    while to_visit:
        score, cd, (cx, cy) = heapq.heappop(to_visit)

        if ((cx, cy), cd) in visited and visited[((cx, cy), cd)] < score:
            continue

        dx, dy = deltas[cd]
        if (cx + dx, cy + dy) in free_spaces:
            np = (cx + dx, cy + dy)
            if (np, cd) not in visited or visited[(np, cd)] > score + 1:
                visited[(np, cd)] = score + 1
                heapq.heappush(to_visit, (score + 1, cd, np))

        for dr in [-1, 1]:
            nd = rot[(rot.index(cd) + dr) % 4]
            if ((cx, cy), nd) not in visited or visited[((cx, cy), nd)] > score + 1000:
                visited[((cx, cy), nd)] = score + 1000
                heapq.heappush(to_visit, (score + 1000, nd, (cx, cy)))

    return visited


def trace_back(visited, target_state):
    deltas = {
        ">": (1, 0),
        "v": (0, 1),
        "<": (-1, 0),
        "^": (0, -1),
    }
    rot = ">v<^"
    to_visit = [(target_state)]

    seen = set()
    while to_visit:
        cp, cd = to_visit.pop(0)

        seen.add(cp)
        dx, dy = deltas[cd]
        np = (cp[0] - dx, cp[1] - dy)
        if (np, cd) in visited and visited[(np, cd)] + 1 == visited[(cp, cd)]:
            to_visit.append((np, cd))

        nd1 = rot[(rot.index(cd) + 1) % 4]
        nd2 = rot[(rot.index(cd) - 1) % 4]

        if (cp, nd1) in visited and visited[(cp, nd1)] + 1000 == visited[(cp, cd)]:
            to_visit.append((cp, nd1))
        if (cp, nd2) in visited and visited[(cp, nd2)] + 1000 == visited[(cp, cd)]:
            to_visit.append((cp, nd2))

    return seen


def part_two(input_data):
    grid = input_data
    start = (-1, -1)
    free_spaces = set()
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            space = grid[r][c]
            if space == "E":
                end = (c, r)
                free_spaces.add((c, r))
            elif space == "S":
                start = (c, r)
                free_spaces.add((c, r))
            elif space == ".":
                free_spaces.add((c, r))
    visited = dijkstra(start, frozenset(free_spaces))
    target_score = min(v for k, v in visited.items() if k[0] == end)
    target_state = [k for k, v in visited.items() if v == target_score and k[0] == end]
    assert len(target_state) == 1
    return len(trace_back(visited, target_state[0]))


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
    test_solution(part_two, "example.txt", 45)
    print(f"Part 2 = {part_two(input_data)}")
