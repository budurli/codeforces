# -*- coding: utf-8 -*-
n = int(raw_input())
p = map(int, raw_input().split(' '))
result = [0 for x in p]
for i in xrange(len(p)):
    result[p[i]-1] = i+1
print(u' '.join(map(str, result)))



