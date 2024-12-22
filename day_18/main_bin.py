import time

H, W = 7, 7
# H, W = 71, 71
# SIM = 1024

END = (H - 1, W - 1)

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def find_path(grid, cr, cc, seen):
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


def try_path(coords, count):
    grid = [["." for _ in range(W)] for _ in range(H)]
    for i in range(count):
        c, r = coords[i]
        grid[r][c] = "#"
    return find_path(grid, 0, 0, set())


s = time.time()
with open("test.txt") as f:
    coords = [list(map(int, line.strip().split(","))) for line in f.readlines()]
    l, r = 0, len(coords) - 1
    answer = None
    while l < r:
        mid = (l + r) // 2
        print(f"PRE-SEARCH: l: {l}, r: {r}, mid: {mid}")
        if try_path(coords, mid + 1):
            l = mid + 1
            print(f"L is now {l}: {coords[l]}")
        else:
            r = mid
            print(f"R is now {r}: {coords[r]}")
    print(coords[l])

print(f"Took: {time.time() - s:.3f}s")
# else:
# print("found_path")
