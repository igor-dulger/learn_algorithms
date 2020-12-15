from graph.basic import Digraph


class Cyclic(object):
    def __init__(self, graph):
        self.__graph = graph
        self.__visited = [False] * self.__graph.v()
        self.__out = [False] * self.__graph.v()
        self.__is_cyclic = self.__has_cycles()

    def __has_cycles(self):
        for v in range(self.__graph.v()):
            # print(v, self.__visited, self.__out)
            if not self.__visited[v]:
                if self.__dfs_until_cycle(v):
                    return True
        return False

    def __dfs_until_cycle(self, v):
        self.__visited[v] = True
        for i in self.__graph.adj(v):
            if not self.__visited[i]:
                if self.__dfs_until_cycle(i):
                    return True
            else:
                if not self.__out[i]:
                    return True
        self.__out[v] = True
        return False

    def is_cyclic(self):
        return self.__is_cyclic

    def __str__(self):
        return str(self.__graph)

    def __repr__(self):
        result_list = []
        for v in range(self.__graph.v()):
            bag = [i for i in self.__graph.adj(v)]
            result_list.append(str(v) + "=>(" + str(bag) + ")")
        return "Cyclic\nIs cyclic: {}\nGraph:{}".format(self.__is_cyclic, repr(self.__graph))


def main():

    g = Digraph(3)
    fd = open("../data/word_net/hypernyms3InvalidTwoRoots.txt", "r")
    for line in [i.strip().split(sep=",") for i in fd]:
        if line:
            for w in line[1:]:
                g.add_edge(int(line[0]), int(w))
    fd.close()

    rdag = Cyclic(g)
    print(repr(rdag))
    print("Is cyclic: ", rdag.is_cyclic())


if __name__ == "__main__":
    main()
