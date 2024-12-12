# so you want to go every direction, in order, and make sure you dont go back while you are searching
# I guess you could solve that by stepping if the next value is one more, else break?


dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


# when I set a default set here, the answer was wrong? but when I passed one in below, it worked
# def walk(trails, r, c, nines):
def walk(trails, r, c):
    # if trails[r][c] == 9:
    #     return 1
    total = 0
    for dr, dc in dirs:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < len(trails) and 0 <= new_c < len(trails[0]):
            if trails[new_r][new_c] == trails[r][c] + 1:
                if trails[r + dr][c + dc] == 9:
                    total += 1
                    # total += walk(trails, new_r, new_c)
                    # nines.append((r + dr, c + dc))
                else:
                    walk(trails, r + dr, c + dc)
                    # walk(trails, r + dr, c + dc, nines)
    return total


total = 0
with open("input.txt") as f:
    trails = [list(map(int, line.strip())) for line in f.readlines()]
    for r, row in enumerate(trails):
        for c, char in enumerate(row):
            if char == 0:
                total += walk(trails, r, c)


print(total)
