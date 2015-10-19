# -*- coding: utf-8 -*-
n = int(raw_input())

coords = map(int, raw_input().split(' '))
_min = coords[0]
_max = coords[-1]

for i in xrange(n):
    if i == 0:
        print('{} {}'.format(abs(coords[i] - coords[i + 1]), abs(_max - _min)))
    elif i == n - 1:
        print('{} {}'.format(abs(coords[i] - coords[i - 1]), abs(_max - _min)))
    else:
        print('{} {}'.format(
            min(abs(coords[i] - coords[i - 1]), abs(coords[i] - coords[i + 1])),
            max(abs(coords[i] - _min), abs(coords[i] - _max))
        ))
