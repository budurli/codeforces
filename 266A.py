# -*- coding: utf-8 -*-
n = int(raw_input())
stones = raw_input()
_len = len(stones)
x = 0
for i in xrange(_len-1):
    if stones[i] == stones[i + 1]:
        x += 1

print(x)
