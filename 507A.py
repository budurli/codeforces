# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split(' '))
a = map(int, raw_input().split(' '))
result = 0
i = 0

for a_i in sorted(a):
    if result > k:
        print(i)
        break
    i += 1
    result += a_i
else:
    print(0)
