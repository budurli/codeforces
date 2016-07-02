# -*- coding: utf-8 -*-
key = raw_input()
value = raw_input()

if '.' in value:
    print('f{}'.format(key.capitalize()))
else:
    print('i{}'.format(key.capitalize()))
