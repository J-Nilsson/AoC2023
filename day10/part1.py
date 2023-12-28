import sys

pipes = {
     '|': [(1, 0), (-1, 0)],
     '-': [(0, 1), (0, -1)],
     'L': [(-1, 0), (0, 1)],
     'J': [(-1, 0), (0, -1)],
     '7': [(1, 0), (0, -1)],
     'F': [(1, 0), (0, 1)],
     '.': [],
}

def loop_length(start, pipemap, start_move):
    cur_pos = start
    cur_move = start_move
    length = 0
    while True:
        length += 1
        cur_pos = (cur_pos[0] + cur_move[0], cur_pos[1] + cur_move[1])
        if cur_pos == start:
            return length
        
        cur_options = pipemap[cur_pos[0]][cur_pos[1]]
        if len(cur_options) == 0:
            return None
        if cur_move[0] == -cur_options[0][0] and cur_move[1] ==-cur_options[0][1]:
            cur_move = cur_options[1]
        elif cur_move[0] == -cur_options[1][0] and cur_move[1] ==-cur_options[1][1]:
            cur_move = cur_options[0]
        else:
            return None

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
    length = loop_length(start, pipemap, move)
    if length is not None:
        print(move)
        print(length // 2)
        break




