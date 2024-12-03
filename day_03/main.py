import re


def solve_multiplications(text):
    # Match exactly mul(X,Y) where X,Y are 1-3 digits
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.finditer(pattern, text)

    total = 0
    for match in matches:
        print(match, match.groups())
        num1, num2 = map(int, match.groups())
        total += num1 * num2

    return total


def solve_multiplications_with_state(text):
    # Compile patterns
    mul_pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    do_pattern = r"do\(\)"
    dont_pattern = r"don\'t\(\)"

    # Find all matches with positions
    muls = [
        (m.start(), int(m.group(1)), int(m.group(2)))
        for m in re.finditer(mul_pattern, text)
    ]
    dos = [m.start() for m in re.finditer(do_pattern, text)]
    donts = [m.start() for m in re.finditer(dont_pattern, text)]

    # Combine and sort all state changes and multiplications
    enabled = True
    total = 0

    # Process events in order of position
    all_events = (
        [(pos, "do") for pos in dos]
        + [(pos, "dont") for pos in donts]
        + [(pos, "mul", x, y) for pos, x, y in muls]
    )
    all_events.sort()

    for event in all_events:
        if event[1] == "do":
            enabled = True
        elif event[1] == "dont":
            enabled = False
        else:  # mul
            if enabled:
                total += event[2] * event[3]

    return total


# Test
# text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)do()?mul(8,5))"


# Example test
text = open("input.txt").read()
print(solve_multiplications(text))  # Should print 161
print(solve_multiplications_with_state(text))  # Should print 48
