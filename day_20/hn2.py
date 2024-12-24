from collections import deque

with open("input.txt") as f:
    grid = [line.strip() for line in f]
    rows = len(grid)
    cols = len(grid[0])
    # Find S and E positions
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "S":
                start = (r, c)
            elif grid[r][c] == "E":
                end = (r, c)

    # Get distances using BFS (same as part 1)
    dists = [[-1] * cols for _ in range(rows)]
    dists[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        cr, cc = q.popleft()
        for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] != "#"
                and dists[nr][nc] == -1
            ):
                dists[nr][nc] = dists[cr][cc] + 1
                q.append((nr, nc))

    normal_dist = dists[end[0]][end[1]]
    savings = set()

    # For each reachable starting position
    for cr in range(rows):
        for cc in range(cols):
            if dists[cr][cc] == -1:  # Skip unreachable positions
                continue

            # BFS to find all positions reachable within 20 steps (allowing wall passage)
            cheat_q = deque([(cr, cc, 0, False)])  # (row, col, steps, passed_wall)
            seen = {(cr, cc)}

            while cheat_q:
                r, c, steps, through_wall = cheat_q.popleft()

                # If we've used a wall and reached a valid path point, check if this saves time
                if through_wall and dists[r][c] != -1:
                    saved_time = dists[r][c] - dists[cr][cc] - steps
                    if saved_time > 0:
                        savings.add(((cr, cc), (r, c), saved_time))

                if steps >= 2:  # Max cheat length
                    continue

                # Try all four directions
                for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        # Mark if we've gone through a wall
                        new_through_wall = through_wall or grid[nr][nc] == "#"
                        cheat_q.append((nr, nc, steps + 1, new_through_wall))

    print(len([s for s in savings if s[2] >= 100]))
