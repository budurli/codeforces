# -*- coding: utf-8 -*-
import re

n = int(raw_input())

word = raw_input()

names = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon",
         "glaceon", "sylveon"]


def to_re(_str):
    result = ''
    for i in _str:
        if i == '.':
            result += '.{1}'
        else:
            result += i
    return re.compile(result)


pattern = to_re(word)

for name in filter(lambda x: len(x) == n, names):
    match = pattern.findall(name)
    if match:
        print(match[0])
        break
