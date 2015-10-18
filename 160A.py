# -*- coding: utf-8 -*-
n = int(raw_input())
monet = map(int, raw_input().split(' '))
_sum = sum(monet)
_len = len(monet)
monet.sort(reverse=True)
x = 0
head = 0
tail = _sum
for i in xrange(_len):
    x += 1
    head += monet[i]
    tail -= monet[i]

    if head > tail:
        print(x)
        break
