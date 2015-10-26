# -*- coding: utf-8 -*-

res = ''
for i in xrange(8):
    res += raw_input()

white_sum = res.count('Q') * 9 + res.count('R') * 5 + res.count('B') * 3 + res.count('N') * 3 + res.count('P')
black_sum = res.count('q') * 9 + res.count('r') * 5 + res.count('b') * 3 + res.count('n') * 3 + res.count('p')
if white_sum > black_sum:
    print('White')
elif white_sum < black_sum:
    print('Black')
else:
    print('Draw')
