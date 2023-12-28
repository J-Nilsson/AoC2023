import sys

card_rank = {
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 0,
    "Q": 12,
    "K": 13,
    "A": 14,
}

def hand_type(hand):
    num_j = hand.count('J')
    if num_j == 5:
        return 7
    
    hand = hand.replace('J', '')
    char_counts = [hand.count(c) for c in set(hand)]
    char_counts.sort(reverse=True)
    if char_counts[0] + num_j == 5:
        return 7
    if char_counts[0] + num_j == 4:
        return 6
    if char_counts[0] + num_j == 3 and char_counts[1] == 2:
        return 5
    if char_counts[0] + num_j == 3 and char_counts[1] == 1:
        return 4
    if char_counts[0] + num_j == 2 and char_counts[1] == 2:
        return 3
    if char_counts[0] + num_j == 2 and char_counts[1] == 1:
        return 2
    return 1

def hand_score(hand):
    return hand_type(hand) + sum([card_rank[h] * 15 ** ( -2 -i) for i, h in enumerate(hand)])

hand_bids = []

for line in sys.stdin:
    hand_bid = list(line.strip().split())
    hand_bid[1] = int(hand_bid[1])
    hand_bids.append(hand_bid)

hand_bids = sorted(hand_bids, key=lambda x: hand_score(x[0]))

total_win = sum([(i + 1) * h[1] for i, h in enumerate(hand_bids)])
print(total_win)