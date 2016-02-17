# -*- coding: utf-8 -*-
n, x = map(int, raw_input().split(' '))
numbers = map(int, raw_input().split(' '))

_sum = abs(sum(numbers))

if _sum % x == 0:
    print(_sum / x)
else:
    print(_sum / x + 1)
