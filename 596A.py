# -*- coding: utf-8 -*-
n = int(raw_input())
x, y = set(), set()

if n == 1:
    print('-1')
else:
    for i in xrange(n):
        _x, _y = map(int, raw_input().split(' '))
        x.add(_x)
        y.add(_y)
    if len(x) > 1 and len(y) > 1:
        x = list(set(x))
        y = list(set(y))
        print(abs(x[0]-x[1])*abs(y[0]-y[1]))
    else:
        print('-1')

