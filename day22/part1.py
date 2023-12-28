import sys
import numpy as np

bricks = []
z_min = 1e20
x_max = 0
y_max = 0
z_max = 0

for i, line in enumerate(sys.stdin):
    line = line.strip().split('~')
    start = list(map(int, line[0].split(',')))
    end = list(map(int, line[1].split(',')))
    z_min = min(z_min, start[2])
    x_max = max(x_max, end[0])
    y_max = max(y_max, end[1])
    z_max = max(z_max, end[2])
    bricks.append([[s, e] for s, e in zip(start, end)])

for brick in bricks:
    brick[2] = [brick[2][0] - z_min, brick[2][1] - z_min]

bricks = sorted(bricks, key=lambda x: x[2][0])
tower = np.full((x_max + 1, y_max + 1, z_max - z_min), False)

for brick in bricks:
    tower[brick[0][0]:brick[0][1] + 1, brick[1][0]:brick[1][1] + 1, brick[2][0]:brick[2][1] + 1] = True

for b in bricks:
    if b[2][0] == 0:
        continue

    below = np.any(tower[b[0][0]:b[0][1] + 1, b[1][0]:b[1][1] + 1, 0:b[2][0]], axis=(0, 1))
    tower[b[0][0]:b[0][1] + 1, b[1][0]:b[1][1] + 1, b[2][0]:b[2][1] + 1] = False

    top = np.where(below)[0]
    if len(top) > 0:
        top = top[-1]
        down_shift = b[2][0] - top - 1
    else:
        down_shift = b[2][0]

    b[2] = [b[2][0] - down_shift, b[2][1] - down_shift]
    tower[b[0][0]:b[0][1] + 1, b[1][0]:b[1][1] + 1, b[2][0]:b[2][1] + 1] = True

num_bricks = len(bricks)

bricks = sorted(bricks, key=lambda x: x[2][0])
for idx, b in enumerate(bricks):
    bricks[idx] = tuple(tuple(coords) for coords in b)

possible = {tuple(b): True for b in bricks}

for idx, b in enumerate(bricks[::-1]):
    real_idx = num_bricks - idx - 1
    supports = []
    for cand in bricks[real_idx::-1]:
        if b[2][0] == cand[2][1] + 1:
            if (b[0][0] > cand[0][1] or b[0][1] < cand[0][0]): continue
            if (b[1][0] > cand[1][1] or b[1][1] < cand[1][0]): continue
            supports.append(cand)
    
    if len(supports) == 1:
        possible[tuple(supports[0])] = False

choose_sum = 0
for k, v in possible.items():
    if v:
        choose_sum += 1

print(choose_sum)

