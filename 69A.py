# -*- coding: utf-8 -*-
n = int(raw_input())
x = y = z = 0
for i in xrange(n):
    _x, _y, _z = map(int, raw_input().split(' '))
    x += _x
    y += _y
    z += _z

if (x == 0) and (y == 0) and (z == 0):
    print('YES')
else:
    print('NO')
