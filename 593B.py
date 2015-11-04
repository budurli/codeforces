# -*- coding: utf-8 -*-
n = int(raw_input())
x1, x2 = map(int, raw_input().split(' '))
k = []
b = []
positive = False

for i in xrange(n):
    new_k, new_b = map(int, raw_input().split(' '))
    k.append(new_k)
    b.append(new_b)
    if not positive and i > 0:
        for j in xrange(i):
            if k[i] != k[j]:
                if x1 < ((b[j] - b[i]) / float((k[i] - k[j]))) < x2:
                    positive = True

if positive:
    print('YES')
else:
    print('NO')
