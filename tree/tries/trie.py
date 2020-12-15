class Trie(object):
    class Node(object):
        def __init__(self, size):
            self.value = None
            self.nodes = [None] * size

    def __init__(self, size):
        self.__size = size
        self.__root = None

    def put(self, key, value):
        self.__root = self.__put(self.__root, key, value, 0)

    def __put(self, x, key, value, d):
        if x is None:
            x = self.Node(self.__size)

        if len(key) == d:
            x.value = value
        else:
            c = self.char_at(key, d)
            x.nodes[c] = self.__put(x.nodes[c], key, value, d + 1)
        return x

    def get(self, key):
        node = self.__get(self.__root, key, 0)
        return node.value if node is not None else None

    def __get(self, x, key, d):
        if x is None:
            return x

        if len(key) == d:
            return x
        else:
            c = self.char_at(key, d)
            return self.__get(x.nodes[c], key, d + 1)

    @property
    def root(self):
        return self.__root

    def contains(self, key):
        return self.get(key) is not None

    def char_at(self, text, pos):
        return ord(text[pos]) % self.__size


def main():
    trie = Trie(26)
    data = {"by": 4, "sea": 6, "sells": 1, "she": 0, "shells": 3, "shore": 7, "the": 5}
    for key in data:
        trie.put(key, data[key])

    for key in data:
        print(key, data[key], trie.get(key))


if __name__ == "__main__":
    main()
