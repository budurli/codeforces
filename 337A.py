# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split(' '))

f = map(int, raw_input().split(' '))

f.sort()
_min = 1001
for i in xrange(0, m - n + 1):
    diff = f[i + n - 1] - f[i]
    if diff == 0:
        print('0')
        break

    if diff < _min:
        _min = diff

else:
    print(_min)
