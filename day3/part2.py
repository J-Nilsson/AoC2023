import sys

sum = 0
digits = '0123456789'
dot = '.'
gear = '*'
lines = []
gear_dict = dict()

def insert_in_geardict(row_idx, col_idx, number, lines, gear_dict):
    rows = [row_idx]
    if row_idx > 0:
        rows.append(row_idx - 1)
    if row_idx < len(lines) - 1:
        rows.append(row_idx + 1)
    cols = [*col_idx]
    if col_idx[0] > 0:
        cols.append(col_idx[0] - 1)
    if col_idx[-1] < len(lines[0]) - 1:
        cols.append(col_idx[-1] + 1)

    for i in rows:
        for j in cols:
            if lines[i][j] == gear:
                if (i, j) not in gear_dict.keys():
                    gear_dict[(i,j)] = []
                gear_dict[(i,j)].append(number)
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
                if c_idx == len(row) - 1:
                    number = int(row[num_begin: num_end + 1])
                    num_cols = list(range(num_begin, num_end + 1))
                    insert_in_geardict(r_idx, num_cols, number, lines, gear_dict)
            else:
                on_number = False
                number = int(row[num_begin: num_end + 1])
                num_cols = list(range(num_begin, num_end + 1))
                insert_in_geardict(r_idx, num_cols, number, lines, gear_dict)
        else:
            if char in digits:
                on_number = True
                num_begin = c_idx
                num_end = c_idx

sum = 0
for numbers in gear_dict.values():
    if len(numbers) == 2:
        sum += numbers[0] * numbers[1]
    

print(sum)