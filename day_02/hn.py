def is_safe(nums):
    diffs = [x - y for x, y in zip(nums, nums[1:])]
    return all(1 <= x <= 3 for x in diffs) or all(-1 >= x >= -3 for x in diffs)


total = 0
for report in open("input.txt"):
    nums = list(map(int, report.split()))
    if is_safe(nums) or any(
        is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums))
    ):
        total += 1
print(total)

# with open("input.txt") as f:

#     total = 0
#     for line in f:
#         nums = [int(x) for x in line.split()]
#         if is_safe(nums):
#             # or any(
#             # is_safe(nums[:i] + nums[i + 1 :]) for i in range(len(nums))
#             # ):
#             total += 1
#     print(total)  # 318
