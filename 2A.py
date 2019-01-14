# -*- coding: utf-8 -*-

n = int(raw_input())
winner = None

steps = []

score = {}
max_individual_score = {}
final_score = {}

for i in xrange(n):
    name, points = raw_input().split(' ')
    steps.append((name, int(points)))

    if name not in score.keys():
        score[name] = int(points)
        max_individual_score[name] = int(points)
    else:
        score[name] += int(points)

    if score[name] > max_individual_score[name]:
        max_individual_score[name] = score[name]

max_score = max(score.values())

for name, points in steps:
    final_score[name] = final_score.get(name, 0) + points

    if final_score[name] >= max_score and score[name] == max_score:
        print(name)
        break
