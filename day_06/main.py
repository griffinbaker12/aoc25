# move_mp = {"up": "right", "right": "down", "down": "left", "left": "up"}
# current_pos = "up"
# start_i, start_j = 0, 0
# total = 0
#
#
# def walk(i, j):
#     if current_pos == "up":
#         i -= 1
#     elif current_pos == "right":
#         j += 1
#     elif current_pos == "down":
#         i += 1
#     else:
#         j -= 1
#     return i, j
#
#
# seen = set()
# with open("input.txt") as f:
#     map = [line.strip() for line in f]
#     for i, line in enumerate(map):
#         for j, c in enumerate(line):
#             if c == "^":
#                 start_i, start_j = i, j
#     i, j = start_i, start_j
#     while 0 <= i < len(map) and 0 <= j < len(map[0]):
#         if map[i][j] == "#":
#             # go back in direction you came...
#             if current_pos == "up":
#                 i += 1
#             elif current_pos == "right":
#                 j -= 1
#             elif current_pos == "down":
#                 i -= 1
#             else:
#                 j += 1
#             current_pos = move_mp[current_pos]
#         else:
#             seen.add((i, j))
#             i, j = walk(i, j)
# print(len(seen))


def simulate_guard(map_data, start_i, start_j):
    move_mp = {"up": "right", "right": "down", "down": "left", "left": "up"}
    current_pos = "up"
    i, j = start_i, start_j
    path = [(i, j, current_pos)]

    while True:
        next_i, next_j = i, j
        if current_pos == "up":
            next_i -= 1
        elif current_pos == "right":
            next_j += 1
        elif current_pos == "down":
            next_i += 1
        else:
            next_j -= 1

        # Check if guard leaves map
        if not (0 <= next_i < len(map_data) and 0 <= next_j < len(map_data[0])):
            return False

        if map_data[next_i][next_j] == "#":
            current_pos = move_mp[current_pos]
        else:
            i, j = next_i, next_j

        state = (i, j, current_pos)
        if state in path:
            return True
        path.append(state)


with open("input.txt") as f:
    original_map = [list(line.strip()) for line in f]

start_i = start_j = 0
for i, line in enumerate(original_map):
    for j, c in enumerate(line):
        if c == "^":
            start_i, start_j = i, j
            break

loop_positions = 0
for i in range(len(original_map)):
    for j in range(len(original_map[0])):
        if original_map[i][j] == "." and (i, j) != (start_i, start_j):
            # Try placing obstacle here
            map_copy = [row[:] for row in original_map]
            map_copy[i][j] = "#"
            if simulate_guard(map_copy, start_i, start_j):
                loop_positions += 1

print("?", loop_positions)


def next_position(i, j, direction, map_data):
    next_i, next_j = i, j
    if direction == "up":
        next_i -= 1
    elif direction == "right":
        next_j += 1
    elif direction == "down":
        next_i += 1
    else:
        next_j -= 1

    if not (0 <= next_i < len(map_data) and 0 <= next_j < len(map_data[0])):
        return None
    return next_i, next_j


def has_loop(map_data, start_i, start_j):
    move_mp = {"up": "right", "right": "down", "down": "left", "left": "up"}

    t_i, t_j, t_dir = start_i, start_j, "up"
    h_i, h_j, h_dir = start_i, start_j, "up"

    while True:
        # Move tortoise one step
        t_next = next_position(t_i, t_j, t_dir, map_data)
        if not t_next:
            return False
        if map_data[t_next[0]][t_next[1]] == "#":
            t_dir = move_mp[t_dir]
        else:
            t_i, t_j = t_next

        # Move hare two steps
        for _ in range(2):
            h_next = next_position(h_i, h_j, h_dir, map_data)
            if not h_next:
                return False
            if map_data[h_next[0]][h_next[1]] == "#":
                h_dir = move_mp[h_dir]
            else:
                h_i, h_j = h_next

        if (t_i, t_j, t_dir) == (h_i, h_j, h_dir):
            return True


with open("input.txt") as f:
    original_map = [list(line.strip()) for line in f]

start_i = start_j = 0
for i, line in enumerate(original_map):
    for j, c in enumerate(line):
        if c == "^":
            start_i, start_j = i, j
            break

loop_positions = 0
for i in range(len(original_map)):
    for j in range(len(original_map[0])):
        if original_map[i][j] == "." and (i, j) != (start_i, start_j):
            map_copy = [row[:] for row in original_map]
            map_copy[i][j] = "#"
            if has_loop(map_copy, start_i, start_j):
                loop_positions += 1

print(loop_positions)
