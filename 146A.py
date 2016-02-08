# -*- coding: utf-8 -*-
import re

n = int(raw_input())
a = raw_input()
pattern = re.compile('(4|7)')

if len(pattern.sub('', a)) > 0:
    print('NO')
else:
    _f, _s = a[len(a) / 2:], a[:len(a) / 2]
    first_sum = sum(map(lambda x: int(x), _f))
    second_sum = sum(map(lambda x: int(x), _s))
    if first_sum == second_sum:
        print('YES')
    else:
        print('NO')
