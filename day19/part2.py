import sys
from copy import copy

class Workflow:
    def __init__(self, str):
        wf = str.split('{')
        self.name = wf[0]

        instructions = wf[1][:-1].split(',')

        self.instructions = []
        for instr in instructions:
            a = dict()
            if ':' not in instr:
                a['dest'] = instr
                self.instructions.append(a)
                continue
            instr = instr.split(':')
            cond = instr[0]
            dest = instr[1]
            a['letter'] = cond[0]
            a['operator'] = cond[1]
            a['number'] = int(cond[2:])
            a['dest'] = dest
            self.instructions.append(a)

workflows = dict()
parts = []

for line in sys.stdin:
    line = line.strip()
    if line == '':
        break

    name = line.split('{')[0]
    workflows[name] = Workflow(line)

global accept_sum
accept_sum = 0

def product(intervals):
    prod = 1
    for interval in intervals.values():
        prod *= (interval[1] - interval[0] + 1)
    return prod

def search(intervals, workflow):
    global accept_sum
    interv_to_cont = intervals
    for instr in workflow.instructions:
        if 'operator' not in instr:
            if instr['dest'] == 'A':
                accept_sum += product(interv_to_cont)
            elif instr['dest'] != 'R':
                search(interv_to_cont, workflows[instr['dest']])
            break
        letter = instr['letter']
        number = instr['number']
        cur_low, cur_upp = interv_to_cont[letter]

        if instr['operator'] == '<':
            new_intervs = copy(interv_to_cont)
            new_intervs[letter] = [cur_low, min(number - 1, cur_upp)]
            if cur_low <= min(number - 1, cur_upp):
                if instr['dest'] == 'A':
                    accept_sum += product(new_intervs)
                elif instr['dest'] != 'R':
                    search(new_intervs, workflows[instr['dest']])

            interv_to_cont[letter] = [max(cur_low, number), cur_upp]
            if max(cur_low, number) > cur_upp:
                break
        else: # >
            new_intervs = copy(interv_to_cont)
            new_intervs[letter] = [max(cur_low, number + 1), cur_upp]
            if cur_upp >= max(cur_low, number + 1):
                if instr['dest'] == 'A':
                    accept_sum += product(new_intervs)
                elif instr['dest'] != 'R':
                    search(new_intervs, workflows[instr['dest']])
            interv_to_cont[letter] = [cur_low, min(cur_upp, number)]
            if cur_low > min(cur_upp, number):
                break

intervals = {'x': [1, 4000], 'm': [1, 4000], 'a': [1, 4000], 's': [1, 4000]}

search(intervals, workflows['in'])

print(accept_sum)

