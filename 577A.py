# -*- coding: utf-8 -*-
table_width, x = map(int, raw_input().split(' '))


def factors(n):
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if
                       n % i == 0)))


number_for_research = min(table_width, int(x ** 0.5) + 1)

r = filter(lambda _x: _x <= table_width, factors(x))

if x > table_width:
    r.remove(1)

print(len(r))
