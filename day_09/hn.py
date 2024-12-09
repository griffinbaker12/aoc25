disk = []
id = 0

for i, char in enumerate(open("test.txt").read().strip()):
    x = int(char)
    if i % 2 == 0:
        disk += [id] * x
        id += 1
    else:
        disk += [-1] * x

blanks = [i for i, x in enumerate(disk) if x == -1]

for i in blanks:
    while disk[-1] == -1:
        disk.pop()
    if len(disk) <= i:
        break
    disk[i] = disk.pop()

print(sum(i * x for i, x in enumerate(disk)))
