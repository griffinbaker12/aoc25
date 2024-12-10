# so you want to go every direction, in order, and make sure you dont go back while you are searching
# I guess you could solve that by stepping if the next value is one more, else break?


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# when I set a default set here, the answer was wrong? but when I passed one in below, it worked
def walk(trails, r, c, nines=set()):
    for dr, dc in dirs:
        new_r, new_c = r + dr, c + dc
        if 0 <= r + dr < len(trails) and 0 <= new_c < len(trails[0]):
            if trails[new_r][new_c] == trails[r][c] + 1:
                if trails[new_r][new_c] == 9:
                    nines.add((new_r, new_c))
                else:
                    walk(trails, new_r, new_c, nines)
    return len(nines)


total = 0
with open("input.txt") as f:
    trails = [list(map(int, line.strip())) for line in f.readlines()]
    for r, row in enumerate(trails):
        for c, char in enumerate(row):
            if char == 0:
                # GOOD: need new set for each trailhead
                total += walk(trails, r, c, set())
                # BAD
                # total += walk(trails, r, c)


print(total)
