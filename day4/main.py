with open("input.txt", "r") as file:
    lines = file.readlines()

word_search = []
for line in lines:
    word_search.append(line)


# def count_word_occurrences(grid, word):
#     def check_direction(x, y, dx, dy):
#         for i in range(len(word)):
#             nx, ny = x + i * dx, y + i * dy
#             if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
#                 return False
#         return True
#
#     def count_from_cell(x, y):
#         directions = [
#             (0, 1),
#             (1, 0),
#             (0, -1),
#             (-1, 0),
#             (1, 1),
#             (1, -1),
#             (-1, 1),
#             (-1, -1)
#         ]
#         count = 0
#         for dx, dy in directions:
#             if check_direction(x, y, dx, dy):
#                 count += 1
#         return count
#
#     total_count = 0
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             total_count += count_from_cell(i, j)
#
#     return total_count


# part 2
def count_x_mas_occurrences(grid):
    def check_x_mas(x, y):
        positions = [
            (-1, -1),
            (-1, 1),
            (1, -1),
            (1, 1)
        ]

        for dx1, dy1 in positions:
            for dx2, dy2 in positions:
                if dx1 == -dx2 and dy1 == -dy2:
                    if check_mas(x + dx1, y + dy1, -dx1, -dy1) and check_mas(x + dx2, y + dy2, -dx2, -dy2):
                        return True
        return False

    def check_mas(x, y, dx, dy):
        mas = "MAS"
        for i in range(3):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= len(grid) or ny >= len(grid[0]) or grid[nx][ny] != mas[i]:
                return False
        return True

    total_count = 0
    for i in range(1, len(grid) - 1):  # Avoid edges
        for j in range(1, len(grid[0]) - 1):  # Avoid edges
            if check_x_mas(i, j):
                total_count += 1

    return total_count


grid = [list(row) for row in word_search]
word = "XMAS"
result = count_x_mas_occurrences(grid)

print("Total occurrences of '{}': {}".format(word, result))
