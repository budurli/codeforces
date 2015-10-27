# -*- coding: utf-8 -*-
from collections import Counter

n = int(raw_input())
c = Counter(map(int, raw_input().split(' ')))
print('{} {}'.format(c.most_common(1)[0][1], len(c.items())))
