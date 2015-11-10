# -*- coding: utf-8 -*-
a = map(int, raw_input().split(' '))
s = raw_input()
result = 0
for i in s:
    result += a[int(i)-1]

print(result)
