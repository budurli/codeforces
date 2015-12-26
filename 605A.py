# -*- coding: utf-8 -*-
n = int(raw_input())
vagouns = map(int, raw_input().split(' '))
middle = n / 2.0
result = 0
for i in xrange(n):
    print('i: {}, vagoun: {}, middle: {}'.format(i+1, vagouns[i], middle))
    if (vagouns[i] >= middle and (i + 1) < middle) or (
                    vagouns[i] <= middle and (i + 1) > middle):
        result += 1

print(result)
