import sys

def map_source_to_dest(source, mapping):
    for line in mapping:
        if source >= line[1] and source <= line[1] + line[2]:
            return line[0] + source - line[1]
    
    return source

lowest_loc = 1e20

seed_line = sys.stdin.readline().strip()
seeds = list(map(int, seed_line.split(':')[1].split()))
sys.stdin.readline()

mappings = []
digits = '0123456789'
current_map = []

for line in sys.stdin:
    line = line.strip()
    if line == '':
        mappings.append(current_map)
        current_map = []
    elif line[0] in digits:
        current_map.append(list(map(int, line.split())))

mappings.append(current_map)

for seed in seeds:
    current = seed
    for mapping in mappings:
        current = map_source_to_dest(current, mapping)
    lowest_loc = min(lowest_loc, current)

print(lowest_loc)