# moves the complexity from (o(n*m)^2) to (o(n*m + p(n*m))), where p is the length of the path.
# caching the path improves our solution as long as p < n*m

grid = list(map(list, open("input.txt").read().splitlines()))
# grid = [list(line) for line in open("test.txt").read().splitlines()]
# print(grid)

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "^":
            break
    else:
        continue
    break

r2, c2 = r, c  # type: ignore

path = set()
dr2, dc2 = -1, 0
while True:
    # add current pos
    path.add((r2, c2))  # type: ignore
    # check if next pos is outside the grid
    if (
        r2 + dr2 < 0
        or r2 + dr2 >= len(grid)
        or c2 + dc2 < 0
        or c2 + dc2 >= len(grid[0])
    ):  # type: ignore
        break
    # not outside grid, change dir or move to next pos
    if grid[r2 + dr2][c2 + dc2] == "#":  # type: ignore
        dc2, dr2 = -dr2, dc2
    else:
        r2 += dr2  # type: ignore
        c2 += dc2  # type: ignore

print(len(path))

# exit()


def loops(grid, r, c):
    dr, dc = -1, 0

    # necessary bc we may revisit points
    seen = set()

    while True:
        # add current pos
        # imagine that we had to keep track of this and that it did not hash to the same
        # val everytime and we had to keep track of the different variables...haha
        # we would not even be able to store them in a hash table/set
        seen.add((r, c, dr, dc))  # type: ignore
        # check if next pos is outside the grid
        if r + dr < 0 or r + dr >= len(grid) or c + dc < 0 or c + dc >= len(grid[0]):  # type: ignore
            return False
        # not outside grid, change dir or move to next pos
        if grid[r + dr][c + dc] == "#":  # type: ignore
            dc, dr = -dr, dc
        else:
            r += dr  # type: ignore
            c += dc  # type: ignore
        if (r, c, dr, dc) in seen:
            return True


total = 0
for cr in range(rows):
    for cc in range(cols):
        if grid[cr][cc] != "." or (cr, cc) not in path:
            continue
        grid[cr][cc] = "#"
        if loops(grid, r, c):  # type: ignore
            total += 1
        grid[cr][cc] = "."
print(total)
