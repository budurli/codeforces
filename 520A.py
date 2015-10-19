# -*- coding: utf-8 -*-
n = int(raw_input())
word = raw_input()


if len(set(word.lower())) == 26:
    print('YES')
else:
    print('NO')
