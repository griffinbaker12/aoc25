l1, l2 = [], []

with open("input.txt") as f:
    for line in f:
        v1, v2 = list(map(int, map(str.strip, line.split())))
        l1.append(v1)
        l2.append(v2)
        for l in (l1, l2):
            l.sort()
    t = 0
    print(sum(x * l2.count(x) for x in l1))
