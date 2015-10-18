# -*- coding: utf-8 -*-
n = int(raw_input())
points = map(int, raw_input().split(' '))

_max = _min = points[0]
result = 0
for i in xrange(1, n):
    if points[i] > _max:
        _max = points[i]
        result += 1

    if points[i] < _min:
        _min = points[i]
        result += 1

print(result)
