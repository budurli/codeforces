# -*- coding: utf-8 -*-
n = int(raw_input())

candies = range(1, n ** 2 + 1)

for i in xrange(0, n ** 2, n):
    row = []
    for j in xrange(i, i + n / 2):
        row.extend([candies[j], candies[n ** 2 - (j + 1)]])

    print(' '.join(map(str, row)))
