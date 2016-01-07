# -*- coding: utf-8 -*-
a, b = map(int, raw_input().split(' '))

candles = a
candle_ends = 0
hours = 0

while True:
    hours += candles
    candle_ends += candles

    candles = candle_ends / b
    candle_ends = candle_ends % b

    if candle_ends < b and candles == 0:
        print(hours)
        break

