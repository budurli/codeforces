# -*- coding: utf-8 -*-
n = int(raw_input())
a = map(int, raw_input().split(' '))

for i in xrange(1, n-1):
    if sum(a[i-1], a[i], a[i+1])>1:
        a[i]