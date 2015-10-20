# -*- coding: utf-8 -*-
a, b, s = map(int, raw_input().split(' '))
if (abs(a) + abs(b)) <= s and (abs(a) + abs(b) - s) % 2 == 0:
    print('YES')
else:
    print('NO')
