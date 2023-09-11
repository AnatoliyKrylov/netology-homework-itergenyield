class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        print("Вошли в цикл")
        self.index_list = 0
        self.index_el = 0
        return self

    def __next__(self):
        if self.index_el >= len(self.list_of_list[self.index_list]):
            self.index_list += 1
            self.index_el = 0
        if self.index_list >= len(self.list_of_list):
            raise StopIteration
        item = self.list_of_list[self.index_list][self.index_el]
        self.index_el += 1
        return item


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()
