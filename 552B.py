# -*- coding: utf-8 -*-

n = raw_input()

multiplier = len(n)

for i in n:
    print(int(i) * multiplier)
    multiplier -= 1
