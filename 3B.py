# -*- coding: utf-8 -*-

n, v = map(int, raw_input().split())
final_v = 0
boats = []
result = []
for i in xrange(n):
    t, _v = map(int, raw_input().split())
    boats.append((i + 1, t, _v, _v / float(t)))

boats.sort(key=lambda x: x[3], reverse=True)
for boat in boats:
    if boat[1] <= v:
        final_v += boat[2]
        result.append(str(boat[0]))
        v -= boat[1]

print(final_v)
print(' '.join(result))
