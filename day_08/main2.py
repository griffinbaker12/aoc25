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
            r_diff, c_diff = r2 - r1, c2 - c1
            while 0 <= r1 < len(grid) and 0 <= c1 < len(grid[0]):
                antinodes.add((r1, c1))
                r1 -= r_diff
                c1 -= c_diff
            while 0 <= r2 < len(grid) and 0 <= c2 < len(grid[0]):
                antinodes.add((r2, c2))
                r2 += r_diff
                c2 += c_diff

print(len(antinodes))
