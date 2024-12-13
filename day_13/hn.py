import re

total = 0
for block in open(0).read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    min_score = float("inf")
    for i in range(101):
        for j in range(101):
            if ax * i + bx * j == px and ay * i + by * j == py:
                min_score = min(min_score, i * 3 + j)
    if min_score != float("inf"):
        total += min_score
print(total)
