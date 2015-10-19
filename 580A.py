# -*- coding: utf-8 -*-
n = int(raw_input())
points = map(int, raw_input().split(' '))

result = 0
longest = 0
for i in xrange(1, n):
    if points[i] < points[i - 1]:
        longest = max(result, longest)
        result = 0
    else:
        result += 1


print(max(result, longest) + 1)
