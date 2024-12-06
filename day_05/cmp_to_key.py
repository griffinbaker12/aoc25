from functools import total_ordering

__all__ = [
    'update_wrapper',
    'wraps',
    'WRAPPER_ASSIGNMENTS',
    'WRAPPER_UPDATES',
    'total_ordering',
    'cache',
    'cmp_to_key',
    'lru_cache',
    'reduce',
    'partial',
    'partialmethod',
    'singledispatch',
    'singledispatchmethod',
    'cached_property',
]


def custom_cmp_to_key(mycmp):
    @total_ordering
    class K:
        __slots__ = ['obj']

        def __init__(self, obj):
            self.obj = obj

        def __lt__(self, other):
            print('LT:', self, other)
            c = (r := mycmp(self.obj, other.obj)) < 0
            print('C:', c, 'R:', r)
            return c

        def __eq__(self, other):
            print('EQ:', self, other)
            c = (r := mycmp(self.obj, other.obj)) == 0
            print('C:', c, 'R:', r)
            return c

        def __str__(self):
            return f'{self.obj}'

    return K


def cmp(a, b):
    if a % 2 == 0 and b % 2 != 0:
        return -1
    if a % 2 != 0 and b % 2 == 0:
        return 1
    return a - b


numbers = [5, 2, 8, 1, 9, 4]

# Let's see what the key function actually returns
key_func = custom_cmp_to_key(cmp)
# wrapper_objects = [key_func(n) for n in numbers]
# print("\nWrapper objects created by cmp_to_key:")
# print(wrapper_objects)  # These are K class instances

print('Sorting:', numbers)
# evens first; sorted asc within e/o
print(sorted(numbers, key=key_func))
