# -*- coding: utf-8 -*-
x1, y1, x2, y2 = map(int, raw_input().split(' '))

x_length = abs(x1 - x2)
y_length = abs(y1 - y2)

if x_length != 0 and y_length != 0 and (x_length != y_length):
    print(-1)
else:
    side_length = max(x_length, y_length)
    if y1 == y2:
        if y1 + side_length < 1000:
            result = [x1, y1 + side_length, x2, y2 + side_length]
        else:
            result = [x1, y1 - side_length, x2, y2 - side_length]
    elif x1 == x2:
        if x1 + side_length < 1000:
            result = [x1 + side_length, y1, x2 + side_length, y2]
        else:
            result = [x1 - side_length, y1, x2 - side_length, y2]
    else:
        result = [x1, y2, x2, y1]

    print(' '.join(map(str, result)))
