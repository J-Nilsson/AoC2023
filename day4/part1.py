import sys

sum = 0

winning = []
numbers = []

for line in sys.stdin:
    line = line.strip().split('|')
    winning = list(map(int, line[0].split(':')[1].split()))
    numbers = list(map(int, line[1].split()))

    num_winning = len([n for n in numbers if n in winning])
    if num_winning > 0:
        sum += 2 ** (num_winning - 1)

print(sum)
