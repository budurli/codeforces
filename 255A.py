# -*- coding: utf-8 -*-
n = int(raw_input())
ex = map(int, raw_input().split())

chest = sum(ex[0::3])
biceps = sum(ex[1::3])
back = sum(ex[2::3])
_max = max(chest, biceps, back)

if _max == chest:
    print('chest')

if _max == biceps:
    print('biceps')

if _max == back:
    print('back')
