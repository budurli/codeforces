# -*- coding: utf-8 -*-
import re

pattern = re.compile('(01|10)')
n = int(raw_input())
_str = raw_input()

actual_length = n
for i in xrange(n):
    k = pattern.findall(_str)
    if k:
        _str = pattern.sub('', _str)
        actual_length -= len(k) * 2
    else:
        print(actual_length)
        break
