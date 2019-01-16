# -*- coding: utf-8 -*-
import operator

n, w, h = map(int, raw_input().split())

envs = []

for i in xrange(n):
    _w, _h = map(int, raw_input().split())
    if (_w >= w) and (_h >= h):
        envs.append((i + 1, _w, _h))

# envs_by_w = sorted(envs, key=operator.itemgetter(1, 2))
# envs_by_h = sorted(envs, key=operator.itemgetter(2, 1))
envs = sorted(envs, key=operator.itemgetter(1, 2))

result = []
c = 0
for env in envs:
    n, _w, _h = env
    if (_w > w) and (_h > h):
        result.append(str(n))
        c += 1
        w, h = _w, _h

print(c)
print(' '.join(result))
