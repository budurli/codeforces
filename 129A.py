# -*- coding: utf-8 -*-
n = int(raw_input())
cookies = map(int, raw_input().split())

odd = 0
even = 0
for i in xrange(n):
    if cookies[i] % 2 == 0:
        even += 1
    else:
        odd += 1

if odd % 2 == 0:
    print(even)
else:
    print(odd)
