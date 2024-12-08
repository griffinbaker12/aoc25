def max_burgers(m, n, t):
    def eat_burgers(time_left, eaten):
        if time_left == 0:
            return eaten
        if time_left < 0:
            return float("-inf")
        eat_m = eat_burgers(time_left - m, eaten + 1)
        eat_n = eat_burgers(time_left - n, eaten + 1)

        return max(eat_m, eat_n)

    return eat_burgers(t, 0)


with open("homer.txt") as f:
    for line in f:
        m, n, t = [int(x) for x in line.split()]
        print(max_burgers(m, n, t))
