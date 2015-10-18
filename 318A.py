# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split(' '))

if k < round(n / 2.0) + 1:
    print(k * 2 - 1)
else:
    print(int((k - round(n / 2.0)) * 2))
