# -*- coding: utf-8 -*-
n, m, a, b = map(int, raw_input().split(' '))
print(min(n * a, round(n / float(m)) * b))
