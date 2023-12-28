import sys

def intersect(p1, v1, p2, v2):
    x1, y1 = p1[:2]
    x2, y2 = p2[:2]
    vx1, vy1 = v1[:2]
    vx2, vy2 = v2[:2]

    if vx1 / vx2 == vy1 / vy2:
        if x1 == x2 and y1 == y2:
            return x1, y1, 1, 1
        else:
            return None, None, None, None

    A = vy1 - vy2 * vx1 / vx2
    B = y2 - y1 + vy2 * (x1-x2) / vx2
    t = B / A

    px = x1 + vx1 * t
    py = y1 + vy1 * t
    s = (x1 - x2) / vx2 + vx1 / vx2 * t

    return px, py, t, s

stones = []

for line in sys.stdin:
    line = line.strip()
    line = line.replace(' ', '').split('@')
    pos = list(map(float, line[0].split(',')))
    velocity = list(map(float, line[1].split(',')))
    stones.append((pos, velocity))

lower = 200000000000000
upper = 400000000000000

cross_sum = 0

for idx, stone1 in enumerate(stones[:-1]):
    for id2, stone2 in enumerate(stones[idx + 1:]):
        px, py, t, s = intersect(stone1[0], stone1[1], stone2[0], stone2[1])
        if px is None:
            continue
        if lower <= px <= upper and lower <= py <= upper and t > 0 and s > 0:
            cross_sum += 1

print(cross_sum)
