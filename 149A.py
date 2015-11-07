# -*- coding: utf-8 -*-
k = int(raw_input())
months = map(int, raw_input().split(' '))

result = 0
i = 0
for month in sorted(months, reverse=True):
    if result >= k:
        print(i)
        break
    i += 1
    result += month
    if result >= k:
        print(i)
        break

else:
    print(-1)
