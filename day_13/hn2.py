import re

p1 = False
total = 0
for block in open(0).read().split("\n\n"):
    ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", block))
    if not p1:
        px, py = [p + 10000000000000 for p in (px, py)]
    i = (px * by - py * bx) / (ax * by - ay * bx)
    j = (px - (ax * i)) / bx
    if p1 and (i > 100 or j > 100):
        continue
    total += i * 3 + j if all(c % 1 == 0 for c in (i, j)) else 0
print(total)
