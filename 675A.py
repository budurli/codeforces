# -*- coding: utf-8 -*-

a, b, c = map(int, raw_input().split())

if a == b:
    print('YES')
    exit(0)
if c == 0:
    print('NO')
    exit(0)

if ((b - a) % c == 0):
    if (a < b) and c > 0:
        print('YES')
        exit(0)

    elif (a > b) and c < 0:
        print('YES')
        exit(0)

print('NO')
