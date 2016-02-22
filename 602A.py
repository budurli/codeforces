# -*- coding: utf-8 -*-
n_x, b_x = map(int, raw_input().split(' '))
x = map(int, raw_input().split(' '))
n_y, b_y = map(int, raw_input().split(' '))
y = map(int, raw_input().split(' '))

result_1 = 0
for i in xrange(n_x):
    result_1 += x[i] * (b_x ** (n_x - i - 1))

result_2 = 0
for i in xrange(n_y):
    result_2 += y[i] * (b_y ** (n_y - i - 1))

if result_1 > result_2:
    print('>')
elif result_1 == result_2:
    print('=')
elif result_1 < result_2:
    print('<')
