import sys
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

dirs = {
    '0': (0, 1),
    '1': (1, 0),
    '2': (0, -1),
    '3': (-1, 0)
}

xs = [0]
ys = [0]

circumf = 0
dir_list = []

for i, line in enumerate(sys.stdin):
    line = line.strip().split()
    hexcode = line[2][1: -1]
    n = int(hexcode[1: -1], 16)
    dir = hexcode[-1]
    ys.append(ys[-1] + n * dirs[dir][0])
    xs.append(xs[-1] + n * dirs[dir][1])
    circumf += n
    dir_list.append(dir)

miny = min(ys)
minx = min(xs)
ys = [y - miny for y in ys]
xs = [x - minx for x in xs]
height = max(ys) + 1
width = max(xs) + 1

corner_to_dir = dict()
for (y, x) in zip(ys, xs):
    corner_to_dir[(y, x)] = []
for i, (y, x) in enumerate(zip(ys[:-1], xs[:-1])):
    if dir_list[i] == '1': #down
        corner_to_dir[(y, x)].append('down')
        corner_to_dir[(ys[i+1], xs[i+1])].append('up')
    elif dir_list[i] == '3':
        corner_to_dir[(y, x)].append('up')
        corner_to_dir[(ys[i+1], xs[i+1])].append('down')  
    elif dir_list[i] == '0':
        corner_to_dir[(y, x)].append('right')
        corner_to_dir[(ys[i+1], xs[i+1])].append('left') 
    elif dir_list[i] == '2':
        corner_to_dir[(y, x)].append('left')
        corner_to_dir[(ys[i+1], xs[i+1])].append('right') 

corners = set([(y,x) for y, x in zip(ys, xs)])
rows_with_corners = set([pos[0] for pos in corners])

row_marks = [[] for _ in range(height)]

for i in range(len(ys) - 1):
    if ys[i] < ys[i + 1]:
        for y in range(ys[i], ys[i + 1] + 1):
            row_marks[y].append(xs[i])
    elif ys[i] > ys[i + 1]:
        for y in range(ys[i + 1], ys[i] + 1):
            row_marks[y].append(xs[i])

inner_sum = 0

start_idx = 0
row_marks = row_marks[0:]
height = len(row_marks)

prev_length = 0
prev_had_corner = True

for row_idx, row in enumerate(row_marks):
    lacks_corner = (row_idx + start_idx) not in rows_with_corners
    if row_idx > 0 and (not prev_had_corner) and lacks_corner:
        inner_sum += prev_length
        continue
    wall_count = 0
    line_sum = 0
    row_marks[row_idx] = sorted(row)
    for col_idx, col in enumerate(row_marks[row_idx][:-1]):
        pos = (row_idx+start_idx, col)
        if pos in corners:
            if 'down' in corner_to_dir[pos]:
                wall_count += 1
        else:
            wall_count += 1
        if wall_count & 1 == 1:
            if not (pos in corners and ('right' in corner_to_dir[pos])):
                line_sum += (row_marks[row_idx][col_idx + 1] - col - 1)
    inner_sum += line_sum
    prev_length = line_sum
    prev_had_corner = not lacks_corner

trench_count = inner_sum + circumf
print(trench_count)