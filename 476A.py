# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split(' '))

max_steps = n
min_steps = n / 2 + n % 2
if m > max_steps:
    print('-1')
else:
    if min_steps % m != 0:
        print(min_steps + (m - min_steps % m))
    else:
        print(min_steps)
