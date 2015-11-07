# -*- coding: utf-8 -*-
x = raw_input()
result = ''
i = 0
for a in x:
    if int(a) > 4:
        if i == 0 and int(a) == 9:
            result += a
        else:
            result += str(9 - int(a))
    else:
        result += a
    i += 1

if int(result) == 0:
    print(x)
else:
    print(result)
