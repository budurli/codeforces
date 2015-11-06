# -*- coding: utf-8 -*-
from operator import itemgetter

n = int(raw_input())
x1, x2 = map(int, raw_input().split(' '))
x1 += 0.0000001
x2 -= 0.0000001
k = []
b = []
positive = False

starts, ends = [], []

for i in xrange(n):
    new_k, new_b = map(int, raw_input().split(' '))
    starts.append({
        'index': i,
        'value': new_k * x1 + new_b
    })
    ends.append({
        'index': i,
        'value': new_k * x2 + new_b
    })

starts.sort(key=itemgetter('value'))
ends.sort(key=itemgetter('value'))

for i in xrange(n):
    if starts[i]['index'] != ends[i]['index']:
        print('YES')
        break
else:
    print('NO')
