# -*- coding: utf-8 -*-
from collections import defaultdict

n = int(raw_input())

points = []

points_by_x = defaultdict(list)
points_by_y = defaultdict(list)
group_x = []
group_y = []
for i in xrange(n):
    point = tuple(map(int, raw_input().split()))

    points_by_x[point[0]].append(point)
    points_by_y[point[1]].append(point)

for key, value in points_by_x.items():
    if len(value) > 2:
        group_x.extend(sorted(value)[1:-1])

for key, value in points_by_y.items():
    if len(value) > 2:
        group_y.extend(sorted(value)[1:-1])

print(len(set(group_x) & set(group_y)))
