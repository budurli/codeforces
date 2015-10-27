# -*- coding: utf-8 -*-
import re

s = raw_input()

pattern = re.compile('([h].*)([e].*)([l].*)([l].*)([o]).*')
if pattern.findall(s):
    print('YES')
else:
    print('NO')
