# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split(' '))
a_i = map(int, raw_input().split(' '))


def counts(_n):
    if _n % m != 0:
        return _n / m + 1
    return _n / m


a_i = zip(range(1, n + 1), map(lambda x: counts(x), a_i))

print(sorted(a_i, key=lambda x: x[1])[-1][0])
