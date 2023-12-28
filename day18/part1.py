import sys
import numpy as np
from collections import deque

def get_neighbors(pos, trench):
    height, width = trench.shape
    y, x = pos
    neighbors = []

    cands = ((y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1))

    for cand in cands:
        if 0 <= cand[0] < height and 0 <= cand[1] < width and not trench[cand[0], cand[1]]:
            neighbors.append(cand)

    return neighbors

def bfs(trench):
    inside_loop = np.zeros_like(trench)

    candidates = set()
    for row_idx in range(1, trench.shape[0] - 1):
        for col_idx in range(1, trench.shape[1] - 1):
            if not trench[row_idx, col_idx]:
                candidates.add((row_idx, col_idx))
    
    while candidates:
        start = candidates.pop()
        visited = set()
        queue = deque()
        queue.append(start)
        visited.add(start)
        broke_out = False
        while queue:
            pos = queue.popleft()
            candidates.discard(pos)
            if pos[0] in (0, height - 1) or pos[1] in (0, width - 1):
                broke_out = True
                break
            neighbors = get_neighbors(pos, trench)
            for n in neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        
        if not broke_out:
            for pos in visited:
                inside_loop[pos[0], pos[1]] = 1
    
    return inside_loop

dirs = {
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1),
    'U': (-1, 0)
}

xs = [0]
ys = [0]

for line in sys.stdin:
    line = line.strip().split()
    dir = line[0]
    n = int(line[1])
    for hole in range(int(n)):
        ys.append(ys[-1] + dirs[dir][0])
        xs.append(xs[-1] + dirs[dir][1])

ys = [y - min(ys) for y in ys]
xs = [x - min(xs) for x in xs]
height = max(ys) + 1
width = max(xs) + 1

trench = np.zeros((height, width), dtype=int)
for y, x in zip(ys, xs):
    trench[y, x] = 1

volume = np.sum(trench) + np.sum(bfs(trench))

print(volume)