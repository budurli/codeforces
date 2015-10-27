# -*- coding: utf-8 -*-
table_width, x = map(int, raw_input().split(' '))


print(min(table_width, int(x ** 0.5) + 1))
print(set(reduce(list.__add__,
                 ([i, x // i] for i in
                  range(1, min(table_width, int(x ** 0.5) + 1)) if
                  x % i == 0))))
