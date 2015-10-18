# -*- coding: utf-8 -*-
import re

pattern = re.compile('[\w+]')

_set = raw_input()
print(len(set(pattern.findall(_set))))
