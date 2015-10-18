# -*- coding: utf-8 -*-
word = raw_input()
if len(word) == 1:
    print(word.swapcase())
else:
    if word.isupper() or (word[0].islower() and word[1:].isupper()):
        print(word.swapcase())
    else:
        print(word)
