with open("input.txt", "r") as file:
    lines = file.readlines()

word_search = []
for line in lines:
    word_search.append(line.strip())


def search_dx(grid, r, c):
    mas_found = False
    top_left = grid[r - 1][c - 1]
    bottom_right = grid[r + 1][c + 1]
    if top_left == "M" and bottom_right == "S":
        mas_found = True
    if top_left == "S" and bottom_right == "M":
        mas_found = True
    return mas_found


def search_dy(grid, r, c):
    mas_found = False
    bottom_left = grid[r + 1][c - 1]
    top_right = grid[r - 1][c + 1]
    if bottom_left == "M" and top_right == "S":
        mas_found = True
    if bottom_left == "S" and top_right == "M":
        mas_found = True
    return mas_found


grid = [list(row) for row in word_search]

count = 0
# we start searching from 1 since there are no x-mas candidates on row 0
for r in range(1, len(grid)):
    for c in range(1, len(grid)):
        if (grid[r][c] == "A"):
            try:
                xmas_found = search_dx(grid, r, c) and search_dy(grid, r, c)
                if xmas_found:
                    count += 1
            except IndexError:
                continue

print(count)
