# -*- coding: utf-8 -*-
n = int(raw_input())
result = []
for i in xrange(n * n):
    if i < (n+1) or (i + 1) % n == 1:
        result.append(1)
    else:
        result.append(result[i - 1] + result[i - n])

print(result[-1])
