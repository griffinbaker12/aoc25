import re

SPACE_HEIGHT = 103
SPACE_WIDTH = 101

# SPACE_HEIGHT = 7
# SPACE_WIDTH = 11
TIME_S = 100

# NOTE: I think there is a way where I can just calcualte the position based on total time
# NOTE: but I will first try this looping approach


def update_positions(stats):
    for i, (px, py, vx, vy) in enumerate(stats):
        new_x, new_y = (px + vx) % SPACE_WIDTH, (py + vy) % SPACE_HEIGHT
        stats[i][0] = new_x
        stats[i][1] = new_y


with open("input.txt") as f:
    stats = [list(map(int, re.findall(r"-?\d+", line))) for line in f.readlines()]
    t = 0
    while t < TIME_S:
        update_positions(stats)
        t += 1

    quads = {n: 0 for n in range(1, 5)}
    mid_x, mid_y = SPACE_WIDTH // 2, SPACE_HEIGHT // 2
    for x, y, *_ in stats:
        if x == mid_x or y == mid_y:
            continue
        if x < mid_x:
            if y < mid_y:
                quads[1] += 1
            else:
                quads[2] += 1
        else:
            if y < mid_y:
                quads[3] += 1
            else:
                quads[4] += 1
    total = 1
    for v in quads.values():
        total *= v
    print(total)
