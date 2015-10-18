# -*- coding: utf-8 -*-
n = int(raw_input())


def _sum(i):
    if i % 2 == 0:
        return i / 2
    else:
        return _sum(i - 1) - i


print(_sum(n))
