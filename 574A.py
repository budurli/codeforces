# -*- coding: utf-8 -*-
n = int(raw_input())
voices = map(int, raw_input().split(' '))
bribe = 0
voices[1:] = sorted(voices[1:])

while voices[0] <= voices[n - 1]:
    voices[0] += 1
    voices[n - 1] -= 1
    bribe += 1
    voices[1:] = sorted(voices[1:])

print(bribe)
