# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split())
peoples = map(int, raw_input().split())

result = 0
accum = 0
for group in peoples:
    if accum + group > m:
        result += 1
        accum = group
    elif accum + group == m:
        result += 1
        accum = 0
    else:
        accum += group

if accum:
    result += 1
print(result)
