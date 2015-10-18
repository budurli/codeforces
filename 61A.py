# -*- coding: utf-8 -*-
i = raw_input()
j = raw_input()
length = max(len(i), len(j))
i, j = map(lambda x: int(x, 2), [i, j])
print (bin(i ^ j)[2:]).zfill(length)
