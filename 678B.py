# -*- coding: utf-8 -*-

y = int(raw_input())

if ((y % 4 == 0) and (y % 100 != 0)) or (y % 400 == 0):
    print(y + 28)
else:
    print(y + 6)
