# -*- coding: utf-8 -*-
k, a, b = map(int, raw_input().split(' '))
result = 0
# print((b - a) / k + 1)
print((b - (a + (a % k)))/ k +1)
