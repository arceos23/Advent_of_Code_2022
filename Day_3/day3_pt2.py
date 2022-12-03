file = open('day3_input.txt', 'r')
rucksacks = file.readlines()
file.close()

NUM_LETTERS = 26
ASCII_ADJ = 6
ELVES_PER_GROUP = 3

priority_sum = 0
for i in range(0, len(rucksacks), ELVES_PER_GROUP):
    rucksack_1_set = set(rucksacks[i])
    rucksack_2_set = set(rucksacks[i + 1])
    rucksack_3 = rucksacks[i + 2]

    for item in rucksack_3:
        if item in rucksack_1_set and item in rucksack_2_set:
            rescaled_priority = ord(item) - ord('A') + 1
            actual_priority = (rescaled_priority - NUM_LETTERS - ASCII_ADJ
            if rescaled_priority > NUM_LETTERS
            else rescaled_priority + NUM_LETTERS)
            priority_sum += actual_priority
            break

print(priority_sum)