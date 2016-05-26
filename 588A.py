# -*- coding: utf-8 -*-
n = int(raw_input())

history = []
min_price = '+inf'

accum = 0
for i in xrange(n):
    meat, price = map(int, raw_input().split(' '))
    if price < min_price:
        min_price = price
    accum += min_price * meat

print(accum)
