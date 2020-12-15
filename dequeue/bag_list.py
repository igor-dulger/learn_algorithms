class BagList(object):

    class Node:
        def __init__(self, val, next_node=None):
            self.val = val
            self.next = next_node

        def __str__(self):
            return str(self.val)

    def __init__(self):
        self.__first = self.Node(None)
        self.__last = self.__first

        self.__size = 0
        self.__current = None

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__size

    def add(self, item):
        self.__last.next = self.Node(item)
        self.__last = self.__last.next
        self.__size += 1

    def __iter__(self):
        self.__current = self.__first.next
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        else:
            temp = self.__current
            self.__current = self.__current.next
            return temp.val

    def __str__(self):
        if self.__size == 0:
            return "Empty list"

        result_list = []
        for item in self:
            result_list.append(str(item))

        return ", ".join(result_list)

    def __len__(self):
        return self.__size

    def __repr__(self):
        if self.__size == 0:
            return "\nEmpty list"

        current = self.__first
        result_list = []
        while True:
            result_list.append(str(current))
            if current.next is None:
                break
            else:
                current = current.next
        return "\nSize: {}\nList: {}\nFirst: {}\nLast: {}".format(self.__size, ", ".join(result_list), self.__first, self.__last)


def main():
    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    d = BagList()
    print(d)

    d.add('2')
    d.add('3')
    d.add('5')
    d.add('7')
    print(repr(d))

    print(d)

    for i in d:
        print(i)

if __name__ == "__main__":
    main()
