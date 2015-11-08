# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split(' '))

result = 0


def chunks(l, _n):
    for _i in xrange(0, len(l), _n):
        yield l[_i:_i + _n]


for i in xrange(n):
    windows = map(int, raw_input().split(' '))
    for flat in chunks(windows, 2):
        if sum(flat) > 0:
            result += 1

print(result)
