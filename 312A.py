# -*- coding: utf-8 -*-
import re

fred = re.compile('(.+)(lala)')
rainbow = re.compile('(miao\.)(.+)', re.DOTALL)

n = int(raw_input())
result = []
for i in xrange(n):
    sentence = raw_input()
    freds = fred.match(sentence)
    rainbows = rainbow.match(sentence)

    if freds and rainbows:
        print('OMG>.< I don\'t know!')

    elif not freds and not rainbows:
        print('OMG>.< I don\'t know!')

    elif freds:
        print('Freda\'s')

    elif rainbows:
        print('Rainbow\'s')
