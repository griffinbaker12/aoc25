from collections import deque

codes = [line.strip() for line in open(0)]


num_keypad = [
    [7, 8, 9],
    [4, 5, 6],
    [1, 2, 3],
    [None, 0, "A"],
]

dir_keypad = [
    [None, "^", "A"],
    ["<", "v", ">"],
]

def solve_numkeypad(code):
    q = deque([(len(num_keypad) - 1, len(num_keypad[0]) - 1, "", "")])
    shortest_paths = []
    min_length = float("inf")
    state_lengths = {}

    while q:
        cr, cc, path, ans = q.popleft()
        curr_len = len(path)

        if curr_len > min_length:
            continue

        if ans == code:
            if curr_len < min_length:
                shortest_paths = [path]
                min_length = curr_len
            elif curr_len == min_length:
                shortest_paths.append(path)
            continue

        current_button = str(num_keypad[cr][cc])
        next_digit = code[len(ans)] if len(ans) < len(code) else None

        if next_digit and current_button == next_digit:
            new_state = (cr, cc, ans + current_button)
            new_length = curr_len + 1
            if new_state not in state_lengths or new_length <= state_lengths[new_state]:
                state_lengths[new_state] = new_length
                q.append((cr, cc, path + "A", ans + current_button))

        for nr, nc, dir in (
            (cr - 1, cc, "^"),
            (cr + 1, cc, "v"),
            (cr, cc - 1, "<"),
            (cr, cc + 1, ">"),
        ):
            if (
                nr < 0
                or nr >= len(num_keypad)
                or nc < 0
                or nc >= len(num_keypad[0])
                or num_keypad[nr][nc] is None
            ):
                continue

            new_state = (nr, nc, ans)
            new_length = curr_len + 1
            if new_state not in state_lengths or new_length <= state_lengths[new_state]:
                state_lengths[new_state] = new_length
                q.append((nr, nc, path + dir, ans))

    return shortest_paths


def solve_dirkeypad(target_sequence, keypad=dir_keypad, start_pos=(0, 2)):
    q = deque([(*start_pos, "", "")])
    shortest_paths = []
    min_length = float("inf")
    state_lengths = {}

    while q:
        cr, cc, path, ans = q.popleft()
        curr_len = len(path)

        if curr_len > min_length:
            continue

        if ans == target_sequence:
            if curr_len < min_length:
                shortest_paths = [path]
                min_length = curr_len
            elif curr_len == min_length:
                shortest_paths.append(path)
            continue

        current_button = str(keypad[cr][cc])
        next_move = (
            target_sequence[len(ans)] if len(ans) < len(target_sequence) else None
        )

        if next_move and current_button == next_move:
            new_state = (cr, cc, ans + current_button)
            new_length = curr_len + 1
            if new_state not in state_lengths or new_length <= state_lengths[new_state]:
                state_lengths[new_state] = new_length
                q.append((cr, cc, path + "A", ans + current_button))

        for nr, nc, dir in (
            (cr - 1, cc, "^"),
            (cr + 1, cc, "v"),
            (cr, cc - 1, "<"),
            (cr, cc + 1, ">"),
        ):
            if (
                nr < 0
                or nr >= len(keypad)
                or nc < 0
                or nc >= len(keypad[0])
                or keypad[nr][nc] is None
            ):
                continue

            new_state = (nr, nc, ans)
            new_length = curr_len + 1
            if new_state not in state_lengths or new_length <= state_lengths[new_state]:
                state_lengths[new_state] = new_length
                q.append((nr, nc, path + dir, ans))

    return shortest_paths


def find_shortest_sequence(code):
    r1_paths = solve_numkeypad(code)
    print(f"Found {len(r1_paths)} optimal paths for Robot 1")

    shortest_r3_sequence = None
    min_r3_length = float("inf")

    for r1_path in r1_paths:
        r2_paths = solve_dirkeypad(r1_path)
        print(f"Found {len(r2_paths)} optimal paths for Robot 2")

        for r2_path in r2_paths:
            r3_paths = solve_dirkeypad(r2_path)

            for r3_path in r3_paths:
                if len(r3_path) < min_r3_length:
                    min_r3_length = len(r3_path)
                    shortest_r3_sequence = r3_path

    return shortest_r3_sequence, min_r3_length


# Process each code
total_complexity = 0
for code in codes:
    code = code.strip()
    print(f"\nProcessing code: {code}")
    sequence, length = find_shortest_sequence(code[:-1])
    print(f"Shortest sequence length: {length}")

    numeric_part = int(code[:-1].lstrip("0"))
    complexity = length * numeric_part
    total_complexity += complexity
    print(f"Complexity: {length} * {numeric_part} = {complexity}")

print(f"\nTotal complexity: {total_complexity}")
