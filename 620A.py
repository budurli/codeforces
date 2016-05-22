# -*- coding: utf-8 -*-
x_start, y_start = map(int, raw_input().split())
x_end, y_end = map(int, raw_input().split())

result = max(abs(x_end - x_start), abs(y_end - y_start))
print(result)
