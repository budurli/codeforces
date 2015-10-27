# -*- coding: utf-8 -*-
x = int(raw_input())

almost_lucky = [
    4, 7,
    44, 77, 47, 74,
    444, 447, 477, 474, 744, 747, 774, 777
]

for i in almost_lucky:
    if x % i == 0:
        print('YES')
        break

else:
    print('NO')
