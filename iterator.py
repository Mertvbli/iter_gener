nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


class MyIterator:

    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.a = []
        for item in nested_list:
            for sublist in item:
                self.a.append(sublist)
        self.count = -1
        return self

    def __next__(self):
        self.count += 1
        if self.count == len(self.a):
            raise StopIteration
        return self.a[self.count]


FlatIterator = MyIterator(nested_list)
if __name__ == '__main__':
    for item in FlatIterator:
        print(item)
