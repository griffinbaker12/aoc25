import re


def solve_multiplications(text):
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, text)

    total = 0
    for match in matches:
        num1, num2 = map(int, match.groups())
        total += num1 * num2
    return total


def solve_multiplications_with_state(text):
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"

    # TODO: under the hood this is creating a new object with internal storage right? that you can then iterate over...
    muls = [
        (m.start(), int(m.group(1)), int(m.group(2)))
        for m in re.finditer(mul_pattern, text)
    ]
    dos = [m.start() for m in re.finditer(do_pattern, text)]
    donts = [m.start() for m in re.finditer(dont_pattern, text)]

    all_events = (
        [(pos, "do") for pos in dos]
        + [(pos, "dont") for pos in donts]
        + [(pos, "mul", x, y) for pos, x, y in muls]
    )
    all_events.sort()

    enabled = True
    total = 0
    for event in all_events:
        if event[1] == "do":
            enabled = True
        elif event[1] == "dont":
            enabled = False
        else:  # mul
            if enabled:
                total += event[2] * event[3]  # type: ignore
    return total


text = open("input.txt").read()
print(solve_multiplications(text))
print(solve_multiplications_with_state(text))
