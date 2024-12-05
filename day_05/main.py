from collections import defaultdict, deque


def topological_sort(nums, rule_mp):
    """
    Takes a set of numbers and orders them according to rule dependencies.
    Uses Kahn's algorithm for topological sorting.
    """
    # Build in-degree count for each number
    in_degree = defaultdict(int)
    nums = set(nums)  # Convert to set to handle duplicates

    # Count incoming edges for each number
    for num in nums:
        for next_num in rule_mp[num]:
            if next_num in nums:
                in_degree[next_num] += 1

    # Find all numbers with no incoming edges
    queue = deque([num for num in nums if in_degree[num] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        # Remove this number's edges and update in_degrees
        for next_num in rule_mp[current]:
            if next_num in nums:
                in_degree[next_num] -= 1
                if in_degree[next_num] == 0:
                    queue.append(next_num)

    return result


with open("input.txt") as f:
    rules, updates = f.read().split("\n\n")
    # Build rule map as before
    rule_mp = defaultdict(set)
    for rule in rules.splitlines():
        k, v = map(int, rule.split("|"))
        rule_mp[k].add(v)

    # Find out-of-order sequences and fix them
    total = 0
    for update in updates.splitlines():
        pages = [int(v) for v in update.split(",")]
        # Check if sequence is out of order
        for curr, next_val in zip(pages, pages[1:]):
            if next_val not in rule_mp[curr]:
                # Found an out-of-order sequence, sort it
                ordered = topological_sort(pages, rule_mp)
                total += ordered[len(ordered) // 2]
                break

    print(total)
