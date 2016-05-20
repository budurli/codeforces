# -*- coding: utf-8 -*-

s, n = map(int, raw_input().split())
dragons_and_points = []

for i in xrange(n):
    dragons_and_points.append(tuple(map(int, raw_input().split())))

dragons_and_points.sort()

for power, treasure in dragons_and_points:
    if s > power:
        s += treasure
    else:
        print('NO')
        break
else:
    print('YES')