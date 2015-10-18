# -*- coding: utf-8 -*-
k, n, w = map(int, raw_input().split(' '))
_sum = 0
for i in xrange(1, w + 1):
    _sum += k * i
print(max(0, _sum - n))
