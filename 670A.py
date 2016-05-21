# -*- coding: utf-8 -*-
n = int(raw_input())

weeks = n / 7
_min = (n / 7) * 2

max_append = min(n % 7, 2)
min_append = max(n % 7 - 5, 0)
print('{} {}'.format(_min + min_append, _min + max_append))
