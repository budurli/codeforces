# -*- coding: utf-8 -*-

n = int(raw_input())

result = []

for i in range(n):
    if i % 2 == 0:
        result.append('I hate')
    else:
        result.append('I love')

    if i == n-1:
        result.append('it')
    else:
        result.append('that')

print(u' '.join(result))
