import sys

sum = 0

for line in sys.stdin:
    line = line.strip()

    first = ''
    last = ''
    for char in line:
        if char in ('0123456789'):
            if first == '':
                first = char
            last = char
    sum += int(first + last)

print(sum)