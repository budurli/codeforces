# -*- coding: utf-8 -*-
n = int(raw_input())

for y in xrange(2 * n + 1):
    row = [n - (abs(x - n) + abs(y - n)) for x in xrange(2 * n + 1)]
    row = map(lambda x: str(x) if x >= 0 else ' ', row)
    row = ' '.join(row)
    row = row.rstrip()
    print(row)
