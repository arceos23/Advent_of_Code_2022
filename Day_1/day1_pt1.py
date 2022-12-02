file = open('day1_input.txt', 'r')
lines = file.readlines()
file.close()

max_calorie_count = 0
i = 0
while i < len(lines):
    current_calorie_count = 0
    while i < len(lines) and lines[i] != '\n':
        current_calorie_count += int(lines[i])
        i += 1
    if (current_calorie_count > max_calorie_count):
        max_calorie_count = current_calorie_count
    i += 1

print(max_calorie_count)