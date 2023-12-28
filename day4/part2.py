import sys

num_cards = 0

wins_per_card = []

for line in sys.stdin:
    line = line.strip().split('|')
    winning = list(map(int, line[0].split(':')[1].split()))
    numbers = list(map(int, line[1].split()))

    num_winning = len([n for n in numbers if n in winning])
    wins_per_card.append(num_winning)

num_copies = [1 for _ in wins_per_card]

for idx, n in enumerate(wins_per_card):
    for i in range(idx + 1, idx + 1 + n):
        num_copies[i] += num_copies[idx]

print(sum(num_copies))