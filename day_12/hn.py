from collections import deque

grid = [list(line.strip()) for line in open("test.txt")]

rows = len(grid)
cols = len(grid[0])

regions = []
seen = set()

for r in range(rows):
    for c in range(cols):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        region = {(r, c)}
        q = deque([(r, c)])
        crop = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == crop
                    and (nr, nc) not in region
                ):
                    region.add((nr, nc))
                    q.append((nr, nc))
        seen |= region
        regions.append(region)


def perim(region):
    output = 0
    for r, c in region:
        output += 4
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c - 1), (r, c + 1)]:
            if (nr, nc) in region:
                output -= 1
    return output


print(sum(len(region) * perim(region) for region in regions))
