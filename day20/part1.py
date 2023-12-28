import sys

class module:
    def __init__(self, name, mod_type, outputs):
        self.mod_type = mod_type
        self.name = name
        self.inputs = dict()
        self.state = 0
        self.outputs = outputs
    
    def send(self, signal):
        if self.mod_type == '%':
            if signal == 1:
                return None
            else:
                return [(self.name, nam, (self.state) & 1) for nam in self.outputs]
        else:
            if all([inp == 1 for inp in self.inputs.values()]):
                return [(self.name, name, 0) for name in self.outputs]
            else:
                return [(self.name, name, 1) for name in self.outputs]
    
    def update(self, input_name, signal):
        if self.mod_type == '%':
            if signal == 0:
                self.state = (self.state + 1) & 1
        else:
            self.inputs[input_name] = signal

modules = {}

for line in sys.stdin:
    line = line.strip()
    line = line.replace(" ", "")
    line = line.split("->")
    name = line[0][1:]
    mod_type = line[0][0]
    outputs = line[1].split(',')

    if name not in modules:
        modules[name] = module(name, mod_type, outputs)
    else:
        modules[name].mod_type = mod_type
        modules[name].outputs = outputs
    
    for out in outputs:
        if out not in modules:
            modules[out] = module(out, '-', [])
        modules[out].inputs[name] = 0


num_high = 0
num_low = 0

num_times = 1000

for _ in range(num_times):
    num_low += 1 + len(modules['roadcaster'].outputs)
    received = [('broadcaster', name, 0) for name in modules['roadcaster'].outputs]
    while received:
        for rec in received:
            modules[rec[1]].update(rec[0], rec[2])
        new_rec = []
        for rec in received:
            if rec[1] == 'output':
                continue
            messages = modules[rec[1]].send(rec[2])
            if messages is not None:
                for sent in messages:
                    new_rec.append(sent)
                    if sent[2] == 0:
                        num_low += 1
                    else:
                        num_high += 1
        received = new_rec

print(num_low * num_high)

