from collections import deque
import heapq

grid = [list(line.strip()) for line in open("input.txt")]
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

pq = [(0, r, c, 0, 1)]  # cost, row, col, dr, dc
lowest_cost = {(r, c, 0, 1): 0}  # state -> lowest cost to reach it
backtrack = {}  # state -> set of previous states that led to it optimally
best_cost = float("inf")
end_states = set()

while pq:
    cost, r, c, dr, dc = heapq.heappop(pq)

    # Skip if we've found a better way here
    if cost > lowest_cost.get((r, c, dr, dc), float("inf")):
        continue

    if grid[r][c] == "E":
        if cost > best_cost:
            break
        best_cost = cost
        end_states.add((r, c, dr, dc))

    # Try all possible moves (forward and both rotations)
    moves = [
        (cost + 1, r + dr, c + dc, dr, dc),  # forward
        (cost + 1000, r, c, dc, -dr),  # clockwise
        (cost + 1000, r, c, -dc, dr),  # counter-clockwise
    ]

    for new_cost, nr, nc, ndr, ndc in moves:
        if not (0 <= nr < rows and 0 <= nc < cols) or grid[nr][nc] == "#":
            continue

        new_state = (nr, nc, ndr, ndc)
        lowest = lowest_cost.get(new_state, float("inf"))

        if new_cost > lowest:
            continue

        if new_cost < lowest:
            backtrack[new_state] = set()
            lowest_cost[new_state] = new_cost

        backtrack[new_state].add((r, c, dr, dc))
        heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc))

# Trace back from end states to find all positions on optimal paths
states = deque(end_states)
seen = set(end_states)

while states:
    current = states.popleft()
    for prev in backtrack.get(current, []):
        if prev in seen:
            continue
        seen.add(prev)
        states.append(prev)

# Count unique positions (ignoring direction)
optimal_positions = {(r, c) for r, c, _, _ in seen}
print(f"Part 2: {len(optimal_positions)}")
