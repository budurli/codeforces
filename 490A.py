# -*- coding: utf-8 -*-
from collections import defaultdict

n = int(raw_input())
students = map(int, raw_input().split())

mapping = defaultdict(list)
counts = {1: 0, 2: 0, 3: 0}
for i in xrange(n):
    mapping[students[i]].append(i + 1)
    counts[students[i]] += 1

mapping = dict(mapping)

count = min(counts.values())
print(count)
for i in xrange(count):
    print('{} {} {}'.format(
        mapping[1][i],
        mapping[2][i],
        mapping[3][i],
    ))
