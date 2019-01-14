# -*- coding: utf-8 -*-
"""
В популярных системах электронных таблиц (например, в программе Excel)
используется следующая нумерация колонок. Первая колонка имеет номер A,
вторая B и т.д. до 26-ой, которая обозначается буквой Z. Затем идут
двухбуквенные обозначения: 27-ая обозначается как AA, 28-ая как AB, а
52-я обозначается парой AZ. Аналогично, следом за ZZ следуют трехбуквенные
обозначения и т.д.

Строки обычно обозначаются целыми числами от 1. Номер ячейки получается
конкатенацией обозначений для столбца и строки. Например, BC23 это
обозначение для ячейки в столбце 55, строке 23.

Иногда используется другая форма записи: RXCY, где X и Y это целые числа,
обозначающие номер строки и столбца, соответственно. Например, R23C55 это
ячейка из примера выше.

Ваша задача написать программу, которая считывает последовательность
обозначений ячеек и выводит каждое из обозначений в другой форме записи.
"""

import re

r_pattern = re.compile(r'R(\d+)C(\d+)')
o_pattern = re.compile(r'([A-Z]+)(\d+)')

# n = int(raw_input())

result = []


def s_to_i(s):  # str to int
    accum = 0
    multiplier = 0

    for i in s[::-1]:
        accum += (ord(i) - ord('A') + 1) * (26 ** multiplier)
        multiplier += 1

    return accum


def i_to_s(i):  # int to str
    if i < 27:
        r = chr(ord('A') + i - 1)
        print('{} == {}'.format(i, r))
        return r
    return i_to_s(i / 27) + i_to_s(i % 27)


def r_to_o(r, c):
    return 'Row: {}, Column: {}'.format(r, c)


def o_to_r(c, r):
    return 'Row: {}, Column: {}'.format(r, c)


# assert i_to_s(27) == 'AA'
# assert i_to_s(28) == 'AB'
# assert i_to_s(52) == 'AZ'
# print(i_to_s(52))
print(s_to_i('AZ'))
# for i in range(1, 10 ** 6):
#     assert i == s_to_i(i_to_s(i))

# print(s_to_i('AZ'))
# print(i_to_s(52))
# for _ in xrange(n):
#     i = raw_input()
#     r = r_pattern.findall(i)
#     if r:
#         result.append(r_to_o(*r[0]))
#     else:
#         o = o_pattern.findall(i)
#         result.append(o_to_r(*o[0]))
#
# print('\n'.join(result))
