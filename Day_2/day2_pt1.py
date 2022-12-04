file = open('day2_input.txt', 'r')
rounds = file.readlines()
file.close()

CHOICE_TO_POINTS = {'X': 1, 'Y': 2, 'Z': 3}
USER_DRAW_DICT = {'A': 'X', 'B': 'Y', 'C': 'Z'}
USER_WINS_DICT = {'A': 'Y', 'B': 'Z', 'C': 'X'}
DRAW_POINTS = 3
WIN_POINTS = 6

total_score = 0
for round in rounds:
    opponent_choice = round[0]
    user_choice = round[2]
    total_score += CHOICE_TO_POINTS[user_choice]
    if (USER_DRAW_DICT[opponent_choice] == user_choice) :
        total_score += DRAW_POINTS
    elif (USER_WINS_DICT[opponent_choice] == user_choice):
        total_score += WIN_POINTS

print(total_score)