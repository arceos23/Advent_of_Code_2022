file = open('day3_input.txt', 'r')
rucksacks = file.readlines()
file.close()

NUM_LETTERS = 26
ASCII_ADJ = 6

priority_sum = 0
for rucksack in rucksacks:
    rucksack_len = len(rucksack)    
    midpoint = int(rucksack_len / 2)
    first_compartment = set(rucksack[0:midpoint])

    for i in range(midpoint, rucksack_len):
        item = rucksack[i]
        if item in first_compartment:
            rescaled_priority = ord(item) - ord('A') + 1
            actual_priority = (rescaled_priority - NUM_LETTERS - ASCII_ADJ
            if rescaled_priority > NUM_LETTERS
            else rescaled_priority + NUM_LETTERS)
            priority_sum += actual_priority
            break

print(priority_sum)