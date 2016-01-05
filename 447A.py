# -*- coding: utf-8 -*-

p, n = map(int, raw_input().split(' '))

result = dict()

for i in xrange(n):
    number = int(raw_input())
    key = number % p

    if result.get(key) is not None:
        print(i + 1)
        break
    else:
        result[key] = number
else:
    print('-1')
