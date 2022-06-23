nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


def flat_generator(data):
    for item in nested_list:
        for sublist in item:
            yield sublist


if __name__ == '__main__':
    for item in flat_generator(nested_list):
        print(item)
