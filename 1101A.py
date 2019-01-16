# -*- coding: utf-8 -*-

q = int(raw_input())
result = []
for _ in xrange(q):
    l, r, d = map(int, raw_input().split())

    if d < l or r < d:
        result.append(str(d))
    else:
        result.append(str(r // d * d + d))

print('\n'.join(result))
