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

    # BFS to get path
    q = deque([(start[0], start[1])])
    came_from = {start: None}

    while q:
        cr, cc = q.popleft()
        if (cr, cc) == end:
            break

        for nr, nc in ((cr + 1, cc), (cr - 1, cc), (cr, cc + 1), (cr, cc - 1)):
            if (
                0 <= nr < rows
                and 0 <= nc < cols
                and grid[nr][nc] != "#"
                and (nr, nc) not in came_from
            ):
                came_from[(nr, nc)] = (cr, cc)
                q.append((nr, nc))

    # Reconstruct path
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = came_from[current]
    path = path[::-1]  # Reverse to get S to E order

    # Check all pairs of positions in path
    savings = []
    for i in range(len(path)):
        # Optimization: Skip last 100 positions as suggested
        for j in range(i + 1, len(path)):
            r1, c1 = path[i]
            r2, c2 = path[j]
            manhattan_dist = abs(r2 - r1) + abs(c2 - c1)

            if manhattan_dist <= 2:  # Only valid cheats
                time_saved = (j - i) - manhattan_dist
                if time_saved >= 100:
                    savings.append(time_saved)

    print(f"Number of cheats saving >= 100: {len(savings)}")
