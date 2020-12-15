from dequeue.bag_list import BagList
import io


class Edge(object):
    def __init__(self, v, w, weight):
        self.__v = v
        self.__w = w
        self.__weight = weight

    def either(self):
        return self.__v

    def other(self, v):
        return self.__v if v == self.__w else self.__w

    def weight(self):
        return self.__weight

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __le__(self, other):
        return self.weight() <= other.weight()

    def __eq__(self, other):
        return other.weight() == self.weight()

    def __ne__(self, other):
        return other.weight() != self.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __ge__(self, other):
        return self.weight() >= other.weight()

    def __repr__(self):
        return "V: {}\nW: {}\nWeight: {}".format(self.__v, self.__w, self.__weight)

    def __str__(self):
        return "{}->{}({})".format(self.__v, self.__w, self.__weight)


class DirectedEdge(object):
    def __init__(self, v, w, weight):
        self.__from = v
        self.__to = w
        self.__weight = weight

    def from_v(self):
        return self.__from

    def to_v(self):
        return self.__to

    def weight(self):
        return self.__weight

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __le__(self, other):
        return self.weight() <= other.weight()

    def __eq__(self, other):
        return other.weight() == self.weight()

    def __ne__(self, other):
        return other.weight() != self.weight()

    def __gt__(self, other):
        return self.weight() > other.weight()

    def __ge__(self, other):
        return self.weight() >= other.weight()

    def __repr__(self):
        return "From: {}\nTo: {}\nWeight: {}".format(self.__from, self.__to, self.__weight)

    def __str__(self):
        return "{}->{}({})".format(self.__from, self.__to, self.__weight)


class EdgeWeightedGraph(object):
    def __init__(self, v):
        if isinstance(v, io.IOBase):
            self.__load_from_file(v)
        else:
            self.__start(v)

    def __load_from_file(self, file):
        params = []
        for line in [i.strip() for i in file]:
            if line:
                params.append(int(line))
            if len(params) == 2:
                break
        self.__start(params[0])

        file.seek(0)

        for line in [i.strip().split() for i in file]:
            if len(line) == 3:
                self.add_edge(Edge(int(line[0]), int(line[1]), line[2]))
        file.close()

    def __start(self, v):
        self.__v = v
        self.__vertices = [BagList() for x in range(self.__v)]
        self.__edges = BagList()

    def v(self):
        return self.__v

    def e(self):
        return len(self.__edges)

    def add_edge(self, e):
        self.__validate_edge(e)
        self.__vertices[e.either()].add(e)
        self.__vertices[e.other(e.either())].add(e)
        self.__edges.add(e)

    def adj(self, v):
        return self.__vertices[v]

    def edges(self):
        return self.__edges

    def __validate_edge(self, e):
        if e.either() < 0 or e.either() > self.__v:
            raise ValueError("vertex " + str(e.either()) + " is not between 0 and " + str(self.__v-1))

        if e.other(e.either()) < 0 or e.other(e.either()) < 0:
            raise ValueError("vertex " + str(e.other(e.either())) + " is not between 0 and " + str(self.__v-1))

    def __str__(self):
        if self.__v == 0:
            return "Empty graph"

        result_list = []
        for v, bag in enumerate(self.__vertices):
            result_list.append(str(v) + "=>(" + (str(bag) if bag.size() else "") + ")")

        return ", ".join(result_list)

    def __repr__(self):
        if self.__v == 0:
            return "\nEmpty list"

        result_list = []
        for v, bag in enumerate(self.__vertices):
            result_list.append(str(v) + "=>(" + str(bag) + ")")

        return "\nSize: {}\nVertices:\n{}\nEdges:\n{}".format(self.__v, "\n".join(result_list), self.__edges)


class EdgeWeightedDigraph(object):
    def __init__(self, v):
        if isinstance(v, io.IOBase):
            self.__load_from_file(v)
        else:
            self.__start(v)

    def __load_from_file(self, file):
        params = []
        for line in [i.strip() for i in file]:
            if line:
                params.append(int(line))
            if len(params) == 2:
                break
        self.__start(params[0])

        file.seek(0)

        for line in [i.strip().split() for i in file]:
            if len(line) == 3:
                self.add_edge(DirectedEdge(int(line[0]), int(line[1]), float(line[2])))
        file.close()

    def __start(self, v):
        self.__v = v
        self.__vertices = [BagList() for x in range(self.__v)]
        self.__edges = BagList()

    def v(self):
        return self.__v

    def e(self):
        return len(self.__edges)

    def add_edge(self, e):
        self.__validate_edge(e)
        self.__vertices[e.from_v()].add(e)
        self.__edges.add(e)

    def adj(self, v):
        return self.__vertices[v]

    def edges(self):
        return self.__edges

    def __validate_edge(self, e):
        if e.from_v() < 0 or e.from_v() > self.__v:
            raise ValueError("vertex " + str(e.from_v()) + " is not between 0 and " + str(self.__v-1))

        if e.to_v() < 0 or e.to_v() < 0:
            raise ValueError("vertex " + str(e.to_v()) + " is not between 0 and " + str(self.__v-1))

    def __str__(self):
        if self.__v == 0:
            return "Empty graph"

        result_list = []
        for v, bag in enumerate(self.__vertices):
            result_list.append(str(v) + "=>(" + (str(bag) if bag.size() else "") + ")")

        return ", ".join(result_list)

    def __repr__(self):
        if self.__v == 0:
            return "\nEmpty list"

        result_list = []
        for v, bag in enumerate(self.__vertices):
            result_list.append(str(v) + "=>(" + str(bag) + ")")

        return "\nSize: {}\nVertices:\n{}\nEdges:\n{}".format(self.__v, "\n".join(result_list), self.__edges)


def main():
    d = Edge(4, 5, 1)
    d1 = Edge(5, 7, 0.5)
    d2 = Edge(5, 7, 1.5)
    print("Either", d.either())
    print("Other 4 =>", d.other(4))
    print("Other 5 =>", d.other(5))
    print(d.weight())
    print(d > d1, d < d2, d == d)
    print(repr(d))
    print("Print", d)

    d = EdgeWeightedGraph(4)
    d.add_edge(0, 1, 1)
    d.add_edge(0, 2, 2)
    d.add_edge(2, 3, 3)
    d.add_edge(2, 0, 4)
    d.add_edge(2, 1, 5)
    print(repr(d))

    print("V:", d.v())
    print("E:", d.e())
    print("reverse:", d.reverse())

    for v in range(d.v()):
        for i in d.adj(v):
            print("{} -> {}".format(v, i))

    # d = EdgeWeightedGraph(open("data/word_net/digraph25.txt", "r"))
    # print(repr(d))
    #
    # print("V:", d.v())
    # print("E:", d.e())
    # print("indegree 0:", d.indegree(0))
    # print("outdegree 0:", d.outdegree(0))
    # print("reverse:", d.reverse())
    #
    # for v in range(d.v()):
    #     for i in d.adj(v):
    #         print("{} -> {}".format(v, i))


if __name__ == "__main__":
    main()
