# -*- coding: utf-8 -*-
import re

pattern = re.compile('BG')
n, t = map(int, raw_input().split(' '))
queue = raw_input()

for i in xrange(t):
    queue = pattern.sub('GB', queue)
print(queue)
