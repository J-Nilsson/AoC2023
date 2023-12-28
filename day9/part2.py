import sys
import numpy as np

def next_value(seq):
    last_numbers = [seq[0]]

    while True:
        seq = np.diff(seq)
        if np.all(seq == 0):
            break
        else:
            last_numbers.append(seq[0])
    
    new_number = 0
    for n in last_numbers[::-1]:
        new_number = -new_number + n
    
    return new_number

total = 0

for line in sys.stdin:
    line = np.array(list(map(int, line.strip().split())))
    total += next_value(line)

print(total)