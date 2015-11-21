# -*- coding: utf-8 -*-
n = int(raw_input())
home, away = [], []
result = 0
for i in xrange(n):
    _home, _away = map(int, raw_input().split(' '))
    home.append(_home)
    away.append(_away)

for color in home:
    result += away.count(color)

print(result)
