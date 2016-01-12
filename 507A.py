# -*- coding: utf-8 -*-
n, k = map(int, raw_input().split(' '))
a = map(int, raw_input().split(' '))
a = enumerate(a, 1)
result = 0

instrs = []

for i, a_i in sorted(a, key=lambda x: x[1]):
    result += a_i
    if result > k:
        break
    else:
        instrs.append(i)

print(len(instrs))
if len(instrs):
    print(' '.join(map(str, instrs)))
