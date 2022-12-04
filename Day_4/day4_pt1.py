file = open('day4_input.txt', 'r')
assignment_pairs = file.readlines()
file.close()

ASSIGNMENT_PAIR_DELIMETER = ','
ASSIGNMENT_RANGE_DELIMETER = '-'

full_assignment_overlap_count = 0
for assignment_pair in assignment_pairs:
    assignments = assignment_pair.split(ASSIGNMENT_PAIR_DELIMETER)
    assignment_one = assignments[0]
    assignment_two = assignments[1]
    assignment_one_sections = assignment_one.split(ASSIGNMENT_RANGE_DELIMETER)
    assignment_two_sections = assignment_two.split(ASSIGNMENT_RANGE_DELIMETER)
    assignment_one_beg = int(assignment_one_sections[0])
    assignment_one_end = int(assignment_one_sections[1])
    assignment_two_beg = int(assignment_two_sections[0])
    assignment_two_end = int(assignment_two_sections[1])

    if assignment_one_beg >= assignment_two_beg and assignment_one_end <= assignment_two_end:
        full_assignment_overlap_count += 1
    elif assignment_two_beg >= assignment_one_beg and assignment_two_end <= assignment_one_end:
        full_assignment_overlap_count += 1

print(full_assignment_overlap_count)