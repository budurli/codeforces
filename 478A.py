# -*- coding: utf-8 -*-
c = map(int, raw_input().split(' '))
if sum(c) % 5 == 0 and sum(c) != 0:
    print(sum(c) / 5)
else:
    print(-1)
