t = list(
    map(
        sorted,
        map(
            list,
            zip(
                *[
                    list(map(int, line.split()))
                    for line in open("test.txt").read().splitlines()
                ]
            ),
        ),
    )
)
print(sum(abs(a - b) for a, b in zip(*t)))
