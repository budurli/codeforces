# -*- coding: utf-8 -*-
n = int(raw_input())
numbers = map(int, raw_input().split())

numbers.sort(reverse=True)

result = 0
odd = 0
for i in numbers:
    if i % 2 == 0:
        result += i
    else:
        if odd:
            result += odd
            result += i

            odd = 0
        else:
            odd = i

print(result)
