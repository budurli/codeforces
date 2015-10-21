# -*- coding: utf-8 -*-
n = int(raw_input())
a = map(int, raw_input().split(' '))
a.sort()
print(" ".join(map(str, a)))
