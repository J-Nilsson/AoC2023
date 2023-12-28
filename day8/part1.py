import sys

adj_list = dict()

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
current = 'AAA'

while True:
    current = adj_list[current][instr[idx % instr_len]]
    steps += 1
    idx +=1
    if current == 'ZZZ':
        break

print(steps)

