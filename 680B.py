# -*- coding: utf-8 -*-
from itertools import izip_longest

n, a = map(int, raw_input().split())
t = map(int, raw_input().split())

result = t[a - 1]

after = t[a:]
before = t[:a - 1][::-1]

for l, r in izip_longest(after, before):
    if l and r:
        result += 2

    if (l is None and r is 1) or (l is 1 and r is None):
        result += 1

print(result)
