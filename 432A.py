# -*- coding: utf-8 -*-

n, k = map(int, raw_input().split(' '))
y = map(int, raw_input().split(' '))

_n = 0
for i in xrange(n):
    if (5 - y[i]) >= k:
        _n += 1

print(_n / 3)
