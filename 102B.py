# -*- coding: utf-8 -*-


def sum_digits(n):
    return str(sum(map(int, n)))


n = raw_input()

i = 0
for _ in xrange(4):

    if int(n) < 10:
        break
    i += 1
    n = sum_digits(n)

print(i)
