# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split(' '))
number = map(int, raw_input().split(' '))
result = 0
last_point = 1
for i in number:
    if i > last_point:
        result += i - last_point
    elif i < last_point:
        result += n - (last_point - i)
    else:
        result += 0

    last_point = i

print(result)
