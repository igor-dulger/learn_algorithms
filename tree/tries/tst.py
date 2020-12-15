class TST(object):
    class Node(object):
        def __init__(self, c):
            self.value = None
            self.c = c
            self.left = None
            self.middle = None
            self.right = None

    def __init__(self):
        self.__root = None

    def put(self, key, value):
        self.__root = self.__put(self.__root, key, value, 0)

    def __put(self, x, key, value, d):
        c = self.__char_at(key, d)
        if x is None:
            x = self.Node(c)

        if c < x.c:
            x.left = self.__put(x.left, key, value, d)
        elif c > x.c:
            x.right = self.__put(x.right, key, value, d)
        elif d < len(key) - 1:
            x.middle = self.__put(x.middle, key, value, d + 1)
        else:
            x.value = value

        return x

    def get(self, key):
        x = self.__get(self.__root, key, 0)
        return x.value if x is not None else None

    def __get(self, x, key, d):
        if x is None:
            return None

        c = self.__char_at(key, d)

        if c < x.c:
            return self.__get(x.left, key, d)
        elif c > x.c:
            return self.__get(x.right, key, d)
        elif d < len(key) - 1:
            return self.__get(x.middle, key, d + 1)
        else:
            return x

    def contains(self, key):
        return self.get(key) is not None

    def delete(self, key):
        x = self.__get(self.__root, key, 0)
        x.value = None

    def keys(self):
        result = []
        self.__collect(self.__root, "", result)
        return result

    def __collect(self, node, prefix, result):
        if node is None:
            return

        if node.value is not None:
            result.append(prefix + node.c)

        self.__collect(node.left, prefix, result)
        self.__collect(node.middle, prefix+node.c, result)
        self.__collect(node.right, prefix, result)

    def keys_with_prefix(self, prefix):
        result = []
        self.__collect(self.__get(self.__root, prefix, 0), prefix[:-1], result)
        return result

    def longest_prefix_of(self, target):
        pos = self.__get_prefix_pos(self.__root, target, 0, 0)
        return target[:pos+1]

    def __get_prefix_pos(self, x, key, d, length):
        if x is None:
            return length

        if len(key) == d:
            return d

        c = self.__char_at(key, d)

        if c < x.c:
            return self.__get_prefix_pos(x.left, key, d, length)
        elif c > x.c:
            return self.__get_prefix_pos(x.right, key, d, length)
        else:
            if x.value is not None:
                length = d
            if d < len(key) - 1:
                return self.__get_prefix_pos(x.middle, key, d + 1, length)
            else:
                return length

    @staticmethod
    def __char_at(s, d):
        return s[d] if d < len(s) else -1
