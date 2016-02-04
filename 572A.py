# -*- coding: utf-8 -*-
a, b = map(int, raw_input().split(' '))
k, m = map(int, raw_input().split(' '))
first = map(int, raw_input().split(' '))
second = map(int, raw_input().split(' '))

_max = first[k - 1]
index_max = -1

for i in xrange(b):
    if second[i] > _max:
        index_max = i
        break

if index_max > -1 and (b - index_max + 1) > m:
    print('YES')
else:
    print('NO')
