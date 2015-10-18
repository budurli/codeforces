# -*- coding: utf-8 -*-
year = int(raw_input())

for i in xrange(year + 1, 9013):
    str_i = str(i)
    if len(str_i) == len(set(str_i)):
        print(str_i)
        break
