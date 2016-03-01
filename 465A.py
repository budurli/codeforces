# -*- coding: utf-8 -*-
n = int(raw_input())

number = raw_input()

diff = 0
one = True

for i in xrange(n):
    if number[i] == '1' and one:
        diff += 1
        one = True
    if number[i] == '0' and one:
        diff += 1
        one = False

print(diff)
