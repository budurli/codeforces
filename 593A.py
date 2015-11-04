# -*- coding: utf-8 -*-
from collections import Counter, defaultdict

n = int(raw_input())

words = []
count = Counter()
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

print dict(counter_dict)

