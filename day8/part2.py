import sys
import math
import numpy as np
import itertools

adj_list = dict()

def get_cycle(start, adj_list, instr):
    visited = set()
    z_times = []
    visit_order = []

    instr_len = len(instr)
    instr_idx = 0
    steps = 0
    current = start
    visited.add((start, instr[0]))
    while True:
        current = adj_list[current][instr[instr_idx]]
        steps += 1
        instr_idx = (instr_idx + 1) % instr_len

        node = (current, instr_idx)

        if current[-1] == 'Z':
            visit_order.append(node)
            z_times.append(steps)
            if node in visited:
                cycle_idx = visit_order.index(node)
                break
            else:
                visited.add(node)
    
    return visit_order, cycle_idx, z_times


instr = sys.stdin.readline().strip()
instr = instr.replace('L', '0')
instr = instr.replace('R', '1')
instr = list(map(int, list(instr)))
instr_len = len(instr)
sys.stdin.readline()

for line in sys.stdin:
    line = line.strip().split('=')
    key = line[0].strip()
    adj = line[1].strip()[1:-1].replace(',', '').split()
    adj_list[key] = adj

steps = 0
idx = 0
current = [c for c in adj_list.keys() if c[-1] == 'A']
ends = [c for c in adj_list.keys() if c[-1] == 'Z']

z_timess = []

for s in current:
    vo, ci, zt = get_cycle(s, adj_list, instr)
    z_timess.append(zt)

return_times = [zt[1] - zt[0] for zt in z_timess]

print(np.lcm.reduce(return_times, dtype=np.int64))