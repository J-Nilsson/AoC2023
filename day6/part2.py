import sys
import math

time = int(sys.stdin.readline().split(':')[1].replace(" ", ""))
dist = int(sys.stdin.readline().split(':')[1].replace(" ", ""))

lower = time / 2 - (time ** 2 / 4 - dist) ** 0.5
if abs(lower - round(lower)) < 1e-5:
    lower = round(lower) + 1
else: 
    lower = math.ceil(lower)
upper = time / 2 + (time ** 2 / 4 - dist) ** 0.5
if abs(upper - round(upper)) < 1e-5:
    upper  = round(upper) - 1
else:
    upper = math.floor(upper)

print(upper - lower + 1)