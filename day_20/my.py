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

    for d in dists:
        print(*d, sep="\t")

    normal_dist = dists[end[0]][end[1]]
    savings = set()

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                continue
            for nr, nc in ((cr + 2, cc), (cr, cc + 2)):
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] not in ("#", -1)
                    and ((dist := dists[nr][nc] - dists[r][c]) > 0)
                ):
                    key = tuple(sorted(((cr, cc), (nr, nc))))
                    savings.add((key, dist - 2))

    # for cr in range(rows):
    #     for cc in range(cols):
    #         if dists[cr][cc] == -1:
    #             continue
    #         for rtc, ctc, nr, nc in (
    #             (cr + 1, cc, cr + 2, cc),
    #             (cr - 1, cc, cr - 2, cc),
    #             (cr, cc + 1, cr, cc + 2),
    #             (cr, cc - 1, cr, cc - 2),
    #         ):
    #             if (
    #                 0 <= nr < rows
    #                 and 0 <= nc < cols
    #                 and ((dist := dists[nr][nc] - dists[cr][cc]) > 0)
    #                 and dists[rtc][ctc] == -1
    #             ):
    #                 savings.add(((cr, cc), (nr, nc), dist - 2))
    #
    print(len([s for s in savings if s[1] >= 100]))
    # print(savings)
    # counts = {}
    # for _, _, d in sorted(savings, key=lambda s: s[2]):
    #     if d not in counts:
    #         counts[d] = 0
    #     counts[d] += 1
    # print(counts)
