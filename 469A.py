# -*- coding: utf-8 -*-
n = int(raw_input())

p = set(filter(lambda x: x, map(int, raw_input().split(' '))[1:]))
q = set(filter(lambda x: x, map(int, raw_input().split(' '))[1:]))

if len(p | q) >= n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
