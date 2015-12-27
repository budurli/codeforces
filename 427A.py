# -*- coding: utf-8 -*-
n = int(raw_input())

events = map(int, raw_input().split(' '))

cops = 0
bads = 0
for i in xrange(n):
    if events[i] == -1:
        if cops > 0:
            cops -= 1
        else:
            bads += 1
    else:
        cops += events[i]

print(bads)
