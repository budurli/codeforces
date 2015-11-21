# -*- coding: utf-8 -*-
n = int(raw_input())

result = 0


def progression_sum(_n):
    # print('Progression for {}'.format(_n))
    if _n == 1:
        return 1.0
    return (1 + _n) / 2.0 * _n


for i in xrange(n):
    row = progression_sum(i+1)
    # print('Row: {}'.format(row))
    n -= row
    if n >= 0:
        result += 1
    else:
        break
print(result)
