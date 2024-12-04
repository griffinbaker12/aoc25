grid = open(0).read().splitlines()

total = 0

# for r in range(len(grid)):
#     for c in range(len(grid[0])):
#         if grid[r][c] != "X":
#             continue
#         for dr in [-1, 0, 1]:
#             for dc in [-1, 0, 1]:
#                 if dr == dc == 0:
#                     continue
#                 if not (0 <= r + 3 * dr < len(grid) and 0 <= c + 3 * dc < len(grid[0])):
#                     continue
#                 for i, char in enumerate(["M", "A", "S"], 1):
#                     if grid[r + dr * i][c + dc * i] != char:
#                         break
#                 else:
#                     total += 1

for r in range(1, len(grid) - 1):
    for c in range(1, len(grid[0]) - 1):
        if grid[r][c] != "A":
            continue
        dirs = [-1, 1]
        corners = "".join([grid[r + dr][c + dc] for dr in dirs for dc in dirs])
        print(corners)
        if corners in ("MMSS", "MSMS", "SSMM", "SMSM"):
            total += 1

print(total)
