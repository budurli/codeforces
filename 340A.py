# -*- coding: utf-8 -*-
from fractions import gcd

x, y, a, b = map(int, raw_input().split(' '))
lcm = (x * y) // gcd(x, y)
if a % lcm:
    first_range = a + lcm - a % lcm
else:
    first_range = a
print((b - first_range) / lcm + 1)
