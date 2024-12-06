# demonstrates key getting called for each value in array
from random import shuffle


def my_key(x):
    print(f"My key called with: {x}")
    return 0


a = [v for v in range(5)]
print(a)
shuffle(a)
print(sorted(a, key=my_key))  # won't sort at all
