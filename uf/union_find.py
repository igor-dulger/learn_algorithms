class UnionFind(object):
    def __init__(self, n):
        self.__list = list(range(n))
        self.__count = n
        self.__sizes = [1 for i in range(n)]

    def find(self, i):
        while self.__list[i] != i:
            self.__list[i] = self.__list[self.__list[i]]
            i = self.__list[i]
        return i

    def union(self, p, q):
        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return False
        else:
            self.__count -= 1
            if self.__sizes[p_root] > self.__sizes[q_root]:
                self.__list[q_root] = p_root
                self.__sizes[p_root] += self.__sizes[q_root]
            else:
                self.__list[p_root] = q_root
                self.__sizes[q_root] += self.__sizes[p_root]
            return True

    @property
    def count(self):
        return self.__count

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def __str__(self):
        # list_dict = {}
        # for i, val in enumerate(self.__list):
        #     if val in list_dict:
        #         list_dict[val].append(i)
        #     else:
        #         list_dict[val] = []
        # print(list_dict)
        return """ 
Count: {}
List: {} 
Sizes: {}             
"""\
        .format(
            str(self.count),
            ", ".join(["{}:{}".format(i, value) for i, value in enumerate(self.__list)]),
            ", ".join(["{}:{}".format(i, value) for i, value in enumerate(self.__sizes)])
        )


def main():

    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    fd = open("data/tinyUF.txt", "r")
    num = int(fd.readline())

    uf = WeightedQuickUnionUF(num)
    for line in fd:
        p, q = [int(chunk) for chunk in line.split(' ')]
        uf.union(p, q)

    test("Check 8 9", uf.connected(8, 9), True)
    test("Check 4 9", uf.connected(4, 9), True)
    test("Check 3 9", uf.connected(3, 9), True)
    test("Check 4 3", uf.connected(4, 3), True)
    test("Check 0 7", uf.connected(0, 7), True)
    test("Check 6 2", uf.connected(6, 2), True)
    test("Check 7 9", uf.connected(7, 9), False)
    test("Check 7 8", uf.connected(7, 8), False)
    test("Check 0 9", uf.connected(0, 9), False)


if __name__ == "__main__":
    main()