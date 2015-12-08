# -*- coding: utf-8 -*-
n = int(raw_input())
_x, _y = [], []
result = []

for i in xrange(n * n):
    x, y = map(int, raw_input().split(' '))
    if (x not in _x) and (y not in _y):
        _x.append(x)
        _y.append(y)
        result.append(str(i + 1))
print(' '.join(result))
