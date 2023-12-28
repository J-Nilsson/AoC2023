import sys
import numpy as np

def lines_to_numpy(lines):
    pattern = np.full((len(lines), len(lines[0])), False)
    for row_idx, row in enumerate(lines):
        for col_idx, col in enumerate(row):
            if col == "#":
                pattern[row_idx, col_idx] = True
    
    return pattern

def find_reflection(pattern):
    # vertical lines
    for line in range(pattern.shape[1] - 1):
        reflect_width = min(line + 1, pattern.shape[1] - line - 1)
        left = pattern[:, line - reflect_width + 1: line + 1]
        right = pattern[:, line + 1: line + 1 + reflect_width]
        if np.all(left == np.fliplr(right)):
            return line + 1
    for line in range(pattern.shape[0] - 1):
        reflect_width = min(line + 1, pattern.shape[0] - line - 1)
        up = pattern[line - reflect_width + 1: line + 1, :]
        down = pattern[line + 1: line + 1 + reflect_width, :]
        if np.all(up == np.flipud(down)):
            return 100 * (line + 1)

total = 0
lines = []

for line in sys.stdin:
    line = line.strip()
    if line == '':
        pattern = lines_to_numpy(lines)
        total += find_reflection(pattern)
        lines = []
    else:
        lines.append(line)

pattern = lines_to_numpy(lines)
total += find_reflection(pattern)

print(total)