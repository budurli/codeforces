# -*- coding: utf-8 -*-
n = int(raw_input())
values = sorted(map(int, raw_input().split(' ')))

if min(values) == 1:
    print(-1)
else:
    print(1)

