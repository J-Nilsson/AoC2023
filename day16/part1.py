import sys

contraption = []

for line in sys.stdin:
    line = line.strip()
    contraption.append(line)


beams = [[0, 0]]
dirs = [[0, 1]]
visited = set()

height = len(contraption)
width = len(contraption[0])

energized = [[0 for j in range(width)] for i in range(height)]

while beams:
    beams_to_add = []
    dirs_to_add = []
    to_remove = set()
    for idx, (beam, dir) in enumerate(zip(beams, dirs)):
        if (tuple(beam), tuple(dir)) in visited:
            to_remove.add(idx)
        else:
            visited.add((tuple(beam), tuple(dir)))
            marker = contraption[beam[0]][beam[1]]
            if 0 <= beam[0] < height and 0 <= beam[1] < width:
                energized[beam[0]][beam[1]] = 1
            if marker == '.':
                beam[0] += dir[0]
                beam[1] += dir[1]
            elif marker == '|':
                if dir[1] == 0:
                    beam[0] += dir[0]
                    beam[1] += dir[1]
                else:
                    to_remove.add(idx)
                    if beam[0] - 1 >= 0:
                        beams_to_add.append([beam[0] - 1, beam[1]])
                        dirs_to_add.append([-1, 0])
                    if beam[0] + 1 < height:
                        beams_to_add.append([beam[0] + 1, beam[1]])
                        dirs_to_add.append([1, 0])
            elif marker == '-':
                if dir[0] == 0:
                    beam[0] += dir[0]
                    beam[1] += dir[1]
                else:
                    to_remove.add(idx)
                    if beam[1] - 1 >= 0:
                        beams_to_add.append([beam[0], beam[1] - 1])
                        dirs_to_add.append([0, -1])
                    if beam[1] + 1 < width:
                        beams_to_add.append([beam[0], beam[1] + 1])
                        dirs_to_add.append([0, 1])
            elif marker == '/':
                if dir == [1, 0]:
                    beam[1] -= 1
                    dir[0] = 0
                    dir[1] = -1
                elif dir == [-1, 0]:
                    beam[1] += 1
                    dir[0] = 0
                    dir[1] = 1
                elif dir == [0, 1]:
                    beam[0] -= 1
                    dir[0] = -1
                    dir[1] = 0
                elif dir == [0, -1]:
                    beam[0] += 1
                    dir[0] = 1
                    dir[1] = 0
            elif marker == '\\':
                if dir == [1, 0]:
                    beam[1] += 1
                    dir[0] = 0
                    dir[1] = 1
                elif dir == [-1, 0]:
                    beam[1] -= 1
                    dir[0] = 0
                    dir[1] = -1
                elif dir == [0, 1]:
                    beam[0] += 1
                    dir[0] = 1
                    dir[1] = 0
                elif dir == [0, -1]:
                    beam[0] -= 1
                    dir[0] = -1
                    dir[1] = 0            

        if beam[0] < 0 or beam[0] == height or beam[1] < 0 or beam[1] == width:
            to_remove.add(idx)
    
    beams = [b for i, b in enumerate(beams) if i not in to_remove]
    dirs = [d for i, d in enumerate(dirs) if i not in to_remove]

    for b, d in zip(beams_to_add, dirs_to_add):
        beams.append(b)
        dirs.append(d)

print(sum(sum(row) for row in energized))
    