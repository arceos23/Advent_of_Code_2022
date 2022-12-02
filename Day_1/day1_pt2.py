from heapq import heappop, heappush, heapify

file = open('day1_input.txt', 'r')
lines = file.readlines()
file.close()

min_heap = []
heapify(min_heap)
i = 0
while i < len(lines):
    current_calorie_count = 0
    while i < len(lines) and lines[i] != '\n':
        current_calorie_count += int(lines[i])
        i += 1
    if len(min_heap) < 3:
        heappush(min_heap, current_calorie_count)
    elif current_calorie_count > min_heap[0]:
        heappop(min_heap)
        heappush(min_heap, current_calorie_count)
    i += 1

top_three_calorie_sum = 0
for i in min_heap:
    top_three_calorie_sum += i

print(top_three_calorie_sum)