from collections import defaultdict

grid = [line.strip() for line in open("input.txt")]

antennas = defaultdict(list)

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char != ".":
            antennas[char].append((r, c))

antinodes = set()
for arr in antennas.values():
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            r1, c1 = arr[i]
            r2, c2 = arr[j]
            # 2r1 - r2, 2c1 - c2
            antinodes.add((r1 - (r2 - r1), c1 - (c2 - c1)))
            # 2r2 - r1, 2c2 - c1
            antinodes.add((r2 + (r2 - r1), c2 + (c2 - c1)))

print(sum(1 for r, c in antinodes if 0 <= r < len(grid) and 0 <= c < len(grid[0])))
