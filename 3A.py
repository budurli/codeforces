# -*- coding: utf-8 -*-

start = raw_input()
end = raw_input()

letters_map = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8
}

start_position = (letters_map[start[0]], int(start[1]))
end_position = (letters_map[end[0]], int(end[1]))

x_moves = abs(start_position[0] - end_position[0])
y_moves = abs(start_position[1] - end_position[1])

diag_moves = min(x_moves, y_moves)

additional_moves = min(diag_moves - x_moves, diag_moves - y_moves)
result_moves = diag_moves + additional_moves

print(diag_moves + additional_moves)

current_position = start_position

for i in xrange(result_moves):
    offset = (
        end_position[0] - current_position[0],
        end_position[1] - current_position[1]
    )

    if offset[0] > 0 and offset[1] > 0:
        current_position = (
            current_position[0]+1,
            current_position[1]+1
        )
        print('RU')
    elif offset[0] > 0 and offset[1] == 0:
        current_position = (
            current_position[0]+1,
            current_position[1]
        )
        print('R')
    elif offset[0] == 0 and offset[1] > 0:
        current_position = (
            current_position[0],
            current_position[1]+1
        )
        print('U')
