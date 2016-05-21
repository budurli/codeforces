# -*- coding: utf-8 -*-
n = int(raw_input())
m = int(raw_input())

flash = []
for i in xrange(n):
    flash.append(int(raw_input()))

flash.sort(reverse=True)

_sum = 0
result = 0
for f in flash:
    _sum += f
    result += 1
    if _sum >= m:
        print(result)
        break
