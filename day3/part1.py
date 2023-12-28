import sys

sum = 0
digits = '0123456789'
dot = '.'
lines = []

def char_is_part(char):
    return char not in digits and char != dot

def has_part_neighbor(row_idx, col_idx, lines):
    rows = [row_idx]
    if row_idx > 0:
        rows.append(row_idx - 1)
    if row_idx < len(lines) - 1:
        rows.append(row_idx + 1)
    cols = [col_idx]
    if col_idx > 0:
        cols.append(col_idx - 1)
    if col_idx < len(lines[0]) - 1:
        cols.append(col_idx + 1)
    
    for i in rows:
        for j in cols:
            if char_is_part(lines[i][j]):
                return True     
    return False

for line in sys.stdin:
    line = line.strip()
    lines.append(line)

for r_idx, row in enumerate(lines):
    num_begin = 0
    num_end = 0
    on_number = False
    is_part = False
    for c_idx, char in enumerate(row):
        if on_number:
            if char in digits:
                num_end = c_idx
                is_part = True if is_part else has_part_neighbor(r_idx, c_idx, lines)
                if c_idx == len(row) - 1 and is_part:
                    sum += int(row[num_begin: num_end + 1])
            else:
                on_number = False
                if is_part:
                    sum += int(row[num_begin: num_end + 1])
                is_part = False
        else:
            if char in digits:
                on_number = True
                num_begin = c_idx
                num_end = c_idx
                is_part = has_part_neighbor(r_idx, c_idx, lines)

print(sum)