# -*- coding: utf-8 -*-
a = int(raw_input(), 2)

binary = '{0:b}'.format(a)
if '0' in binary:
    binary = binary.replace('0', '', 1)
else:
    binary = binary.replace('1', '', 1)
print(binary)
