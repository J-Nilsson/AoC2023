import sys
import numpy as np
from heapq import heappush, heappop

turns = {
    (0, 0): [(1, 0), (0, 1)],
    (1, 0): [(2, 0), (0, 1), (0, -1)],
    (2, 0): [(3, 0), (0, 1), (0, -1)],
    (3, 0): [(0, 1), (0, -1)],
    (0, 1): [(0, 2), (1, 0), (-1, 0)],
    (0, 2): [(0, 3), (1, 0), (-1, 0)],
    (0, 3): [(1, 0), (-1, 0)],
    (-1, 0): [(-2, 0), (0, 1), (0, -1)],
    (-2, 0): [(-3, 0), (0, 1), (0, -1)],
    (-3, 0): [(0, 1), (0, -1)],
    (0, -1): [(0, -2), (1, 0), (-1, 0)],
    (0, -2): [(0, -3), (1, 0), (-1, 0)],
    (0, -3): [(1, 0), (-1, 0)]
    }

def get_neighbors(node, height, width):
    pos = node[0]
    dir = node[1]
    avail_turns = turns[dir]
    neighbors = []
    for turn in avail_turns:
        move_0 = np.sign(turn[0])
        move_1 = np.sign(turn[1])
        if 0 <= pos[0] + move_0 < height and 0 <= pos[1] + move_1 < width:
            new_pos = (pos[0] + move_0, pos[1] + move_1)
            neighbors.append((new_pos, turn))
    return neighbors

def dijkstra(grid, start, dest):
    dists = dict()
    dir = (0, 0)
    dists[(start, dir)] = 0

    finished = set()

    height, width = grid.shape
    queue = []
    heappush(queue, (0, (start, dir)))

    while queue:
        cur_node_and_dist = heappop(queue)
        cur_node = cur_node_and_dist[1]
        if cur_node in finished:
            continue
        finished.add(cur_node)
        for neighbor in get_neighbors(cur_node, height, width):
            alt = dists[cur_node] + grid[neighbor[0]]
            if neighbor not in dists:
                dists[neighbor] = alt
                heappush(queue, (alt, neighbor))
            elif alt < dists[neighbor]:
                dists[neighbor] = alt
                heappush(queue, (alt, neighbor))
    min_dist = 1e20
    for t in turns.keys():
        if (dest, t) in dists:
            min_dist = min(min_dist, dists[(dest, t)])
    return min_dist

lines = []

for line in sys.stdin:
    line = line.strip()
    line = [int(c) for c in line]
    lines.append(line)

height = len(lines)
width = len(lines[0])
grid = np.array(lines, dtype=int)

start = (0, 0)
dest = (height - 1, width - 1)
print(dijkstra(grid, start, dest))