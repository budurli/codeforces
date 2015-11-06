# -*- coding: utf-8 -*-
n, l = map(int, raw_input().split(' '))
a = map(int, raw_input().split(' '))

a.extend([0, l])

a = list(set(sorted(a)))

print(a)
print(map(lambda i: a[i] - a[i - 1], range(1, len(a))))
