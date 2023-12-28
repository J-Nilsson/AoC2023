import sys
import numpy as np

def count_weight(column):
    height = len(column)
    temp_solids = np.where(column == 2)[0]
    solids = np.zeros(temp_solids.size + 2, dtype=int)
    solids[0] = -1
    solids[1:-1] = temp_solids
    solids[-1] = height

    weight_sum = 0

    for s_idx, s in enumerate(solids[:-1]):
        n_roll = np.sum(column[s + 1: solids[s_idx + 1]])
        weight_sum += n_roll * (height - s) - n_roll * (n_roll + 1) // 2
    
    return weight_sum

def platform_weight(platform):
    weight_sum = 0

    for col in platform.T:
        weight_sum += count_weight(col)
    
    return weight_sum

def lines_to_platform(lines):
    height = len(lines)
    width = len(lines[0])

    translation = {'.': 0, 'O': 1, '#': 2}

    platform = np.zeros((height, width), dtype=int)

    for row_idx, row in enumerate(lines):
        for col_idx, col in enumerate(row):
            platform[row_idx, col_idx] = translation[lines[row_idx][col_idx]]
    
    return platform

lines = []

for line in sys.stdin:
    lines.append(line.strip())

print(platform_weight(lines_to_platform(lines)))
