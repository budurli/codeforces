# -*- coding: utf-8 -*-
n = int(raw_input())
first_row = map(int, raw_input().split(' '))
second_row = map(int, raw_input().split(' '))
third_row = map(int, raw_input().split(' '))

print [item for item in first_row if item not in second_row]
print [item for item in second_row if item not in third_row]