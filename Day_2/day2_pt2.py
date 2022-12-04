file = open('day2_input.txt', 'r')
rounds = file.readlines()
file.close()

CHOICE_TO_POINTS = {'X': 1, 'Y': 2, 'Z': 3}
USER_LOSES_DICT = {'A': 'Z', 'B': 'X', 'C': 'Y'}
USER_DRAW_DICT =  {'A': 'X', 'B': 'Y', 'C': 'Z'}
USER_WINS_DICT =  {'A': 'Y', 'B': 'Z', 'C': 'X'}
DRAW_POINTS = 3
WIN_POINTS = 6

total_score = 0
for round in rounds:
    opponent_choice = round[0]
    user_choice = round[2]
    if user_choice == 'X':
        total_score += CHOICE_TO_POINTS[USER_LOSES_DICT[opponent_choice]]
    elif user_choice == 'Y':
        total_score += DRAW_POINTS
        total_score += CHOICE_TO_POINTS[USER_DRAW_DICT[opponent_choice]]
    elif user_choice == 'Z':
        total_score += WIN_POINTS
        total_score += CHOICE_TO_POINTS[USER_WINS_DICT[opponent_choice]]

print(total_score)