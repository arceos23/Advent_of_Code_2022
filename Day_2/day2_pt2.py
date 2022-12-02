file = open('day2_input.txt', 'r')
lines = file.readlines()
file.close()

CHOICE_TO_POINTS = {'X': 1, 'Y': 2, 'Z': 3}
USER_LOSES_DICT = {'A': 'Z', 'B': 'X', 'C': 'Y'}
USER_DRAW_DICT =  {'A': 'X', 'B': 'Y', 'C': 'Z'}
USER_WINS_DICT =  {'A': 'Y', 'B': 'Z', 'C': 'X'}

total_score = 0
for line in lines:
    opponent_choice = line[0]
    user_choice = line[2]
    if user_choice == 'X':
        total_score += CHOICE_TO_POINTS[USER_LOSES_DICT[opponent_choice]]
    elif user_choice == 'Y':
        total_score += 3
        total_score += CHOICE_TO_POINTS[USER_DRAW_DICT[opponent_choice]]
    elif user_choice == 'Z':
        total_score += 6
        total_score += CHOICE_TO_POINTS[USER_WINS_DICT[opponent_choice]]

print(total_score)