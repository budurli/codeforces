# -*- coding: utf-8 -*-
from fractions import gcd

a, b, n = map(int, raw_input().split(' '))

move = 0
while True:
    if move % 2 == 0:
        if n >= gcd(a, n):
            n -= gcd(a, n)
        else:
            break
    else:
        if n >= gcd(b, n):
            n -= gcd(b, n)
        else:
            break
    move += 1

print([1, 0][move % 2])
