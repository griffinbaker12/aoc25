# so you want to go every direction, in order, and make sure you dont go back while you are searching
# I guess you could solve that by stepping if the next value is one more, else break?


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# when I set a default set here, the answer was wrong? but when I passed one in below, it worked
def walk(trails, r, c, nines):
    for dr, dc in dirs:
        if 0 <= r + dr < len(trails) and 0 <= c + dc < len(trails[0]):
            if trails[r + dr][c + dc] == trails[r][c] + 1:
                if trails[r + dr][c + dc] == 9:
                    nines.append((r + dr, c + dc))
                else:
                    walk(trails, r + dr, c + dc, nines)
    return len(nines)


total = 0
with open("input.txt") as f:
    trails = [list(map(int, line.strip())) for line in f.readlines()]
    for r, row in enumerate(trails):
        for c, char in enumerate(row):
            if char == 0:
                total += walk(trails, r, c, [])


print(total)
