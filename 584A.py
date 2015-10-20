# -*- coding: utf-8 -*-
n, t = map(int, raw_input().split(' '))

if t == 10:
    if n > 1:
        print(10 ** (n - 1))
    else:
        print(-1)
else:
    f = 10 ** (n - 1) % t
    print(10 ** (n - 1) + (t-f))
