import sys
import queue
from copy import copy
from functools import lru_cache
import matplotlib.pyplot as plt

def get_neighbors(grid, pos):
    height = len(grid)
    width = len(grid[0])
    neighbors = []

    y, x = pos
    down = y + 1
    up = y - 1
    right = x + 1
    left = x - 1

    cands = (
        (up, x),
        (down, x),
        (y, left),
        (y, right)
    )

    for cand in cands:
        if cand[0] < 0 or cand[0] >= height or cand[1] < 0 or cand[1] > width:
            continue
        c_symb = grid[cand[0]][cand[1]]
        if c_symb == '#':
            continue
        neighbors.append(cand)
    
    return neighbors

def longest_path(start, dest, nodes, prev_path, depth):
    length = 0
    cur_pos = start
    if start == dest:
        return 0
    while True:
        if cur_pos == dest:
            return length
        prev_path.add(cur_pos)
        if len(nodes[cur_pos]) == 1:
            neighbor = next(iter(nodes[cur_pos]))
            if neighbor[1] in prev_path:
                return -1
            length += neighbor[0]
            cur_pos = neighbor[1]
        else:
            max_cont_dist = 0
            for neighbor in nodes[cur_pos]:
                dist = neighbor[0]
                pos = neighbor[1]
                if pos in prev_path:
                    continue
                cont_path = longest_path(pos, dest, nodes, copy(prev_path), depth+1)
                if cont_path > -1:
                    max_cont_dist = max(max_cont_dist, dist + cont_path)
            length += max_cont_dist
            break
    return -1 if max_cont_dist == 0 else length

grid = []

for i, line in enumerate(sys.stdin):
    line = line.strip()
    grid.append(line)

start = (0, 1)
dest = (140, 139)

node_poss = set()
node_poss.add(start)
node_poss.add(dest)

for r_idx, row in enumerate(grid):
    for c_idx, col in enumerate(row):
        pos = (r_idx, c_idx)
        if col != '#' and len(get_neighbors(grid, pos)) > 2:
            node_poss.add(pos)

nodes = dict()

for node in node_poss:
    q = []
    q.append((0, node))
    visited = set()
    visited.add(node)
    while q:
        cur_node = q.pop(0)
        dist = cur_node[0]
        cur_node = cur_node[1]
        for n in get_neighbors(grid, cur_node):
            if n in visited:
                continue
            if n in node_poss:
                if node not in nodes.keys():
                    nodes[node] = set()
                nodes[node].add((dist + 1, n))
            else:
                q.append((dist + 1, n))
            visited.add(n)

print(longest_path(start, dest, nodes, set(), 0))