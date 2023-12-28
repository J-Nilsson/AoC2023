import sys
import numpy as np
import matplotlib.pyplot as plt

def tilt_north(platform, solids_x, solids_y):
    height = platform.shape[0]

    for col_idx in range(platform.shape[1]):
        solids = solids_y[np.where(solids_x == col_idx)[0]]
        if len(solids) == 0:
            n_roll = np.sum(platform[:, col_idx])
            platform[:n_roll, col_idx] = 1
            platform[n_roll:, col_idx] = 0
            continue

        n_roll = np.sum(platform[:solids[0], col_idx])
        platform[:n_roll, col_idx] = 1
        platform[n_roll: solids[0], col_idx] = 0

        for s_idx, s in enumerate(solids[:-1]):
            n_roll = np.sum(platform[s + 1: solids[s_idx + 1], col_idx])
            platform[s + 1: s + 1 + n_roll, col_idx] = 1
            platform[s + 1 + n_roll: solids[s_idx + 1], col_idx] = 0
        last_s = solids[-1]
        n_roll = np.sum(platform[last_s + 1: height, col_idx])
        platform[last_s + 1: last_s + 1 + n_roll, col_idx] = 1
        platform[last_s + 1 + n_roll:, col_idx] = 0
    
    return platform

def tilt_south(platform, solids_x, solids_y):
    height = platform.shape[0]

    for col_idx in range(platform.shape[1]):
        solids = solids_y[np.where(solids_x == col_idx)[0]]
        if len(solids) == 0:
            n_roll = np.sum(platform[:, col_idx])
            platform[height - n_roll:, col_idx] = 1
            platform[:height - n_roll, col_idx] = 0
            continue

        n_roll = np.sum(platform[:solids[0], col_idx])
        platform[solids[0] - n_roll:solids[0], col_idx] = 1
        platform[:solids[0] - n_roll, col_idx] = 0

        for s_idx, s in enumerate(solids[:-1]):
            n_roll = np.sum(platform[s + 1: solids[s_idx + 1], col_idx])
            platform[s + 1: solids[s_idx + 1] - n_roll, col_idx] = 0
            platform[solids[s_idx + 1] - n_roll: solids[s_idx + 1], col_idx] = 1
        last_s = solids[-1]
        n_roll = np.sum(platform[last_s + 1: height, col_idx])
        platform[last_s + 1: height -  n_roll, col_idx] = 0
        platform[height - n_roll:, col_idx] = 1
    
    return platform

def tilt_west(platform, solids_x, solids_y):
    return tilt_north(platform.T, solids_y, solids_x).T

def tilt_east(platform, solids_x, solids_y):
    return tilt_south(platform.T, solids_y, solids_x).T

def cycle(platform, solids_x, solids_y):
    platform = tilt_north(platform, solids_x, solids_y)
    platform = tilt_west(platform, solids_x, solids_y)
    platform = tilt_south(platform, solids_x, solids_y)
    platform = tilt_east(platform, solids_x, solids_y)
    return platform

def platform_weight(platform):
    height = platform.shape[0]
    weight_nums = np.zeros_like(platform)
    for row_idx in range(weight_nums.shape[0]):
        weight_nums[row_idx, :] = height - row_idx
    
    weight = np.sum(weight_nums * (platform == 1))
    return weight

def lines_to_platform(lines):
    height = len(lines)
    width = len(lines[0])

    translation = {'.': 0, 'O': 1, '#': 2}

    platform = np.zeros((height, width), dtype=int)

    for row_idx, row in enumerate(lines):
        for col_idx, col in enumerate(row):
            platform[row_idx, col_idx] = translation[lines[row_idx][col_idx]]
    
    return platform

lines = []

for line in sys.stdin:
    lines.append(line.strip())

platform = lines_to_platform(lines)
solids = np.where(platform == 2)
solids_y = solids[0]
solids_x = solids[1]


for i in range(200):
    cycle(platform, solids_x, solids_y)

orig_platform = np.copy(platform)

idx = 0
while True:
    cycle(platform, solids_x, solids_y)
    if np.all(platform == orig_platform):
        break
    idx += 1

period = idx + 1

k = (1000000000 - 200) // period
near = 200 + k * period
for i in range(1000000000 - near):
    cycle(platform, solids_x, solids_y)

print(platform_weight(platform))