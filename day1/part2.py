import sys

sum = 0

digits = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine')
buffer = ''

for line in sys.stdin:
    line = line.strip()

    first = None
    last = None
    for idx, char in enumerate(line):
        if char in ('0123456789'):
            if first is None:
                first = int(char)
            last = int(char)
        else:
            for i, d in enumerate(digits):
                if line[idx:idx + len(d)] == d:
                    if first is None:
                        first =  i + 1
                    last = i + 1
    print(first, last)
    sum += first * 10 + last

print(sum)