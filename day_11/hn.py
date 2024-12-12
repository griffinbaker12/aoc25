from functools import cache

stones = [int(x) for x in open("input.txt").read().split()]


@cache
def count(stone, steps):
    if steps == 0:
        return 1
    if stone == 0:
        return count(1, steps - 1)
    string = str(stone)
    length = len(string)
    if length % 2 == 0:
        return count(int(string[: length // 2]), steps - 1) + count(
            int(string[length // 2 :]), steps - 1
        )
    return count(stone * 2024, steps - 1)


# You don't need to keep track of the entire list
# You just need to be able to know how many stones a given stone
# will turn into
print(sum(count(stone, 75) for stone in stones))
