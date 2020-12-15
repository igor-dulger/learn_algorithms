class BagArray(object):

    def __init__(self):
        self.__size = 0
        self.__list = [None]
        self.__current = 0

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__size

    def __double(self):
        self.__list = self.__list + [None]*len(self.__list)

    def add(self, item):
        if item is None:
            raise ValueError("Can't add None value")
        if len(self.__list) == self.size():
            self.__double()
        self.__list[self.size()] = item
        self.__size += 1

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        if self.__current == self.size():
            raise StopIteration
        else:
            self.__current += 1
            return self.__list[self.__current-1]

    def __str__(self):
        if self.is_empty():
            return "Empty list"
        return ",".join(self.__list[:self.size()])

    def __repr__(self):
        result = []
        for i in self.__list:
            if i is None:
                result.append('None')
            else:
                result.append(i)

        return "{}\n{}\nSize: {}\nList: {}\n".format(self.__class__.__name__, '-'*20, self.__size, ",".join(result))


def main():
    d = Bag()
    # print(repr(d))
    d.add('q')
    d.add('w')
    d.add('e')
    d.add('r')
    d.add('t')
    # print(repr(d))
    # print(d)

    for i in d:
        print(i)

    print(repr(d))


if __name__ == "__main__":
    main()
