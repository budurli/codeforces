# -*- coding: utf-8 -*-
import re

n, k = map(int, raw_input().split(' '))
numbers = raw_input().split(' ')

pattern = re.compile('(4|7)')
result = 0

for _n in numbers:
    if len(pattern.findall(_n)) <= k:
        result += 1

print(result)
