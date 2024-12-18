# he said something about the new line char maybe not being used as the line break?
top, bottom = open(0).read().split("\n\n")

expansion = {"#": "##", "O": "[]", ".": "..", "@": "@."}

grid = [list(("".join(char for char in line))) for line in top.splitlines()]
moves = bottom.replace("\n", "")

rows = len(grid)
cols = len(grid[0])

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "@":
            break
    else:
        continue
    break

move_mp = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}

for move in moves:
    dr, dc = move_mp[move]
    targets = [(r, c)]  # type: ignore
    go = True
    for cr, cc in targets:
        nr = cr + dr
        nc = cc + dc
        if (nr, nc) in targets:
            continue
        char = grid[nr][nc]
        if char == "#":
            go = False
            break
        if char == "[":
            targets.append((nr, nc))
            targets.append((nr, nc + 1))
        if char == "]":
            targets.append((nr, nc))
            targets.append((nr, nc - 1))
    if not go:
        continue
    copy = [list(row) for row in grid]
    grid[r][c] = "."  # type: ignore
    grid[r + dr][c + dc] = "@"  # type: ignore
    for br, bc in targets[1:]:
        grid[br][bc] = "."
    for br, bc in targets[1:]:
        grid[br + dr][bc + dc] = copy[br][dr]
    r += dr
    c += dc

print(sum(100 * r + c for r in range(rows) for c in range(cols) if grid[r][c] == "["))
