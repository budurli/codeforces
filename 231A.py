# -*- coding: utf-8 -*-
n = int(raw_input())
result = 0
for i in xrange(n):
    if sum(map(int, raw_input().split(' '))) > 1:
        result += 1

print(result)
