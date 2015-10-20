# -*- coding: utf-8 -*-
import re

pattern = re.compile('[A-Z]')
word = raw_input()
_length = len(word)
if len(pattern.findall(word)) > _length / 2:
    print(word.upper())
else:
    print(word.lower())
