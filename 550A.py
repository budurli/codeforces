# -*- coding: utf-8 -*-
import re

s = raw_input()

first = re.compile('AB\w+BA')
second = re.compile('BA\w+AB')
if first.search(s) or second.search(s):
    print('YES')
else:
    print('NO')
