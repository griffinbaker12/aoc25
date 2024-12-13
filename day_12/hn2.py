from collections import deque

# Parse the grid
grid = [list(line.strip()) for line in open("test.txt")]
rows, cols = len(grid), len(grid[0])

regions = []
seen = set()

# Identify regions using BFS
for r in range(rows):
    for c in range(cols):
        if (r, c) in seen:
            continue
        seen.add((r, c))
        region = {(r, c)}
        q = deque([(r, c)])
        plant = grid[r][c]
        while q:
            cr, cc = q.popleft()
            for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and grid[nr][nc] == plant
                    and (nr, nc) not in region
                ):
                    region.add((nr, nc))
                    q.append((nr, nc))
        seen |= region
        regions.append(region)


# Function to count vertices (and thus sides) of a region
def get_sides(region):
    vertices = 0

    for r, c in region:
        # Top-left corner
        if (r - 1, c) not in region or (r, c - 1) not in region:
            vertices += 1
        # Top-right corner
        if (r - 1, c) not in region or (r, c + 1) not in region:
            vertices += 1
        # Bottom-left corner
        if (r + 1, c) not in region or (r, c - 1) not in region:
            vertices += 1
        # Bottom-right corner
        if (r + 1, c) not in region or (r, c + 1) not in region:
            vertices += 1

    return vertices


# Compute the total cost for part 2
total_cost = sum(len(region) * get_sides(region) for region in regions)
print("Part 2 Total Cost:", total_cost)
