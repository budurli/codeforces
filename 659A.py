# -*- coding: utf-8 -*-
from collections import deque

n, a, b = map(int, raw_input().split())

d = deque(range(1, n + 1))

d.rotate(-a + 1)

d.rotate(-b)

print(d[0])
