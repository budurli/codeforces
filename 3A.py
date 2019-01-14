# -*- coding: utf-8 -*-

start = raw_input().lower()
end = raw_input().lower()

sx, sy = ord(start[0]) - ord('a') + 1, int(start[1])
dx, dy = ord(end[0]) - ord('a') + 1, int(end[1])

n = 0
steps = []

while (sx, sy) != (dx, dy):
    n += 1
    if sx > dx:
        if sy > dy:
            steps.append('LD')
            sx -= 1
            sy -= 1
        elif sy == dy:
            steps.append('L')
            sx -= 1
        elif sy < dy:
            steps.append('LU')
            sx -= 1
            sy += 1

    elif sx == dx:
        if sy > dy:
            steps.append('D')
            sy -= 1
        elif sy < dy:
            steps.append('U')
            sy += 1

    elif sx < dx:
        if sy > dy:
            steps.append('RD')
            sx += 1
            sy -= 1
        elif sy == dy:
            steps.append('R')
            sx += 1
        elif sy < dy:
            steps.append('RU')
            sx += 1
            sy += 1

print(n)
print('\n'.join(steps))
