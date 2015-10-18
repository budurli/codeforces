# -*- coding: utf-8 -*-
n = int(raw_input())
result = 1
last_symb = None
for i in xrange(n):
    m = raw_input()
    if m[0] == last_symb:
        result += 1
    last_symb = m[1]

print(result)
