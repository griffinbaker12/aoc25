trails = [list(map(int, line.strip())) for line in open("input.txt")]
trailheads = [
    (r, c)
    for r in range(len(trails))
    for c in range(len(trails[0]))
    if trails[r][c] == 0
]


def walk(trails, r, c, nines):
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_r, new_c = r + dr, c + dc
        if 0 <= r + dr < len(trails) and 0 <= new_c < len(trails[0]):
            if trails[new_r][new_c] == trails[r][c] + 1:
                if trails[new_r][new_c] == 9:
                    nines.add((new_r, new_c))
                else:
                    walk(trails, new_r, new_c, nines)
    return len(nines)


print(sum(walk(trails, r, c, set()) for r, c in trailheads))
