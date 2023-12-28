import sys

def hash_of_string(s):
    val = 0
    for char in s:
        val = ((val + ord(char)) * 17) % 256
    
    return val

def follow_instruction(boxes, instr):
    if instr[-1] == '-':
        label = instr[:-1]
        box_idx = hash_of_string(label)
        boxes[box_idx] = [lens for lens in boxes[box_idx] if lens[0] != label]
    elif instr[-2] == '=':
        label = instr[:-2]
        box_idx = hash_of_string(label)        
        foc_len = int(instr[-1])
        for lens in boxes[box_idx]:
            if lens[0] == label:
                lens[1] = foc_len
                break
        else:
            boxes[box_idx].append([label, foc_len])

boxes = [[] for _ in range(256)]
strings = sys.stdin.readline().split(',')

for s in strings:
    follow_instruction(boxes, s)

print(sum([sum([(i + 1) * (j + 1) * l[1] for j, l in enumerate(b)]) for i , b in enumerate(boxes)]))

