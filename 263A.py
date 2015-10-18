# -*- coding: utf-8 -*-
result = 0
for i in [1, 2, 3, 4, 5]:
    row = map(int, raw_input().split(' '))
    if 1 in row:
        j = row.index(1)
        result = abs(i - 3) + abs(j - 2)

print(result)
