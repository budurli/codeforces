# -*- coding: utf-8 -*-
from collections import Counter

n = int(raw_input())
s = Counter(raw_input())

pattern = ''
for key, value in s.iteritems():
    if value % n == 0:
        pattern += key * (value / n)
    else:
        print('-1')
        break
else:
    print(pattern * n)
