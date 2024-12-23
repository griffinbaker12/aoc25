grid = [line.strip() for line in open(0)]

rows = len(grid)
cols = len(grid[0])

# for r in range(rows):
#     for c in range(cols):
#         if grid[r][c] == "S":
#             break
#     else:
#         continue
#     break

for r in range(rows):
    for c in range(cols):
        if grid[r][c] == "S":
            break
    else:
        continue
    break
