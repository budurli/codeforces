# -*- coding: utf-8 -*-
n = int(raw_input())
capacity = 0
people_in_transport = 0

for i in xrange(n):
    _in, _out = map(int, raw_input().split(' '))
    people_in_transport -= _in
    people_in_transport += _out

    if people_in_transport > capacity:
        capacity = people_in_transport

print(capacity)
