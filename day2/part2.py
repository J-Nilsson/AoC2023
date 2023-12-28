import sys


power_sum = 0

for idx, line in enumerate(sys.stdin):
    line = line.strip()
    cubes = line.split(':')[1]
    subsets = cubes.split(';')

    most_seen = [0, 0, 0]
    for s in subsets:
        revealed = s.split(',')
        for r in revealed:
            r = r.strip().split()
            if r[1] == 'red':
                most_seen[0] = max(most_seen[0], int(r[0]))
            elif r[1] == 'green':
                most_seen[1] = max(most_seen[1], int(r[0]))
            elif r[1] == 'blue':
                most_seen[2] = max(most_seen[2], int(r[0]))
        
    power_sum += most_seen[0] * most_seen[1] * most_seen[2]

print(power_sum)