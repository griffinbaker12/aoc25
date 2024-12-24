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

# 1) robot at the num_keypad (starts at A in bottom right)
# 2) robot also needs to go to the dir_keypad (starts at A at top left)
# 3) second robot also using the dir_keypad to control the second one
# 4) one directional keypad that we are using
# can never go over one either


def solve_numkeypad(code):
    q = deque([(len(num_keypad) - 1, len(num_keypad[0]) - 1, "", "")])
    visited = set()

    while q:
        cr, cc, path, ans = q.popleft()

        # If we've entered our full code and we're back at A, we're done
        if ans == code:
            return path

        current_button = str(num_keypad[cr][cc])
        next_digit = code[len(ans)]

        # If we're at the next button we need, we can press it
        if current_button == next_digit:
            # current shortest path to this ans path
            new_state = (cr, cc, ans + current_button)
            if new_state not in visited:
                q.append((cr, cc, path + "A", ans + current_button))
                visited.add(new_state)

        # We can always try moving in any valid direction
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
            if new_state not in visited:
                q.append((nr, nc, path + dir, ans))
                visited.add(new_state)

    return None


def solve_dirkeypad(target_seq):
    q = deque([(0, 2, "", "")])
    visited = set()

    while q:
        cr, cc, path, ans = q.popleft()

        # If we've entered our full code and we're back at A, we're done
        if ans == target_seq:
            return path

        current_button = str(dir_keypad[cr][cc])
        next_move = target_seq[len(ans)]

        # If we're at the next button we need, we can press it
        if current_button == next_move:
            # current shortest path to this ans path
            new_state = (cr, cc, ans + current_button)
            if new_state not in visited:
                q.append((cr, cc, path + "A", ans + current_button))
                visited.add(new_state)

        # We can always try moving in any valid direction
        for nr, nc, dir in (
            (cr - 1, cc, "^"),
            (cr + 1, cc, "v"),
            (cr, cc - 1, "<"),
            (cr, cc + 1, ">"),
        ):
            if (
                nr < 0
                or nr >= len(dir_keypad)
                or nc < 0
                or nc >= len(dir_keypad[0])
                or dir_keypad[nr][nc] is None
            ):
                continue

            new_state = (nr, nc, ans)
            if new_state not in visited:
                q.append((nr, nc, path + dir, ans))
                visited.add(new_state)

    return None


# def compute_complexity(code_len, seq):


t = 0
for i, code in enumerate(codes):
    print("*" * 50)
    print(f"solving code {i+1}: {code}")

    r1_seq = solve_numkeypad(code)
    print(f"optimal r1 seq: {r1_seq}")

    r2_seq = solve_dirkeypad(r1_seq)
    print(f"optimal r2 seq: {r2_seq}")

    r3_seq = solve_dirkeypad(r2_seq)
    print(f"optimal r3 seq: {r3_seq}")

    t += len(r3_seq) * int(code.rstrip("A"))

print(t)
