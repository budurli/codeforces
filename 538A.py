# -*- coding: utf-8 -*-
import re

source = raw_input()
pattern = re.compile('(.*?)([C])(.*?)([O])(.*?)([D])(.*?)([E])(.*?)([F])(.*?)([O])(.*?)([R])(.*?)([C])(.*?)([E])(.*?)([S])(.*?)', re.DOTALL)

if pattern.findall(source):
    print('YES')
else:
    print('NO')

"""
MDBUWCZFFZKFMJTTJFXRHTGRPREORKDVUXOEMFYSOMSQGHUKGYCRCVJTNDLFDEWFS
     C                     O  D    E F  O          RC        E  S
"""