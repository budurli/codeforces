# -*- coding: utf-8 -*-
from fractions import gcd

a, b = map(int, raw_input().split(' '))

print((a * b) // gcd(a, b))
