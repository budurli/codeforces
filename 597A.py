# -*- coding: utf-8 -*-
import  math
k, a, b = map(int, raw_input().split(' '))
interval = b - a + 1

div = interval / float(k)

if a % k == 0:
    print(int(math.ceil(div)))
else:
    print(int(div))
