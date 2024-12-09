with open("input.txt") as f:
    # Parse input into blocks
    blocks = []
    id = 0
    blank = False
    for line in f.readlines():
        for char in line.strip():
            amt = int(char)
            if blank:
                c = "."
                blank = False
            else:
                c = id
                id += 1
                blank = True
            for _ in range(amt):
                blocks.append(c)

    # Find all file positions and lengths in reverse ID order
    files = {}  # id -> [(start_pos, length)]
    i = 0
    while i < len(blocks):
        if blocks[i] != ".":
            curr_id = blocks[i]
            curr_len = 1
            i += 1
            while i < len(blocks) and blocks[i] == curr_id:
                curr_len += 1
                i += 1
            files[curr_id] = [i - curr_len, curr_len]
        else:
            i += 1

    # for vals in files.values():
    #     if len(vals) > 1:
    #         print(vals)

    for curr_id in range(id - 1, -1, -1):
        l, l_len = None, 0
        r_start, r_len = files[curr_id]
        # move_l = True
        # try to find empty space
        for i in range(r_start):
            if blocks[i] == ".":
                if l is None:
                    l = i
                l_len += 1
                if l_len >= r_len:
                    for i in range(l, l + r_len):
                        blocks[i] = curr_id
                    for i in range(r_start, r_start + r_len):
                        blocks[i] = "."
                    break
            else:
                l = None
                l_len = 0

    # Calculate checksum
    total = 0
    for i, v in enumerate(blocks):
        if v != ".":
            total += i * int(v)
    print(total)
