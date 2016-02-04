# -*- coding: utf-8 -*-
from itertools import combinations
n = int(raw_input())

ranks = sorted(map(int, raw_input().split(' ')))

diff = ranks[n - 1] - ranks[0]

has_next_iteration = True
left_pointer = 0
right_pointer = n - 1

if diff != 0:
    count = len(filter(lambda x: x == ranks[n - 1], ranks)) * len(
            filter(lambda x: x == ranks[0], ranks))
else:
    count = len(list(combinations(ranks, 2)))
print('{} {}'.format(diff, count))
