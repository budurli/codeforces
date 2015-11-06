# -*- coding: utf-8 -*-
from collections import Counter, defaultdict
from itertools import combinations

n = int(raw_input())

counter_dict = defaultdict(int)

for i in xrange(n):
    new_word = raw_input()
    this_word_counter = Counter(new_word)
    counter_dict_update = this_word_counter.most_common()

    if len(counter_dict_update) == 1:
        counter_dict[counter_dict_update[0][0]] += counter_dict_update[0][1]

    if len(counter_dict_update) == 2:
        k1, k2 = sorted([counter_dict_update[0][0], counter_dict_update[1][0]])
        key = "{}_{}".format(k1, k2)

        counter_dict[key] += counter_dict_update[0][1] \
                             + counter_dict_update[1][1]

result = []

one_letter_keys = filter(lambda x: len(x) == 1, counter_dict.keys())
for letter_1, letter_2 in (combinations(one_letter_keys, 2)):
    result.append(
        counter_dict[letter_1]+counter_dict[letter_2]
    )

for key in counter_dict.keys():
    if len(key) == 1:
        result.append(counter_dict[key])

    if len(key) == 3:
        result.append(
            counter_dict[key] + counter_dict[key[0]] + counter_dict[key[-1]]
        )

if result:
    print(max(result))
else:
    print(0)
