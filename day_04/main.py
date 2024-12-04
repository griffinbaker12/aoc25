def search_grid_1(grid):
    def check_direction(i, j, dr, dc):
        pattern = "XMAS"
        for char in pattern:
            if not (0 <= i < len(grid) and 0 <= j < len(grid[0])):
                return False
            if grid[i][j] != char:
                return False
            i += dr
            j += dc
        return True

    total = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "X":
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == dc == 0:
                            continue
                        if check_direction(r, c, dr, dc):
                            total += 1
    return total


def search_grid_2(grid):
    def check_pattern_through_a(i, j):
        patterns_found = 0
        dr = 1
        for dc in [1, -1]:
            back_i, back_j = i - dr, j - dc
            front_i, front_j = i + dr, j + dc
            if (
                0 <= back_i < len(grid)
                and 0 <= back_j < len(grid[0])
                and 0 <= front_i < len(grid[0])
                and 0 <= front_j < len(grid[0])
            ):
                if grid[back_i][back_j] == "M" and grid[front_i][front_j] == "S":
                    patterns_found += 1
                if grid[back_i][back_j] == "S" and grid[front_i][front_j] == "M":
                    patterns_found += 1
        return 1 if patterns_found == 2 else 0

    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "A":
                total += check_pattern_through_a(i, j)
    return total


with open("input.txt", "r") as f:
    grid = []
    for line in f:
        grid.append([c for c in line.strip()])
    print(search_grid_1(grid))
    print(search_grid_2(grid))
