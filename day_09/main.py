with open("test.txt") as f:
    blocks = []
    id = 0
    blank = False
    for line in f.readlines():
        for i, char in enumerate(line.strip()):
            amt = int(char)
            if blank:
                c = "."
                blank = False
            else:
                c = id
                id += 1
                blank = True
            c_len = 0
            for _ in range(amt):
                c_len += 1
                blocks.append(c)
    l, r = 0, len(blocks) - 1
    l_len, r_len = 0, 0
    move_l = True
    while l < r:
        print(l, r)
        if move_l:
            while l < r and blocks[l] != ".":
                l += 1
            while l < r and blocks[l] == ".":
                l_len += 1
                l += 1
        while r > l and blocks[r] == ".":
            r -= 1
        curr_num = blocks[r]
        while r > l and blocks[r] == curr_num:
            r_len += 1
            r -= 1
        if l_len >= r_len:
            l_start = l - l_len
            for i in range(r_len):
                blocks[l_start + i], blocks[r + i + 1] = (
                    blocks[r + i + 1],
                    blocks[l_start + i],
                )
            move_l = True
        else:
            move_l = False
    # while l < r:
    #     print(l, r)
    #     while l < r and blocks[l] != ".":
    #         l += 1
    #     blocks[l], blocks[r] = blocks[r], blocks[l]
    #     r -= 1
    total = 0
    for i, v in enumerate(blocks):
        if v == ".":
            break
        total += i * v
    print(total)
