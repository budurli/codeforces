# -*- coding: utf-8 -*-
n, m = map(int, raw_input().split(' '))

max_scores = [0 for _i in range(m)]
bests = [0 for _i in range(m)]  # students

for i in xrange(n):
    scores = map(int, list(raw_input()))
    for _i, _s in enumerate(scores):
        if _s > max_scores[_i]:
            max_scores[_i] = _s
            bests[_i] = 1
        elif _s == max_scores[_i]:
            bests[_i] += 1


print(max_scores)
print(bests)


