import time


def get_list_from_file():
    with open("input.txt", 'r') as file:
        return file.read().splitlines()


def find_route(visited, start_pos, next_row, next_col, grid):
    row_count = len(grid)
    col_count = len(grid[0])
    curr_row, curr_col = start_pos
    while True:
        # Add coords to visited
        visited.add((curr_row, curr_col))
        # Bounds check (is guard gonna leave)
        if curr_row + next_row < 0 or curr_row + next_row >= row_count or curr_col + next_col < 0 or curr_col + next_col >= col_count:
            break
        # Check for obstacle else move
        if grid[curr_row + next_row][curr_col + next_col] == "#":
            next_col, next_row = -next_row, next_col
        else:
            curr_row += next_row
            curr_col += next_col


def find_looped_route(start_pos, next_row, next_col, grid):
    row_count = len(grid)
    col_count = len(grid[0])
    curr_row, curr_col = start_pos
    visited = set()

    while True:
        visited.add((curr_row, curr_col, next_row, next_col))
        if curr_row + next_row < 0 or curr_row + next_row >= row_count or curr_col + next_col < 0 or curr_col + next_col >= col_count:
            break
        if grid[curr_row + next_row][curr_col + next_col] == "#":
            next_col, next_row = -next_row, next_col
        else:
            curr_row += next_row
            curr_col += next_col
        if (curr_row, curr_col, next_row, next_col) in visited:
            return True


def part_one(data_input):
    total = 0
    visited = set()
    grid = [list(row) for row in data_input]
    start_pos = None
    for row_idx, row in enumerate(grid):
        if "^" in row:
            col_idx = row.index("^")
            start_pos = (row_idx, col_idx)

    next_row, next_col = -1, 0
    find_route(visited, start_pos, next_row, next_col, grid)

    total = len(visited)

    return total


def part_two(data_input):
    total = 0
    grid = [list(row) for row in data_input]
    start_pos = None
    for row_idx, row in enumerate(grid):
        if "^" in row:
            col_idx = row.index("^")
            start_pos = (row_idx, col_idx)
    next_row, next_col = -1, 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != ".":
                continue
            grid[row][col] = "#"
            if find_looped_route(start_pos, next_row, next_col, grid):
                total += 1
            grid[row][col] = "."

    return total


if __name__ == "__main__":
    t1 = time.time()

    input_data = get_list_from_file()

    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")

    t2 = time.time()
    print(f"Executed in {t2 - t1:0.4f} seconds")
