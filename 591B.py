# -*- coding: utf-8 -*-
from collections import defaultdict
n, m = map(int, raw_input().split(' '))
brand = raw_input()

c = defaultdict(list)
result = range(n)

for i in xrange(n):
    c[brand[i]].append(i)

for i in xrange(m):
    _from, _to = raw_input().split(' ')
    c[_from], c[_to] = c[_to], c[_from]


for key, indexes in dict(c).iteritems():
    if indexes:
        for i in indexes:
            result[i] = key

print("".join(result))