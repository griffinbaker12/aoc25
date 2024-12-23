from functools import cache

lines = open(0).read().splitlines()

patterns = lines[0].split(", ")
maxlen = max(map(len, patterns))


@cache
def can_obtain(design):
    if design == "":
        return True
    for i in range(min(len(design), maxlen) + 1):
        # if design[:i] in patterns and can_obtain(design[i:]):
        #     return True
        if design[:i] in patterns:
            return can_obtain(design[i:])
    return False


print(sum(can_obtain(d) for d in lines[2:]))
