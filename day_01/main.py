from collections import defaultdict

col1, col2 = [], []

col2_hash = defaultdict(int)


with open("input.txt") as f:
    for line in f:
        v1, v2 = [int(v.strip()) for v in line.split("   ")]
        col1.append(v1)
        col2.append(v2)
    for v in col2:
        col2_hash[v] += 1
    total = sum(v * col2_hash[v] for v in col1)
    print(total)
    #     col1 = sorted(col1)
    #     col2 = sorted(col2)
    # total = sum(abs(v1 - v2) for v1, v2 in zip(col1, col2))
    # print(total)
