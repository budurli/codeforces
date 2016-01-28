# -*- coding: utf-8 -*-
n = int(raw_input())

center = n / 2
for i in xrange(n):
    row = map(lambda x: 'D' if abs(x - center) + abs(i-center) < center+1 else '*', xrange(n))
    print(''.join(row))
