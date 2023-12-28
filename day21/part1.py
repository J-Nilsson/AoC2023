import sys
import numpy as np

def get_neighbors(garden, pos):
    height, width = garden.shape
    neighbors = []

    if pos[0] < height - 1 and not garden[pos[0] + 1, pos[1]]:
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[0] > 0 and not garden[pos[0] - 1, pos[1]]:
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[1] < width - 1 and not garden[pos[0], pos[1] + 1]:
        neighbors.append((pos[0], pos[1] + 1))
    if pos[1] > 0 and not garden[pos[0], pos[1] - 1]:
        neighbors.append((pos[0], pos[1] - 1))
    
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

positions = set()
positions.add(start)
num_steps = 64

for step in range(num_steps):
    new_positions = set()
    for pos in positions:
        for n in get_neighbors(garden, pos):
            new_positions.add(n)
    
    positions = new_positions

print(len(positions))