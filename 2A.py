# -*- coding: utf-8 -*-
from collections import defaultdict

n = int(raw_input())
score = defaultdict(int)
max_score = 0
winner = None
for i in xrange(n):
    name, points = raw_input().split(' ')
    score[name] += int(points)
    if score[name] > max_score:
        max_score = score[name]
        winner = name

print(winner)
