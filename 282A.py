# -*- coding: utf-8 -*-
n = int(raw_input())
x = 0
for i in xrange(n):
    operation = raw_input()
    if '+' in operation:
        x += 1
    else:
        x -= 1

print(x)
