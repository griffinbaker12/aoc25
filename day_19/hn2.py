from functools import cache

lines = open(0).read().splitlines()
patterns = lines[0].split(", ")
maxlen = max(map(len, patterns))


@cache
def count_ways(design):
    if design == "":
        return 1
    total = 0
    for i in range(min(len(design), maxlen) + 1):
        if design[:i] in patterns:
            total += count_ways(design[i:])
    return total


print(sum(count_ways(d) for d in lines[2:]))
