# -*- coding: utf-8 -*-
n = int(raw_input())

if n % 4 == 0:
    print('{} {}'.format(n / 2 - 2, n / 2 + 2))
elif n % 2 == 0:
    print('{} {}'.format(n / 2 - 3, n / 2 + 3))
else:
    middle = n / 2
    first = middle - middle % 3
    if first % 2 == 0:
        first += 3
    second = n - first
    print('{} {}'.format(first, second))
