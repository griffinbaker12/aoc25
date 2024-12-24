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


def compute_paths_between_buttons(keypad):
    """
    Precompute shortest paths between all pairs of buttons on a keypad.
    Returns a dictionary where:
    - key: tuple of (start_button, end_button)
    - value: list of all shortest paths between those buttons
    """
    paths = {}  # Will store all shortest paths between each pair of buttons

    # First, map button values to their positions
    button_positions = {}
    for r in range(len(keypad)):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                button_positions[str(keypad[r][c])] = (r, c)

    # For each pair of buttons, find all shortest paths between them
    for start_button in button_positions:
        for end_button in button_positions:
            if start_button == end_button:
                # Same button - just need to press it
                paths[(start_button, end_button)] = ["A"]
                continue

            # Find all shortest paths from start to end button
            start_pos = button_positions[start_button]
            end_pos = button_positions[end_button]

            q = deque([(start_pos, "")])
            shortest_paths = []
            min_length = float("inf")
            state_lengths = {}

            while q:
                (cr, cc), path = q.popleft()

                if len(path) > min_length:
                    continue

                # Check if we've reached the target button
                if (cr, cc) == end_pos:
                    if len(path) < min_length:
                        shortest_paths = [path + "A"]
                        min_length = len(path)
                    elif len(path) == min_length:
                        shortest_paths.append(path + "A")
                    continue

                # Try moving in each direction
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

                    new_state = (nr, nc)
                    new_length = len(path) + 1
                    if (
                        new_state not in state_lengths
                        or new_length <= state_lengths[new_state]
                    ):
                        state_lengths[new_state] = new_length
                        q.append((new_state, path + dir))

            paths[(start_button, end_button)] = shortest_paths

    return paths


def solve_with_cached_paths(sequence, cached_paths, start_button="A"):
    """
    Find all shortest paths to type a sequence using precomputed paths between buttons.
    """
    if not sequence:
        return [""]

    shortest_paths = []
    min_length = float("inf")

    # Get all paths from current button to first button of sequence
    for path in cached_paths[(start_button, sequence[0])]:
        # Recursively find paths for rest of sequence
        for rest_path in solve_with_cached_paths(
            sequence[1:], cached_paths, sequence[0]
        ):
            full_path = path + rest_path
            if len(full_path) < min_length:
                shortest_paths = [full_path]
                min_length = len(full_path)
            elif len(full_path) == min_length:
                shortest_paths.append(full_path)

    return shortest_paths


# Precompute paths for both keypads
num_paths = compute_paths_between_buttons(num_keypad)
dir_paths = compute_paths_between_buttons(dir_keypad)


def find_shortest_sequence(code):
    """Find shortest sequence using precomputed paths."""
    # Get all shortest paths for Robot 1 on numeric keypad
    r1_paths = solve_with_cached_paths(code, num_paths)
    print(f"Found {len(r1_paths)} optimal paths for Robot 1")

    shortest_r3_sequence = None
    min_r3_length = float("inf")

    for r1_path in r1_paths:
        r2_paths = solve_with_cached_paths(r1_path, dir_paths)
        print(f"Found {len(r2_paths)} optimal paths for Robot 2")

        for r2_path in r2_paths:
            r3_paths = solve_with_cached_paths(r2_path, dir_paths)

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

    numeric_part = int(code[:-1].lstrip("0"))
    complexity = length * numeric_part
    total_complexity += complexity
    print(f"Complexity: {length} * {numeric_part} = {complexity}")

print(f"\nTotal complexity: {total_complexity}")
