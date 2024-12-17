import re

# SPACE_HEIGHT = 103
# SPACE_WIDTH = 101

WIDTH = 11
HEIGHT = 7

# NOTE: I think there is a way where I can just calcualte the position based on total time
# NOTE: but I will first try this looping approach


with open("test.txt") as f:
    # TODO: the '-' means either 0 or 1 minus leading (means it is optional I guess)
    robots = [tuple(map(int, re.findall(r"-?\d+", line))) for line in f.readlines()]
    results = [
        ((px + vx * 100) % WIDTH, (py + vy * 100) % HEIGHT) for px, py, vx, vy in robots
    ]

    # TODO: another good problem is to print out the grid as quickly as you can

    # NOTE: cool use of the array here because you don't need a hash map for just 4 values with this
    # NOTE: access pattern
    quad = [0] * 4
    for px, py in results:
        if px == WIDTH // 2 or py == HEIGHT // 2:
            continue
        if px < HEIGHT:
            if py < WIDTH:
                quad[0] += 1
            else:
                quad[1] += 1
        else:
            if py < WIDTH:
                quad[2] += 1
            else:
                quad[3] += 1
    print(quad)
