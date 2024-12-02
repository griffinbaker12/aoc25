def is_safe(nums):
    if len(nums) <= 1:
        return False

    inc = nums[1] - nums[0]
    for i in range(len(nums) - 1):
        diff = nums[i + 1] - nums[i]
        if abs(diff) < 1 or abs(diff) > 3 or (inc * diff) <= 0:
            return False
    return True


with open("input.txt") as f:
    total = 0
    for line in f:
        nums = [int(x) for x in line.split()]

        if is_safe(nums):
            total += 1
            continue

        for i in range(len(nums)):
            test_nums = nums[:i] + nums[i + 1 :]
            if is_safe(test_nums):
                total += 1
                break

    print(total)
