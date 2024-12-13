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


def extended_gcd(a, b):
    """Returns (gcd, x, y) where ax + by = gcd"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def find_min_cost_solution(a_move, b_move, target):
    """
    Find minimum cost solution where:
    a_move * a_presses + b_move * b_presses = target
    Cost is 3 * a_presses + b_presses
    """
    # First check if solution exists using GCD
    gcd, x0, y0 = extended_gcd(a_move, b_move)
    if target % gcd != 0:
        return None  # No solution exists

    # Scale up to get one solution
    scale = target // gcd
    x0 *= scale
    y0 *= scale

    # All solutions are of form:
    # x = x0 + k * (b_move/gcd)
    # y = y0 - k * (a_move/gcd)
    # where k is any integer

    # Find k that minimizes 3x + y
    # We want to minimize: 3(x0 + k*b_move/gcd) + (y0 - k*a_move/gcd)
    # Taking derivative and setting to 0:
    k = round(
        (3 * b_move / gcd - a_move / gcd)
        / (3 * (b_move / gcd) ** 2 + (a_move / gcd) ** 2)
        * (-y0 - 3 * x0)
    )

    # Get final solution
    x = x0 + k * (b_move // gcd)
    y = y0 - k * (a_move // gcd)

    if x < 0 or y < 0:  # Need non-negative solutions
        return None

    return (x, y)


def solve_machine(machine):
    """Solve for both X and Y coordinates"""
    move_ax, move_ay = machine["A"]
    move_bx, move_by = machine["B"]
    target_x, target_y = machine["X"]

    # Find solutions for both coordinates
    x_sol = find_min_cost_solution(move_ax, move_bx, target_x)
    y_sol = find_min_cost_solution(move_ay, move_by, target_y)

    if not x_sol or not y_sol:
        return None

    # Check if solutions match (same number of A and B presses)
    if x_sol == y_sol:
        return 3 * x_sol[0] + x_sol[1]  # Return cost
    return None


# Add 10^13 to each prize coordinate
for machine in config.values():
    machine["X"][0] += 10**13
    machine["X"][1] += 10**13

# Find total cost
total_cost = 0
for i, machine in config.items():
    cost = solve_machine(machine)
    if cost:
        print(f"Machine {i}: Cost {cost}")
        total_cost += cost
    else:
        print(f"Machine {i}: No solution")

print(f"Total cost: {total_cost}")
