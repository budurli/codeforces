# -*- coding: utf-8 -*-
a, b = map(int, raw_input().split(' '))

count = 0
while a != b:
    if a > b:
        count += (a / b)
        a = a % b
    elif b > a:
        count += (b / a)
        b = b % a

    if a == 0 or b == 0:
        break

print(count)
