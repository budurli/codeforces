# -*- coding: utf-8 -*-
n, h = map(int, raw_input().split())
a = map(int, raw_input().split())

higher = filter(lambda x: x > h, a)
len_higher = len(higher)
print(len(a) + len_higher)
