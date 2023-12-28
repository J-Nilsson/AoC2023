import sys
import numpy as np
import matplotlib.pyplot as plt

def get_neighbors(garden, pos, garden_mults):
    height, width = garden.shape
    neighbors = []

    y, x = pos
    down = y + 1
    up = y - 1
    right = x + 1
    left = x - 1

    cands = (
        (down % height, x, 0 if y < height - 1 else 1, 0),
        (up % height, x, 0 if y > 0 else -1, 0),
        (y, right % width, 0, 0 if x < width - 1 else 1),
        (y, left % width, 0, 0 if x > 0 else -1),        
    )

    for cand in cands:
        if garden[cand[:2]]: continue

        new_mults = set()
        for mult in garden_mults:
            new_mults.add((mult[0] + cand[2], mult[1] + cand[3]))
        neighbors.append((cand[0], cand[1], new_mults))
    
    return neighbors


lines = []
start = None

for row_idx, line in enumerate(sys.stdin):
    line = line.strip()

    col_idx = line.find('S')
    if col_idx != -1:
        start = (row_idx, col_idx)
    
    row = [1 if c == '#' else 0 for c in line]
    lines.append(row)

garden = np.array(lines)

positions = dict()
positions[start] = {(0, 0)}
num_steps = 2 * garden.shape[0] + garden.shape[0] // 2

for step in range(num_steps):
    print(step)
    new_positions = dict()
    for pos, mults in positions.items():
        for n in get_neighbors(garden, pos, mults):
            if (n[0], n[1]) not in new_positions:
                new_positions[(n[0], n[1])] = set()
            new_positions[(n[0], n[1])].update(n[2])
    
    positions = new_positions

mult_counts = dict()

for p, mults in positions.items():
    for m in mults:
        if m not in mult_counts.keys():
            mult_counts[m] = 0
        mult_counts[m] += 1

def position_count(k, mult_counts):
    res = 0
    res += mult_counts[(1, 0)] * k ** 2
    res += mult_counts[(0, 0)] * (k - 1) ** 2
    res += mult_counts[(2, 0)]
    res += mult_counts[(-2, 0)]
    res += mult_counts[(0, 2)]
    res += mult_counts[(0, -2)]
    res += mult_counts[(1, 1)] * (k - 1)
    res += mult_counts[(-1, 1)] * (k - 1)
    res += mult_counts[(1, -1)] * (k - 1)
    res += mult_counts[(-1, -1)] * (k - 1)
    res += mult_counts[(2, 1)] * k
    res += mult_counts[(2, -1)] * k
    res += mult_counts[(-2, 1)] * k
    res += mult_counts[(-2, -1)] * k

    return res

N = 26501365 // garden.shape[0]
print(position_count(N, mult_counts))