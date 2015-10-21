# -*- coding: utf-8 -*-
from string import maketrans

r_transtab = maketrans(
    'qwertyuiop'
    'asdfghjkl;'
    'zxcvbnm,./',
    'wertyuiopp'
    'sdfghjkl;;'
    'xcvbnm,.//'
)

l_transtab = maketrans(
    'qwertyuiop'
    'asdfghjkl;'
    'zxcvbnm,./',
    'qqwertyuio'
    'aasdfghjkl'
    'zzxcvbnm,.'
)

direction = raw_input()
word = raw_input()

if direction == 'L':
    print(word.translate(r_transtab))
else:
    print(word.translate(l_transtab))
