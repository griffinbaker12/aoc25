import heapq

grid = [line for line in open("input.txt").read().splitlines()]
MOVE_COST = 1
ROT_COST = 1000
rows = len(grid)
cols = len(grid[0])

# Find start
for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break

# Use heap for minimum cost
seen = set()
# (cost, row, col, dr, dc)
pq = [(0, r, c, 0, 1)]  # Start facing east

while pq:
    cost, cr, cc, dr, dc = heapq.heappop(pq)

    state = (cr, cc, dr, dc)
    if state in seen:
        continue
    seen.add(state)

    # Found end
    if grid[cr][cc] == "E":
        print(cost)
        break

    # Try moving forward
    nr, nc = cr + dr, cc + dc
    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != "#":
        heapq.heappush(pq, (cost + MOVE_COST, nr, nc, dr, dc))

    # Try rotations
    # Clockwise: (dr,dc) -> (dc,-dr)
    heapq.heappush(pq, (cost + ROT_COST, cr, cc, dc, -dr))
    # Counter-clockwise: (dr,dc) -> (-dc,dr)
    heapq.heappush(pq, (cost + ROT_COST, cr, cc, -dc, dr))
