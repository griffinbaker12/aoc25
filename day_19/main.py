def valid_pattern(design, patterns):
    n = len(design)
    # dp[i] represents whether it's possible to match design[i:] using the patterns
    dp = [False] * (n + 1)
    dp[n] = True  # Empty string is always valid

    # Work backwards from the end of the string
    for i in range(n - 1, -1, -1):
        # Try each pattern at current position
        for pattern in patterns:
            if (
                i + len(pattern) <= n  # Pattern fits
                and design[i : i + len(pattern)] == pattern  # Pattern matches
                and dp[i + len(pattern)]
            ):  # Rest of string is valid
                dp[i] = True
                break

    return dp[0]


# Parse input
top, bottom = open(0).read().split("\n\n")
patterns = [p.strip() for p in top.split(",")]
designs = [d.strip() for d in bottom.splitlines()]

# Create pattern set for O(1) lookups
patterns = set(patterns)  # Convert to set for faster lookups

# Count valid designs
total = sum(1 for design in designs if valid_pattern(design, patterns))
print(total)
