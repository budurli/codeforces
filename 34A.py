# -*- coding: utf-8 -*-
k = int(raw_input())
n = map(int, raw_input().split(' '))

min_diff = 1001
result = None
for i in xrange(1, k):
    if abs(n[i - 1] - n[i]) < min_diff:
        min_diff = abs(n[i - 1] - n[i])
        result = (i, i+1)

if abs(n[k-1] - n[0]) < min_diff:
    min_diff = abs(n[k-1] - n[0])
    result = (k, 1)

print(' '.join(map(str, result)))