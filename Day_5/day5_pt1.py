from collections import deque
import re

file = open('day5_input.txt', 'r')
lines = file.readlines()
file.close()

END_CRATES_LINE_NUM = 9
NUM_STACKS = 9
START_LETTER = 1
NEXT_LETTER = 4
START_PROCEDURES = 11

deque_list = [deque() for i in range(NUM_STACKS)]
line_num = 1
for line in lines:
    if line_num < END_CRATES_LINE_NUM:
        letter_index = START_LETTER
        for i in range(NUM_STACKS):
            if line[letter_index].isalpha():
                deque_list[i].appendleft(line[letter_index])
            letter_index += NEXT_LETTER
    elif line_num >= START_PROCEDURES:
        temp = re.findall(r'\d+', line)
        rearrangement = list(map(int, temp))
        crates_to_move = rearrangement[0]
        from_index = rearrangement[1] - 1
        to_index = rearrangement[2] - 1
        for i in range(crates_to_move):
            deque_list[to_index].append(deque_list[from_index].pop())
    line_num += 1

top_crates = ""
for stack in deque_list:
    top_crates += stack[len(stack) - 1]
print(top_crates)