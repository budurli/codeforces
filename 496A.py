# -*- coding: utf-8 -*-
n = int(raw_input())
a_i = map(int, raw_input().split())

diffs = []
for i in xrange(1, n):
    diffs.append(a_i[i] - a_i[i - 1])
print(diffs)
