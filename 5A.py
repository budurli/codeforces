# -*- coding: utf-8 -*-

import sys

s, u = 0, 0
for line in sys.stdin:
    if line[0] == '+':
        u += 1
    elif line[0] == '-':
        u -= 1
    else:
        s += len(line.rstrip().split(':')[1]) * u
print(s)
