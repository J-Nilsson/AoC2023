import sys
from collections import deque

pipes = {
     '|': [(1, 0), (-1, 0)],
     '-': [(0, 1), (0, -1)],
     'L': [(-1, 0), (0, 1)],
     'J': [(-1, 0), (0, -1)],
     '7': [(1, 0), (0, -1)],
     'F': [(1, 0), (0, 1)],
     '.': [],
}

def get_loop_map(start, pipemap, start_move):
    cur_pos = start
    cur_move = start_move
    length = 0
    loop_map = [[False for _ in pipemap[0]] for _ in pipemap]
    loop_map[start[0]][start[1]] = True
    loop_moves = [[[-2, -2] for _ in pipemap[0]] for _ in pipemap]
    loop_moves[start[0]][start[1]] = start_move
    while True:
        length += 1
        cur_pos = (cur_pos[0] + cur_move[0], cur_pos[1] + cur_move[1])
        loop_map[cur_pos[0]][cur_pos[1]] = True
        if cur_pos == start:
            return loop_map, loop_moves
        
        cur_options = pipemap[cur_pos[0]][cur_pos[1]]
        if len(cur_options) == 0:
            return None, None
        if cur_move[0] == -cur_options[0][0] and cur_move[1] ==-cur_options[0][1]:
            cur_move = cur_options[1]
        elif cur_move[0] == -cur_options[1][0] and cur_move[1] ==-cur_options[1][1]:
            cur_move = cur_options[0]
        else:
            return None, None
        loop_moves[cur_pos[0]][cur_pos[1]] = cur_move

def get_boundaries(loop_map):
    left = 1e20
    right = 0
    top = 1e20
    bottom = 0

    for row_idx, row in enumerate(loop_map):
        for col_idx, col in enumerate(row):
            if col:
                left = min(left, col_idx)
                right = max(right, col_idx)
                top = min(top, row_idx)
                bottom = max(bottom, row_idx)
    
    return left, right, top, bottom

def get_neighbors(pos, loop_map, loop_moves):
    neighbors = []
    up = int(pos[0] - 0.5)
    down = int(pos[0] + 0.5)
    left = int(pos[1] - 0.5)
    right = int(pos[1] + 0.5)

    if pos[0] > 1.5 and loop_moves[up][left][1] != 1 and loop_moves[up][right][1] != -1:
        neighbors.append((pos[0] - 1, pos[1]))            
    if pos[0] < len(loop_map) - 1.5 and loop_moves[down][left][1] != 1 and loop_moves[down][right][1] != -1:
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] > 1.5 and loop_moves[up][left][0] != 1 and loop_moves[down][left][0] != -1:
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] < len(loop_map[0]) - 1.5 and loop_moves[up][right][0] != 1 and loop_moves[down][right][0] != -1:
        neighbors.append((pos[0], pos[1] + 1))

    return neighbors

def get_integer_neighborhood(pos):
    up = int(pos[0] - 0.5)
    down = int(pos[0] + 0.5)
    left = int(pos[1] - 0.5)
    right = int(pos[1] + 0.5)
    return up, down, left, right


def bfs(loop_map, loop_moves, pipemap):
    left, right, top, bottom = get_boundaries(loop_map)

    outside_loop = [[False for _ in pipemap[0]] for _ in pipemap]

    candidates = set()
    for row_idx, row in enumerate(loop_map):
        for col_idx, col in enumerate(row):
            if loop_map[row_idx][col_idx]:
                outside_loop[row_idx][col_idx] = True
            if col_idx > left and col_idx < right and row_idx > top and row_idx < bottom:
                if not loop_map[row_idx][col_idx]:
                    candidates.add((row_idx, col_idx))
            else:
                outside_loop[row_idx][col_idx] = True
    
    while candidates:
        start = candidates.pop()
        visited = set()
        queue = deque()
        queue.append((start[0] + 0.5, start[1] + 0.5))
        queue.append((start[0] - 0.5, start[1] + 0.5))
        queue.append((start[0] + 0.5, start[1] - 0.5))
        queue.append((start[0] - 0.5, start[1] - 0.5))
        visited.add(start)
        broke_out = False
        while queue:
            pos = queue.popleft()
            up, down, left, right = get_integer_neighborhood(pos)
            candidates.discard((up, left))
            candidates.discard((up, right))
            candidates.discard((down, left))
            candidates.discard((down, right))
            if pos[0] <= top or pos[0] >= bottom or pos[1] <= left or pos[1] >= right:
                broke_out = True
                break
            neighbors = get_neighbors(pos, loop_map, loop_moves)
            for n in neighbors:
                if n not in visited:
                    visited.add(n)
                    queue.append(n)
        if broke_out:
            for pos in visited:
                up, down, left, right = get_integer_neighborhood(pos)
                outside_loop[up][left] = True
                outside_loop[up][right] = True
                outside_loop[down][left] = True
                outside_loop[down][right] = True
    
    return outside_loop

pipemap = []
start = None

for row_idx, line in enumerate(sys.stdin):
    line = list(line.strip())
    if 'S' in line:
        col_idx = line.index('S')
        start = (row_idx, col_idx)
        line[col_idx] = '.'
    pipemap.append([pipes[c] for c in line])

start_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for move in start_moves:
    loop_map, loop_moves = get_loop_map(start, pipemap, move)
    if loop_map is not None:
        break

outside_loop = bfs(loop_map, loop_moves, pipemap)

inside_sum = sum([sum([c  == False for c in row]) for row in outside_loop])
print(inside_sum)
