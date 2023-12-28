import sympy
import sys

stones = []

for line in sys.stdin:
    line = line.strip()
    line = line.replace(' ', '').split('@')
    pos = list(map(float, line[0].split(',')))
    velocity = list(map(float, line[1].split(',')))
    stones.append((pos, velocity))

x, y, z, vx, vy, vz, t1, t2, t3 = sympy.symbols("x y z vx vy vz t1 t2 t3", real=True)
ts = [t1, t2, t3]

eqs = []
for idx, stone in enumerate(stones[:3]):
    x1, y1, z1 = stone[0]
    vx1, vy1, vz1 = stone[1]
    eqs.append(sympy.Eq(x + vx * ts[idx], x1 + vx1 * ts[idx]))
    eqs.append(sympy.Eq(y + vy * ts[idx], y1 + vy1 * ts[idx]))
    eqs.append(sympy.Eq(z + vz * ts[idx], z1 + vz1 * ts[idx]))

sol = sympy.solve(eqs)[0]
pos_sum = sol[x] + sol[y] + sol[z]

print(int(pos_sum))