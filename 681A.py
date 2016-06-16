# -*- coding: utf-8 -*-

n = int(raw_input())

RED = 2400

for i in xrange(n):
    handle, before, after = raw_input().split()
    before = int(before)
    after = int(after)

    if before >= RED and (after > before):
        print('YES')
        break
else:
    print('NO')
