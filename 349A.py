# -*- coding: utf-8 -*-
n = int(raw_input())

money = map(int, raw_input().split(' '))

cash = {
    '25': 0,
    '50': 0,
    '100': 0
}

for i in xrange(n):
    incoming = money[i]
    cash[str(incoming)] += 1

    cashback = incoming - 25

    if cashback == 25:
        if cash['25'] > 0:
            cash['25'] -= 1
        else:
            print('NO')
            break

    elif cashback == 75:
        if cash['50'] > 0 and cash['25'] > 0:
            cash['50'] -= 1
            cash['25'] -= 1
        elif cash['50'] == 0 and cash['25'] > 2:
            cash['25'] -= 3
        else:
            print('NO')
            break
else:
    print('YES')
