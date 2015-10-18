# -*- coding: utf-8 -*-
n = int(raw_input())
start = raw_input()
end = raw_input()

result = 0
for i in xrange(n):
    rotation = abs(int(start[i]) - int(end[i]))
    if rotation <= 5:
        result += rotation
    else:
        result += (10 - rotation)

print result
