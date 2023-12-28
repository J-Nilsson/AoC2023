import sys
import itertools

empty_rows = []
empty_cols_b = []
galaxies = []

num_rows = 0

for row_idx, line in enumerate(sys.stdin):
    line = line.strip()
    if row_idx == 0:
        empty_cols_b = [True for _ in line]
    galaxy_cols = [pos for pos, c in enumerate(line) if c == "#"]
    if len(galaxy_cols) == 0:
        empty_rows.append(row_idx)
    else:
        for col_idx in galaxy_cols:
            empty_cols_b[col_idx] = False
            galaxies.append((row_idx, col_idx))
    num_rows += 1

empty_rows_b = [False for _ in range(num_rows)]
for row in empty_rows:
    empty_rows_b[row] = True

dist_sum = 0

for g1, g2 in itertools.combinations_with_replacement(galaxies, 2):
    if g1 == g2:
        continue
    lower_row = min(g1[0], g2[0])
    upper_row = max(g1[0], g2[0])
    lower_col = min(g1[1], g2[1])
    upper_col = max(g1[1], g2[1])
    rows_added = sum(empty_rows_b[lower_row:upper_row])
    cols_added = sum(empty_cols_b[lower_col:upper_col])

    dist = upper_row - lower_row + upper_col - lower_col + rows_added + cols_added
    dist_sum += dist

print(dist_sum)