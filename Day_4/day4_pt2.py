file = open('day4_input.txt', 'r')
assignment_pairs = file.readlines()
file.close()

ASSIGNMENT_PAIR_DELIMETER = ','
ASSIGNMENT_RANGE_DELIMETER = '-'

assignment_overlap_count = 0
for assignment_pair in assignment_pairs:
    assignments = assignment_pair.split(ASSIGNMENT_PAIR_DELIMETER)
    assignment_one_range = assignments[0].split(ASSIGNMENT_RANGE_DELIMETER)
    assignment_two_range = assignments[1].split(ASSIGNMENT_RANGE_DELIMETER)
    assignment_one_beg = int(assignment_one_range[0])
    assignment_one_end = int(assignment_one_range[1])
    assignment_two_beg = int(assignment_two_range[0])
    assignment_two_end = int(assignment_two_range[1])

    if assignment_one_beg >= assignment_two_beg and assignment_one_beg <= assignment_two_end:
        assignment_overlap_count += 1
    elif assignment_two_beg >= assignment_one_beg and assignment_two_beg <= assignment_one_end:
        assignment_overlap_count += 1

print(assignment_overlap_count)