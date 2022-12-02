file = open('day2_input.txt', 'r')
lines = file.readlines()
file.close()

CHOICE_TO_POINTS = {'X': 1, 'Y': 2, 'Z': 3}
USER_DRAW_DICT = {'A': 'X', 'B': 'Y', 'C': 'Z'}
USER_WINS_DICT = {'A': 'Y', 'B': 'Z', 'C': 'X'}

total_score = 0
for line in lines:
    opponent_choice = line[0]
    user_choice = line[2]
    total_score += CHOICE_TO_POINTS[user_choice]
    if (USER_DRAW_DICT[opponent_choice] == user_choice) :
        total_score += 3
    elif (USER_WINS_DICT[opponent_choice] == user_choice):
        total_score += 6

print(total_score)