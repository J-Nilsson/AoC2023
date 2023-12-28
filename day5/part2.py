import sys

def map_interval(source, mapping):
    new_ranges = []
    if source[0] < mapping[0][0][0]:
        right_bound = min(source[1], mapping[0][0][0] - 1)
        new_ranges.append([source[0], right_bound])
    if source[1] > mapping[-1][0][1]:
        left_bound = max(source[0], mapping[-1][0][1] + 1)
        new_ranges.append([left_bound, source[1]])

    for idx, (from_int, to_int) in enumerate(mapping):
        if from_int[1] >= source[0] and from_int[0] <= source[1]:
            from_lower = max(source[0], from_int[0])
            from_upper = min(source[1], from_int[1])
            to_lower = to_int[0] + (from_lower - from_int[0])
            to_upper = to_int[1] + (from_upper - from_int[1])
            new_ranges.append([to_lower, to_upper])

        if idx < len(mapping) - 1 and from_int[1] < source[1]:
            next_map = mapping[idx + 1]
            next_from_lower = next_map[0][0]
            if next_from_lower > from_int[1] + 1:
                new_ranges.append([from_int[1] + 1, next_from_lower - 1])

    return new_ranges

seed_line = sys.stdin.readline().strip()
seed_line = list(map(int, seed_line.split(':')[1].split()))
seed_starts = seed_line[0::2]
seed_lengths = seed_line[1::2]

seed_ranges = []
for s, l in zip(seed_starts, seed_lengths):
    seed_ranges.append([s, s + l - 1])
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
        dest, source, length = list(map(int, line.split()))
        from_int = [source, source + length - 1]
        to_int = [dest, dest + length - 1]
        current_map.append([from_int, to_int])

mappings.append(current_map)

for m in mappings:
    m.sort(key=lambda x:x[0][0])

lowest_loc = 1e20

for r in seed_ranges:
    ranges = [r]
    for m in mappings:
        new_ranges = []
        for ra in ranges:
            new_ranges.extend(map_interval(ra, m))
        ranges = new_ranges
    
    for r in ranges:
        lowest_loc = min(lowest_loc, r[0])

print(lowest_loc)