# -*- coding: utf-8 -*-
n = int(raw_input())
ranks = map(int, raw_input().split(' '))
a, b = map(int, raw_input().split(' '))

print sum(ranks[a-1:b-1])
