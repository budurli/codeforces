# -*- coding: utf-8 -*-
import operator

n = int(raw_input())
prices = []
qualities = []

for i in xrange(n):
    _p, _q = map(int, raw_input().split(' '))
    prices.append({'index': i, 'value': _p})
    qualities.append({'index': i, 'value': _q})

sorted_prices = sorted(prices, key=operator.itemgetter('value'))
sorted_qualities = sorted(qualities, key=operator.itemgetter('value'))

for i in xrange(n):
    if sorted_qualities[i]['index'] != sorted_prices[i]['index']:
        print('Happy Alex')
        break
else:
    print('Poor Alex')
