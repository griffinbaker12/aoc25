def is_safe(nums):
    inc = nums[1] - nums[0]
    for n1, n2 in zip(nums, nums[1:]):
        diff = n2 - n1
        if abs(diff) < 1 or abs(diff) > 3 or (inc * diff) <= 0:
            return False
    return True


with open("input.txt") as f:
    total = 0
    for line in f:
        nums = [int(x) for x in line.split()]
        if is_safe(nums) or any(
            is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums))
        ):
            total += 1
    print(total)  # 318
