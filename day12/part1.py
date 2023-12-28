import sys

def solve(line, counts, table, on_segment, char_idx, count_idx, num_current):
    if char_idx == len(line) - 1:
        if count_idx < len(counts) - 1:
            return 0
        if line[char_idx] == '#' and (count_idx != len(counts)- 1 or counts[count_idx] - num_current == 0):
            return 0
        if line[char_idx] == '.' and (count_idx == len(counts) - 1 and counts[count_idx] - num_current > 0):
            return 0
        if line[char_idx] == '.' and count_idx < len(counts) - 1:
            return 0
        if line[char_idx] == '#' and (count_idx != len(counts)- 1 or counts[count_idx] - num_current > 1):
            return 0
        if line[char_idx] == '?' and num_current > 0 and (count_idx != len(counts)- 1 or counts[count_idx] - num_current > 1):
            return 0
        if line[char_idx] == '?' and num_current == 0 and count_idx < len(counts) - 1:
            return 0
        if line[char_idx] == '?' and count_idx <= len(counts) - 1 and num_current < counts[count_idx] - 1:
            return 0
        if count_idx < len(counts) and num_current > counts[count_idx]:
            return 0       
        return 1
    
    if (char_idx, count_idx, num_current) not in table.keys():
        if line[char_idx] == '.':
            temp_count_idx = count_idx
            if on_segment:
                temp_count_idx += 1
            if on_segment and num_current < counts[count_idx]:
                table[(char_idx, count_idx, num_current)] = 0
            else:
                table[(char_idx, count_idx, num_current)] = solve(line, counts, table, 0, char_idx + 1, temp_count_idx, 0)
        elif line[char_idx] == '#':
            if not on_segment:
                on_segment = True
            if count_idx > len(counts) - 1:
                table[(char_idx, count_idx, num_current)] = 0
            elif num_current + 1 > counts[count_idx]:
                table[(char_idx, count_idx, num_current)] = 0
            else:
                table[(char_idx, count_idx, num_current)] = solve(line, counts, table, True, char_idx + 1, count_idx, num_current + 1)
        else: # char is ?
            temp_count_idx = count_idx
            if on_segment:
                temp_count_idx += 1
            if on_segment and counts[count_idx] - num_current != 0:
                a = 0
            else:
                a = solve(line, counts, table, False, char_idx + 1, temp_count_idx, 0)
            if count_idx > len(counts) - 1 or num_current + 1 > counts[count_idx]:
                b = 0
            else:
                temp_count_idx = count_idx
                b = solve(line, counts, table, True, char_idx + 1, temp_count_idx, num_current + 1)
            
            table[(char_idx, count_idx, num_current)] = a + b
    
    return table[(char_idx, count_idx, num_current)]

total = 0

for i, line in enumerate(sys.stdin):
    line = line.strip().split()
    counts = list(map(int, line[1].split(',')))
    line = line[0]
    table = dict()
    total += solve(line, counts, table, False, 0, 0, 0)

print(total)
