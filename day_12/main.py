garden = [p for p in open("test.txt").read().split()]

# ends have perim of 3 (unless on its own)
# middle have perim of 2

# all on its own has perim of 4

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_area(curr, r, c, seen):
    seen.add((r, c))
    for dr, dc in dirs:
        new_r, new_c = r + dr, c + dc
        if 0 <= new_r < len(garden) and 0 <= new_c < len(garden[0]):
            next_val = garden[new_r][new_c]
            if next_val == curr and (new_r, new_c) not in seen:
                seen.add((new_r, new_c))
                get_area(next_val, new_r, new_c, seen)
    return len(seen), seen


def in_bounds_and_diff(r, c, new_r, new_c):
    return (
        0 <= new_r < len(garden)
        and 0 <= new_c < len(garden[0])
        and garden[new_r][new_c] != garden[r][c]
    )


def get_perim(pts):
    t = 0
    for r, c in pts:
        for dr, dc in dirs:
            new_r, new_c = r + dr, c + dc
            # OOB counts
            if not (0 <= new_r < len(garden) and 0 <= new_c < len(garden[0])):
                t += 1
            # diff value counts
            elif garden[new_r][new_c] != garden[r][c]:
                t += 1
    return t


def get_sides(pts):
    boundaries = set()
    curr = garden[list(pts)[0][0]][list(pts)[0][1]]

    for r, c in pts:
        for dr, dc in dirs:
            new_r, new_c = r + dr, c + dc
            if (
                not (0 <= new_r < len(garden) and 0 <= new_c < len(garden[0]))
                or garden[new_r][new_c] != curr
            ):
                boundaries.add((r, c, dr, dc))

    # Now only count unique rows/columns
    rows = set()  # For horizontal sides
    cols = set()  # For vertical sides
    for r, c, dr, dc in boundaries:
        if dc != 0:  # Horizontal side
            rows.add(r)
        if dr != 0:  # Vertical side
            cols.add(c)

    return len(rows) + len(cols)


mp = {}
p_seen = set()

for r in range(len(garden)):
    for c in range(len(garden[0])):
        if (r, c) in p_seen:
            continue

        curr = garden[r][c]
        area, c_seen = get_area(curr, r, c, set())
        # perim = get_perim(c_seen)
        sides = get_sides(c_seen)
        p_seen.update(c_seen)

        # Each region gets its own entry in the dictionary
        # mp[len(mp)] = {"type": curr, "area": area, "perim": perim}
        mp[len(mp)] = {"type": curr, "area": area, "sides": sides}

total = sum(v["area"] * v["sides"] for v in mp.values())
print(mp)
print(total)
