# -*- coding: utf-8 -*-
from collections import defaultdict

n = int(raw_input())

names = defaultdict(list)
result = []
for i in xrange(n):
    name = raw_input()
    if len(names[name]) > 0:
        new_name = '{}{}'.format(name, len(names[name]))
        names[name].append(new_name)
        result.append(new_name)
    else:
        names[name].append(name)
        result.append('OK')

for r in result:
    print(r)
