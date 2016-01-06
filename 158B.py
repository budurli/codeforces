# -*- coding: utf-8 -*-
from collections import Counter

n = int(raw_input())
groups = map(int, raw_input().split(' '))

counter = dict(Counter(groups))
taxi = 0

if counter.get(4, False):
    taxi += counter.get(4)
    counter[4] = 0

group_1_and_3 = min(counter.get(1, 0), counter.get(3, 0))

if group_1_and_3:
    counter[1] -= group_1_and_3
    counter[3] -= group_1_and_3
    taxi += group_1_and_3

group_2_and_1_and_1 = min(counter.get(2, 0), counter.get(1, 0) / 2)

if group_2_and_1_and_1:
    counter[2] -= group_2_and_1_and_1
    counter[1] -= group_2_and_1_and_1 * 2
    taxi += group_2_and_1_and_1

group_2_and_2 = counter.get(2, 0) / 2

if group_2_and_2:
    counter[2] -= group_2_and_2 * 2
    taxi += group_2_and_2

group_2_and_1 = min(counter.get(2, 0), counter.get(1, 0))

if group_2_and_1:
    counter[2] -= group_2_and_1
    counter[1] -= group_2_and_1
    taxi += group_2_and_1

group_1 = counter.get(1, 0) / 4

if group_1:
    counter[1] -= group_1 * 4
    taxi += group_1

if counter.get(1, 0):
    counter[1] = 0
    taxi += 1

print(taxi + sum(counter.values()))
