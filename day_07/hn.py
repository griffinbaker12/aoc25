total = 0


def can_obtain(target, arr):
    if len(arr) == 1:
        return target == arr[0]
    if target % arr[-1] == 0 and can_obtain(target / arr[-1], arr[:-1]):
        return True
    if target > arr[-1] and can_obtain(target - arr[-1], arr[:-1]):
        return True
    target_str = str(target)
    last_str = str(arr[-1])
    # Check if target ends with our last number
    if target_str.endswith(last_str) and can_obtain(
        int(target_str[: -len(last_str)]), arr[:-1]
    ):
        return True
    return False


with open("test.txt") as f:
    eqs = []
    for line in f.readlines():
        left, right = line.split(":")
        target = int(left)
        arr = [int(x) for x in right.split()]
        if can_obtain(target, arr):
            total += target
print(total)
