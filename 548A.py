# -*- coding: utf-8 -*-

def is_palindrome(_s):
    return bool(_s == str(_s)[::-1])


s = raw_input()
n = int(raw_input())

_len = len(s)
if _len % n != 0:
    print('NO')
    exit(0)

blocks = _len / n

words = [s[i:i + blocks] for i in range(0, _len, blocks)]
for w in words:
    if not is_palindrome(w):
        print('NO')
        break
else:
    print('YES')
