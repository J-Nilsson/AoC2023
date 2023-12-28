import sys
from heapq import heappop, heappush
import queue

slopes = {
    'v': (1, 0),
    '^': (-1, 0),
    '>': (0, 1),
    '<': (0, -1)
}

def get_neighbors(grid, pos):
    height = len(grid)
    width = len(grid[0])
    neighbors = []

    y, x = pos
    down = y + 1
    up = y - 1
    right = x + 1
    left = x - 1

    symb = grid[pos[0]][pos[1]]

    if symb in slopes.keys():
        cand = (pos[0] + slopes[symb][0], pos[1] + slopes[symb][1])
        if 0 <= cand[0] < height and 0 <= cand[1] < width:
            return [cand]

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
        if c_symb in slopes.keys() and cand[0] - pos[0] == -slopes[c_symb][0] and cand[1] - pos[1] == -slopes[c_symb][1]:
            continue
        if c_symb == '#':
            continue
        neighbors.append(cand)
    
    return neighbors

def get_succ(grid, pos):
    height = len(grid)
    width = len(grid[0])
    succs = []

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
        if c_symb in slopes.keys() and y - cand[0] == slopes[c_symb][0] and x - cand[1] == slopes[c_symb][1]:
            succs.append(cand)
    
    return succs 


def longest_path(grid, start, dest):
    dists = dict()
    dists[start] = 0

    finished = set()
    queue = []
    waiting = set()
    queue = [start]

    while queue:
        cur_node = queue.pop(0)
        if cur_node in finished:
            continue
        finished.add(cur_node)
        neighbors = get_neighbors(grid, cur_node)
        A = 1
        for neighbor in neighbors:
            if neighbor in finished: continue
            succs = get_succ(grid, neighbor)
            if len(succs) >= 2:
                if all([s in dists.keys() for s in succs]):
                    dists[neighbor] = max([dists[s] + 1 for s in succs])
                    waiting.discard(neighbor)
                    queue.append(neighbor)
            else:
                dists[neighbor] = dists[cur_node] + 1
                queue.append(neighbor)

    return dists[dest]

grid = []

for line in sys.stdin:
    line = line.strip()
    grid.append(line)

print(longest_path(grid, (0, 1), (140, 139)))