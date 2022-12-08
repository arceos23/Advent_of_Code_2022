file = open('day8_input.txt', 'r')
forest = file.readlines()
file.close()

rows = len(forest)
cols = len(forest[0]) - 1

# Build 2D array for max tree towards the top of a given tree 
top_maxs = [[0 for i in range(cols)] for j in range(rows)]
for row in range(rows):
    for col in range(cols):
        tree = int(forest[row][col])
        if row == 0:
            top_maxs[row][col] = tree
        else:
            top_maxs[row][col] = max(top_maxs[row - 1][col], tree)

# Build 2D array for max tree towards the bottom of a given tree 
bot_maxs = [[0 for i in range(cols)] for j in range(rows)]
for row in range(rows - 1, -1, -1):
    for col in range(cols - 1, -1, -1):
        tree = int(forest[row][col])
        if row == rows - 1:
            bot_maxs[row][col] = tree
        else:
            bot_maxs[row][col] = max(bot_maxs[row + 1][col], tree)

visible_count = 0
counted = [[0 for i in range(cols)] for j in range(rows)]
# Increment count of trees visible from top or left
for row in range(rows):
    max_left = -1
    for col in range(cols):
        tree = int(forest[row][col])
        if row == 0 or col == 0 or row == rows - 1 or col == cols - 1:
            visible_count += 1
            counted[row][col] = True
        elif tree > top_maxs[row - 1][col] or tree > max_left:
            visible_count += 1
            counted[row][col] = True
        max_left = max(max_left, tree)

# Increment count of trees visible from bottom or right
for row in range(rows - 1, -1, -1):
    max_right = -1
    for col in range(cols - 1, -1, -1):
        tree = int(forest[row][col])
        if row == 0 or col == 0 or row == rows - 1 or col == cols - 1 or counted[row][col]:
            max_right = max(max_right, tree)
            continue
        elif tree > bot_maxs[row + 1][col] or tree > max_right:
            visible_count += 1
        max_right = max(max_right, tree)

print(visible_count)