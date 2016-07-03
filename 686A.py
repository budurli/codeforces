# -*- coding: utf-8 -*-
n, x = map(int, raw_input().split())

sad_children = 0

for i in xrange(n):
    sign, delta = raw_input().split()
    delta = int(delta)
    if sign == '-':
        if (x - delta) >= 0:
            x -= delta
        else:
            sad_children += 1
    elif sign == '+':
        x += delta

print('{} {}'.format(x, sad_children))
