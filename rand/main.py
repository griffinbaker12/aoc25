class MyMap:
    def __init__(self, data, fn):
        self.data = data
        self.fn = fn

    def __iter__(self):
        for x in self.data:
            yield self.fn(x)


mm = MyMap([1, 2, 3], lambda x: x * 2)
for x in mm:
    print(x)


def my_map(data, fn):
    for x in data:
        yield fn(x)


print(list(my_map([1, 2, 3], lambda x: x * 2)))
