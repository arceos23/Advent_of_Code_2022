file = open('day6_input.txt', 'r')
datastream = file.readlines()
file.close()

MESSAGE_SIZE = 14

characters = datastream[0]
window = {}
window_size = MESSAGE_SIZE - 1
marker_index = -1
for i in range(len(characters)):
    current_char = characters[i]
    if i < window_size:
        window[current_char] = window.get(current_char, 0) + 1
    else:
        if current_char in window or len(window) < window_size:
            window[characters[i - window_size]] = window[characters[i - window_size]] - 1
            if window[characters[i - window_size]] == 0:
                del window[characters[i - window_size]]
            window[current_char] = window.get(current_char, 0) + 1
        else:
            marker_index = i + 1
            break

print(marker_index)