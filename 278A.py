# -*- coding: utf-8 -*-
n = int(raw_input())
d = map(int, raw_input().split(' '))
s, t = map(int, raw_input().split(' '))

s, t = min(s, t), max(s, t)

first = sum(d[s - 1:t - 1])
d_copy = d[t - 1:]
d_copy.extend(d[:s - 1])
second = sum(d_copy)
print(min(first, second))
