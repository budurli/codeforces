# -*- coding: utf-8 -*-
rooms = int(raw_input())

result = 0
for i in xrange(rooms):
    p, q = map(int, raw_input().split(' '))
    if (q - p) >= 2:
        result += 1

print(result)
