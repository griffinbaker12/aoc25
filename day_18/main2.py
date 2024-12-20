import time

H, W = 71, 71
# SIM = 1024

END = (H - 1, W - 1)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_path(grid, cr, cc, seen):
    # print(cr, cc)
    if END == (cr, cc):
        return True
    for dr, dc in DIRS:
        nr, nc = cr + dr, cc + dc
        if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in seen and grid[nr][nc] == ".":
            seen.add((nr, nc))
            if find_path(grid, nr, nc, seen):
                return True
            seen.remove((nr, nc))
    return False


s = time.time()
with open("input.txt") as f:
    grid = [["." for _ in range(W)] for _ in range(H)]
    coords = [list(map(int, line.strip().split(","))) for line in f.readlines()]
    for i in range(len(coords)):
        c, r = coords[i]
        grid[r][c] = "#"
        if not find_path(grid, 0, 0, set()):
            print(c, r, sep=",")
            break
print(f"Took: {time.time() - s:.3f}s")
# else:
# print("found_path")
