# -*- coding: utf-8 -*-
n = int(raw_input())
result = range(n)

ratings = enumerate(map(int, raw_input().split()))

ratings = sorted(ratings, key=lambda x: x[1], reverse=True)

position = 1
group_count = 0
max_rating = ratings[0][1]
for number, rating in ratings:
    if rating < max_rating:
        position += group_count
        max_rating = rating
        group_count = 1
    else:
        group_count += 1
    result[number] = position

print(u' '.join(map(str, result)))
