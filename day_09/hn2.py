# fid -> (pos, len)
files = {}
# (pos, len)
blanks = []

fid = 0
pos = 0

for i, char in enumerate(open("input.txt").read().strip()):
    x = int(char)
    if i % 2 == 0:
        # only 0s are blanks, but if there were a file with size 0, then the blanks
        # on both sides would be joined and problem doesn't say whether to skip 1 or 2 for id
        files[fid] = (pos, x)
        fid += 1
    else:
        # only add blanks with a length
        if x != 0:
            blanks.append((pos, x))
    pos += x

while fid > 0:
    fid -= 1
    pos, size = files[fid]
    for i, (start, length) in enumerate(blanks):
        if start >= pos:
            blanks = blanks[:i]
            break
        if size <= length:
            files[fid] = (start, size)
            # blank no longer exists
            if size == length:
                blanks.pop(i)
            else:
                blanks[i] = (start + size, length - size)
            break

# add up using gaussian summation?? said it is way more effcient and that it could be done
# mathematically to avoid looping
# file is now contiguous and can add adj indices using gaussian summation
# one line in max efficiency
# total = 0
# for fid, (pos, size) in files.items():
#     end = pos + size - 1
#     total += fid * (size * (pos + end) // 2)
# print(total)

print(sum(fid * size * (2 * pos + size - 1) // 2 for fid, (pos, size) in files.items()))
