import time
from collections import deque

H, W = 71, 71


def bfs(grid):
    end = (H - 1, W - 1)

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # row, column, distance
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        row, col, dist = queue.popleft()

        if (row, col) == end:
            return True

        for dr, dc in dirs:
            nr, nc = row + dr, col + dc
            if 0 <= nr < H and 0 <= nc < W and (nr, nc) not in visited and grid[nr][nc] == ".":
                queue.append((nr, nc, dist + 1))
                visited.add((nr, nc))
    return False


s = time.time()
with open("input.txt") as f:
    grid = [["." for _ in range(W)] for _ in range(H)]
    coords = [list(map(int, line.strip().split(","))) for line in f.readlines()]
    for i in range(len(coords)):
        c, r = coords[i]
        grid[r][c] = "#"
        if not bfs(grid):
            print(c, r, sep=",")
            break
print(f"Took: {time.time() - s:.3f}s")
