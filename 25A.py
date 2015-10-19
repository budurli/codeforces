# -*- coding: utf-8 -*-
n = int(raw_input())
numbers = map(int, raw_input().split(' '))
odds = []
evens = []
for i in xrange(n):
    if numbers[i] % 2 == 1:
        odds.append(i)
    else:
        evens.append(i)

if len(odds) > len(evens):
    print(evens[0] + 1)
else:
    print(odds[0] + 1)
