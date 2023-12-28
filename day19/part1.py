import sys

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
    
    def get_dest(self, part):
        for instr in self.instructions:
            if 'letter' not in instr.keys():
                return instr['dest']
            if instr['operator'] == '<':
                if part[instr['letter']] < instr['number']:
                    return instr['dest']
                continue
            if instr['operator'] == '>':
                if part[instr['letter']] > instr['number']:
                    return instr['dest']
                continue

def parse_part(part):
    part = part[1:-1]
    part = part.split(',')
    res = dict()
    for p in part:
        res[p[0]] = int(p[2:])
    
    return res

workflows = dict()
parts = []

for line in sys.stdin:
    line = line.strip()
    if line == '':
        break

    name = line.split('{')[0]
    workflows[name] = Workflow(line)

for line in sys.stdin:
    line = line.strip()
    parts.append(parse_part(line))

accept_sum = 0

for part in parts:
    workflow = workflows['in']

    while True:
        dest = workflow.get_dest(part)
        if dest == 'A':
            accept_sum += sum([r for r in part.values()])
            break
        if dest == 'R':
            break
        workflow = workflows[dest]

print(accept_sum)

