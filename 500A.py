# -*- coding: utf-8 -*-
n, t = map(int, raw_input().split(' '))
cells = map(int, raw_input().split(' '))

number = 1
while True:
    if number == t:
        print('YES')
        break
    elif number > t:
        print('NO')
        break
    else:
        number += cells[number-1]
