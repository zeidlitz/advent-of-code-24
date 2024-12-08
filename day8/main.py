def parse_input():
    with open("input.txt", 'r') as file:
        grid = []
        lines = file.readlines()
        for line in lines:
            grid.append(line.strip())
        grid = [list(row) for row in grid]
    return grid


def is_within_bounds(r, c, rows, columns):
    if r < 0 or r > rows:
        return False
    if c < 0 or c > columns:
        return False
    return True


def place_signal_on_antenna_map(r0, c0, r1, c1, dr, dc, rows, columns, result):
    north_r = -1 * dr
    north_c = -1 * dc
    south_r = dr
    south_c = dc
    north_signal_r = r0 + north_r
    north_signal_c = c0 + north_c
    south_signal_r = r1 + south_r
    south_signal_c = c1 + south_c
    if (is_within_bounds(north_signal_r, north_signal_c, rows, columns)):
        result.append((north_signal_r, north_signal_c))
    if (is_within_bounds(south_signal_r, south_signal_c, rows, columns)):
        result.append((south_signal_r, south_signal_c))


def find_row_column_differences(grid):
    result = []
    from collections import defaultdict
    positions = defaultdict(list)
    rows = len(grid)
    columns = len(grid[0])
    for row in range(rows):
        for col in range(columns):
            element = grid[row][col]
            if element != ".":
                positions[element].append((row, col))

    for element, pos_list in positions.items():
        for i in range(len(pos_list)):
            for j in range(i + 1, len(pos_list)):
                r0 = pos_list[i][0]
                c0 = pos_list[i][1]
                r1 = pos_list[j][0]
                c1 = pos_list[j][1]
                row_diff = r1 - r0
                col_diff = c1 - c0
                place_signal_on_antenna_map(r0, c0, r1, c1, row_diff, col_diff, rows, columns, result)

    return result


def part_one(input_data):
    antenna_grid = input_data
    result = find_row_column_differences(antenna_grid)
    result = list(set(result))
    return len(result)


def part_two(input_data):
    return 0


if __name__ == "__main__":
    input_data = parse_input()
    print(f"Part 1 = {part_one(input_data)}")
    print(f"Part 2 = {part_two(input_data)}")


"""
1. for every antenna, find other similar antennas
2. what is the row/column distance between them. For example a[1][3] and a[2][4] have a distance of [1][1], namely one should walk up and to the right to find the frequency.
3. Check if the frequency is within the bounds of the map
4. If within the bounds, mark the frequency on the frequency map

uncertainties:
- two different frequencies can occour at the same place?
- we should probably not count frequencies of same type in same place?
"""
