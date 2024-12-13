with open("test.txt") as f:
    config = {
        i: {
            letter: [
                int(dir.strip().split("=" if letter == "X" else "+")[1])
                for dir in line.split(":")[1].split(",")
            ]
            for line, letter in zip(chunk.splitlines(), ("A", "B", "X"))
        }
        for i, chunk in enumerate(f.read().split("\n\n"))
    }


def tokens(c):
    cheapest = float("inf")
    ax, ay, bx, by, tx, ty = (t for t in (c["A"], c["B"], c["X"]))
    for i in range(101):
        curr_x = ax * i
        # if you can get there from x
        if (remaining := (tx - curr_x)) % bx == 0:
            other_x = remaining // bx
            # and it is less than 100 pressses to get there
            if other_x > 100:
                continue
            # now check the y works too...
            if i * ay + other_x * by == ty:
                cost = 3 * i + other_x
                cheapest = min(cheapest, cost)
    return cheapest if cheapest != float("inf") else 0


print(sum(tokens(c) for c in config.values()))
