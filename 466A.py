# -*- coding: utf-8 -*-
n, m, a, b = map(int, raw_input().split(' '))

profit = m * a - b
if profit > 0:
    if n % m != 0:
        overhead = (n / m + 1) * b
        exact = (n / m) * b + (n % m) * a
        print(min(overhead, exact))
    else:
        print(n / m * b)
else:
    print(n * a)
