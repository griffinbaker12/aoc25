from functools import lru_cache

stones = open("test.txt").read().split()
print(stones)

blinks = 75


@lru_cache(maxsize=None)
def transform_stone(stone):
    stone_to_int = int(stone)

    if stone_to_int == 0:
        return "1"
    elif len(stone) % 2 == 0:
        mid = len(stone) // 2
        left, right = stone[:mid], stone[mid:]
        right_transformed = "0" if right.lstrip("0") == "" else right.lstrip("0")
        return left, right_transformed
    else:
        return str(stone_to_int * 2024)


for _ in range(blinks):
    i = 0
    while i < len(stones):
        transformed_stone = transform_stone(stones[i])
        if isinstance(transformed_stone, str):
            stones[i] = transformed_stone
        else:
            mid = len(stones[i]) // 2
            stones = stones[: i + 1] + [transformed_stone[1]] + stones[i + 1 :]
            i += 1
        i += 1

print(len(stones))
