from dequeue.bag_list import BagList
import io


class Graph(object):
    def __init__(self, v):
        self.__v = v
        self.__e = 0
        self.__vertices = [BagList() for x in range(self.__v)]

    def v(self):
        return self.__v

    def e(self):
        return self.__e

    def add_edge(self, v, w):
        self.__vertices[v].add(w)
        self.__vertices[w].add(v)
        self.__e += 1

    def adj(self, v):
        return self.__vertices[v]

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
        return "\nSize: {}\nVertices: {}".format(self.__v, ", ".join(result_list))


class Digraph(object):
    def __init__(self, v):
        if isinstance(v, io.IOBase):
            self.__load_from_file(v)
        else:
            self.__start(v, 0)

    def __load_from_file(self, file):
        params = []
        for line in [i.strip() for i in file]:
            if line:
                params.append(int(line))
            if len(params) == 2:
                break
        self.__start(params[0], params[1])

        file.seek(0)

        for line in [i.strip().split() for i in file]:
            if len(line) == 2:
                self.add_edge(int(line[0]), int(line[1]))
        file.close()

    def __start(self, v, e):
        self.__v = v
        self.__e = e
        self.__indegree = [0] * self.__v
        self.__vertices = [BagList() for x in range(self.__v)]

    def v(self):
        return self.__v

    def e(self):
        return self.__e

    def add_edge(self, v, w):
        self.__validate_vertex(v)
        self.__validate_vertex(w)
        self.__vertices[v].add(w)
        self.__indegree[w] += 1
        self.__e += 1

    def outdegree(self, v):
        self.__validate_vertex(v)
        return len(self.adj(v))

    def indegree(self, v):
        self.__validate_vertex(v)
        return self.__indegree[v]

    def reverse(self):
        reverse = Digraph(self.__v)
        for v in range(self.__v):
            for w in self.adj(v):
                reverse.add_edge(w, v)
        return reverse

    def adj(self, v):
        return self.__vertices[v]

    def __validate_vertex(self, v):
        if v < 0 or v >= self.__v:
            raise ValueError("vertex " + str(v) + " is not between 0 and " + str(self.__v-1))

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
        return "\nSize: {}\nVertices: {}".format(self.__v, ", ".join(result_list))


def main():
    d = Graph(4)
    print(d)

    d.add_edge(0, 1)
    d.add_edge(0, 2)
    d.add_edge(2, 3)
    d.add_edge(2, 1)
    print(repr(d))

    print(d)

    for i in d.adj(0):
        print(i)


if __name__ == "__main__":
    main()
