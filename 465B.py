# -*- coding: utf-8 -*-
n = int(raw_input())
letters = map(int, raw_input().split())

result = 0
stream = False

for i in xrange(n):
    if letters[i]:
        if stream:
            result += 1
        else:
            result += 2
    else:
        if stream:
            result += 1
        stream = False

print(result)
