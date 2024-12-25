# a = list(zip(*[map(int, line.split()) for line in open(0).read().splitlines()]))


# nums = [list(map(int, line.split())) for line in open(0).read().splitlines()]
# print(nums)
#
# zns = zip(*nums)
# print(list(zns))

nums_no_list = [map(int, line.split()) for line in open(0).read().splitlines()]
print(*nums_no_list)

zns = zip(*nums_no_list)
print(list(zns))
