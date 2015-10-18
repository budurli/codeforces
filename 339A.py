# -*- coding: utf-8 -*-
numbers_in_string = map(int, raw_input().split('+'))
numbers_in_string.sort()
print '+'.join(map(str, numbers_in_string))
