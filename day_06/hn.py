grid = list(map(list, open("test.txt").read().splitlines()))
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

dr, dc = -1, 0

# necessary bc we may revisit points
seen = set()

while True:
    # add current pos
    seen.add((r, c))  # type: ignore
    # check if next pos is outside the grid
    if r + dr < 0 or r + dr >= len(grid) or r + dc < 0 or c + dc >= len(grid[0]):  # type: ignore
        break
    # not outside grid, change dir or move to next pos
    if grid[r + dr][c + dc] == "#":  # type: ignore
        dc, dr = -dr, dc
    else:
        r += dr  # type: ignore
        c += dc  # type: ignore

print(len(seen))
