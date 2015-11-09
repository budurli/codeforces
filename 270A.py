# -*- coding: utf-8 -*-
t = int(raw_input())
result = []
for i in xrange(t):
    x = int(raw_input())
    if x == 180:
        result.append('NO')
    else:
        n = 360 / float(180 - x)
        if n.is_integer():
            result.append('YES')
        else:
            result.append('NO')

for i in result:
    print(i)
