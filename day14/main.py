import pdb


def parse_input(input_data="input.txt"):
    res = []
    with open(input_data, 'r') as file:
        lines = file.readlines()
    for line in lines:
        position = line.strip().split(" ")[0][2:].split(",")
        position = [int(x) for x in position]
        velocity = line.strip().split(" ")[1][2:].split(",")
        velocity = [int(x) for x in velocity]
        res.append((position, velocity))
    return res


def move(w, h, position, velocity):
    width = w
    height = h
    x, y = position
    vx, vy = velocity
    new_x = (x + vx) % width
    new_y = (y + vy) % height
    return [new_x, new_y]


def find_quadrants(width, height, positions):
    mid_x = width / 2
    mid_y = height / 2

    quadrants = {
        "top_left": 0,
        "top_right": 0,
        "bottom_left": 0,
        "bottom_right": 0
    }

    for p, v in positions:
        x = p[0]
        y = p[1]
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x and y > mid_y:
            quadrants["top_left"] += 1
        elif x > mid_x and y > mid_y:
            quadrants["top_right"] += 1
        elif x < mid_x and y < mid_y:
            quadrants["bottom_left"] += 1
        elif x > mid_x and y < mid_y:
            quadrants["bottom_right"] += 1
    return quadrants


def multiply_quadrants(quadrants):
    return quadrants["top_left"] * quadrants["top_right"] * quadrants["bottom_left"] * quadrants["bottom_right"]


def find_positions(w, h, positions, iterations):
    all_positions = []
    for _ in range(iterations):
        new_positions = []
        for p, v in positions:
            new_pos = move(w, h, p, v)
            new_positions.append((new_pos, v))
        all_positions.extend(new_positions)
        positions = new_positions
    return all_positions


def part_one(input_data, w=101, h=103):
    positions = find_positions(w, h, input_data, 100)
    q = find_quadrants(w, h, positions)
    pdb.set_trace()
    return multiply_quadrants(q)


def part_two(input_data, w, h):
    return 0


def test_solution(func, input_data, result):
    GREEN = "\033[92m"
    RED = "\033[91m"
    RESET = "\033[0m"
    example_input_data = parse_input(input_data)
    expected_output = result
    actual_output = func(example_input_data, 11, 7)

    if actual_output == expected_output:
        print(f"Test for {func.__name__} - {GREEN}PASSED{RESET}: expected {actual_output}, got {actual_output}")
    else:
        print(f"Test for {func.__name__} - {RED}FAILED{RESET}: expected {expected_output}, got {actual_output}")


if __name__ == "__main__":
    input_data = parse_input()
    test_solution(part_one, "example.txt", 12)
    print(f"Part 1 = {part_one(input_data)}")
    # test_solution(part_two, "example.txt", 0)
    # print(f"Part 2 = {part_two(input_data)}")
