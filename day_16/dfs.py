grid = [list(line.strip()) for line in open("test.txt")]
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


def valid_move(r, c):
    return 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#"


global_min = float("inf")  # Track minimum cost found so far


def dfs(r, c, dr, dc, cost=0, seen=None):
    if seen is None:
        seen = set()

    global global_min

    # Prune if current path already too expensive or state seen
    if cost >= global_min or (r, c, dr, dc) in seen:
        return float("inf")

    # Found end - update global minimum
    if grid[r][c] == "E":
        global_min = min(global_min, cost)
        return cost

    seen.add((r, c, dr, dc))

    min_cost = float("inf")
    # Try moving forward
    if valid_move(r + dr, c + dc):
        min_cost = min(min_cost, dfs(r + dr, c + dc, dr, dc, cost + 1, seen))

    # Try rotations
    min_cost = min(min_cost, dfs(r, c, dc, -dr, cost + 1000, seen))  # clockwise
    min_cost = min(min_cost, dfs(r, c, -dc, dr, cost + 1000, seen))  # counter-clockwise

    seen.remove((r, c, dr, dc))
    return min_cost


# Start facing east
result = dfs(r, c, 0, 1)
print(f"Minimum cost: {result}")
