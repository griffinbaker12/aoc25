def concat_nums(a, b):
    return int(str(a) + str(b))


def solve(target, numbers):
    def try_operations(curr, rem):
        if not rem:
            return curr == target

        next_num, rest = rem[0], rem[1:]

        if try_operations(curr + next_num, rest):
            return True

        if try_operations(curr * next_num, rest):
            return True

        if try_operations(concat_nums(curr, next_num), rest):
            return True

        return False

    return try_operations(numbers[0], numbers[1:])


total = 0
with open("input.txt") as f:
    eqs = []
    for line in f.readlines():
        left, right = line.split(":")
        target = int(left)
        arr = [int(x) for x in right.split()]
        if solve(target, arr):
            total += target


print(total)
