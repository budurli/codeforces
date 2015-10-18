# -*- coding: utf-8 -*-
n = int(raw_input())
groups = map(int, raw_input().split(' '))

max_taxi = len(groups)

_1 = groups.count(1)
_2 = groups.count(2)
_3 = groups.count(3)
_4 = groups.count(4)

group_1_and_3 = min(_1, _3)

group_2_and_2 = _2 / 2
