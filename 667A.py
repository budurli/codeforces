# -*- coding: utf-8 -*-
from math import pi

d, h, v, e = map(float, raw_input().split())

initial_value = pi * h * (d / 2) ** 2

incoming = pi * e * (d / 2) ** 2
outcoming = v

if incoming >= outcoming:
    print('NO')
else:
    print('YES')
    print(initial_value / (outcoming - incoming))
