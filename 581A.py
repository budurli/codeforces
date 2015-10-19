# -*- coding: utf-8 -*-
a, b = map(int, raw_input().split(' '))
k, j = min(a, b), max(a, b)
print('{} {}'.format(k, (j - k) / 2))
