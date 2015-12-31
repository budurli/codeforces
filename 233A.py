# -*- coding: utf-8 -*-
import itertools
n = int(raw_input())
if n % 2 == 0:
    r = range(1, n + 1)
    r = itertools.chain.from_iterable(zip(r[1::2], r[::2]))
    print(' '.join(map(str, r)))
else:
    print(-1)
