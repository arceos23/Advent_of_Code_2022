file = open('day8_input.txt', 'r')
forest = file.readlines()
file.close()

rows = len(forest)
cols = len(forest[0])
top_left_maxs = [[0] * cols] * rows
for row in range(rows):
    for col in range(cols - 1):
        tree = int(forest[row][col])
        if row == 0 and col == 0:
            top_left_maxs[row][col] = tree
        elif row == 0:
            top_left_maxs[row][col] = max(top_left_maxs[row][col - 1], tree)
        elif col == 0:
            top_left_maxs[row][col] = max(top_left_maxs[row - 1][col], tree)
        else:
            top_left_maxs[row][col] = max(top_left_maxs[row - 1][col - 1], tree)

bot_right_maxs = [[0] * cols] * rows
for row in range(rows - 1, -1, -1):
    for col in range(cols - 2, -1, -1):
        tree = int(forest[row][col])
        if row == rows - 1 and col == cols - 1:
            bot_right_maxs[row][col] = tree
        elif row == rows - 1:
            bot_right_maxs[row][col] = max(bot_right_maxs[row][col + 1], tree)
        elif col == cols - 1:
            bot_right_maxs[row][col] = max(bot_right_maxs[row + 1][col], tree)
        else:
            bot_right_maxs[row][col] = max(bot_right_maxs[row + 1][col + 1], tree)

visible_count = 0
for row in range(rows):
    for col in range(cols - 1):
        if row == 0 or row == len(forest) - 1:
            visible_count += 1
        elif col == 0 or col == row - 1:
            visible_count += 1
        else:
            tree = int(forest[row][col])
            if (tree > top_left_maxs[row - 1][col] or tree > top_left_maxs[row][col - 1]
                or tree > bot_right_maxs[row + 1][col] or tree > bot_right_maxs[row][col + 1]):
                visible_count += 1

print(visible_count)