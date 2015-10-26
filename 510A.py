# -*- coding: utf-8 -*-
from itertools import cycle

n, m = map(int, raw_input().split(' '))
c = cycle(['.' * (m - 1) + '#', '#' + '.' * (m - 1)])
for i in xrange(n):
    if i % 2 == 0:
        print('#' * m)
    else:
        print(c.next())
