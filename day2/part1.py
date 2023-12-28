import sys

sum = 0

for idx, line in enumerate(sys.stdin):
    line = line.strip()
    cubes = line.split(':')[1]
    subsets = cubes.split(';')

    possible = True
    for s in subsets:
        if not possible:
            break
        revealed = s.split(',')
        for r in revealed:
            r = r.strip().split()
            if r[1] == 'red' and int(r[0]) > 12:
                possible = False
                break
            elif r[1] == 'green' and int(r[0]) > 13:
                possible = False
                break
            elif r[1] == 'blue' and int(r[0]) > 14:
                possible = False
                break

    if possible:
        sum += idx + 1

print(sum)