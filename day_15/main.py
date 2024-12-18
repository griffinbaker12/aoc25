with open("test.txt") as f:
    grid = []
    moves = []
    for i, chunk in enumerate(f.read().split("\n\n")):
        if i == 0:
            grid = [list(c.strip()) for c in chunk.split()]
        else:
            moves = list(chunk.replace("\n", "").strip())
    print(moves)

    r, c = 0, 0
    for _r in range(len(grid)):
        for _c in range(len(grid[0])):
            if grid[_r][_c] == "@":
                r, c = _r, _c

    move_mp = {
        ">": (0, 1),
        "<": (0, -1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    for move in moves:
        c_d = move_mp[move]
        new_r, new_c = r + c_d[0], c + c_d[1]

        # we can move
        if 1 <= new_r < len(grid) - 1 and 1 <= new_c < len(grid[0]) - 1:
            # but need to check if next position is
            print(new_r, new_c)
            if grid[new_r][new_c] == "O":
                # keep moving in that direction to get the positions that you need to update
                _r, _c = new_r, new_c
                pts = [(grid[r][c], r, c)]
                while grid[_r][_c] == "O":
                    pts.append((grid[_r][_c], _r, _c))
                    _r, _c = _r + c_d[0], _c + c_d[1]
                print(pts)
                # there is no room
                if grid[_r][_c] == "#":
                    continue
                # can move these points
                else:
                    for pt in pts:
                        nr, nc = pt[1] + c_d[0], pt[2] + c_d[1]
                        grid[nr][nc] = pt[0]
                    grid[r][c] = "."
                    r, c = new_r, new_c

            # else, can just move to the next spot if not a hashtag
            elif grid[new_r][new_c] != "#":
                grid[r][c] = "."
                r, c = new_r, new_c
                grid[r][c] = "@"

        # print(move, "*" * 50)
        # for row in grid:
        #     print(row)

    t = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "O":
                t += 100 * r + c
    print(t)
