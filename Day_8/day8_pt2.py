def calc_scenic_score(forest, row, col):
    tree = int(forest[row][col])
    top, bot, left, right = 1, 1, 1, 1
    top = get_top_dis(forest, row - 1, col, tree)
    bot = get_bot_dis(forest, row + 1, col, tree)
    left = get_left_dis(forest, row, col - 1, tree)
    right = get_right_dis(forest, row, col + 1, tree)
    return top * bot * left * right

def get_top_dis(forest, row, col, max_tree):
    if row == 0:
        return 1
    count = 0
    while row > 0 and int(forest[row][col]) < max_tree:
        count += 1
        row -= 1
    return count + 1

def get_bot_dis(forest, row, col, max_tree):
    if row >= len(forest) - 1:
        return 1
    count = 0
    while row < len(forest) - 1 and int(forest[row][col]) < max_tree:
        count += 1
        row += 1
    return count + 1

def get_left_dis(forest, row, col, max_tree):
    if col == 0:
        return 1
    count = 0
    while col > 0 and int(forest[row][col]) < max_tree:
        count += 1
        col -= 1
    return count + 1

def get_right_dis(forest, row, col, max_tree):
    if col >= len(forest[0]) - 1:
        return 1
    count = 0
    while col < len(forest[0]) - 1 and int(forest[row][col]) < max_tree:
        count += 1
        col += 1
    return count + 1

file = open('day8_input.txt', 'r')
forest = file.readlines()
file.close()

rows = len(forest)
cols = len(forest[0]) - 1
max_scenic_score = 0
for row in range(rows):
    for col in range(cols):
        max_scenic_score = max(max_scenic_score, calc_scenic_score(forest, row, col))

print(max_scenic_score)