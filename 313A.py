# -*- coding: utf-8 -*-
from copy import copy

n = list(raw_input())

if int("".join(n)) >= 0:
    print("".join(n))
else:
    f = copy(n)
    del f[-1]
    f = int("".join(f))

    s = copy(n)
    del s[-2]
    s = int("".join(s))
    print(max(s, f))
