from graph.basic import Graph


class Connections(object):
    def __init__(self, graph):
        self.__marked = [False for x in range(graph.v())]
        self.__ids = [None for x in range(graph.v())]
        self.__count = 0

        for i in range(graph.v()):
            if not self.__marked[i]:
                self.__dfp(graph, i)
                self.__count += 1

    def __dfp(self, graph, v):
        self.__marked[v] = True
        self.__ids[v] = self.__count

        for i in graph.adj(v):
            if not self.__marked[i]:
                self.__dfp(graph, i)

    def count(self):
        return self.__count

    def id(self, v):
        return self.__ids[v]

    def __repr__(self):
        market_list = [str(i) + " => " + str(v) for i, v in enumerate(self.__marked)]
        ids_list = [str(i) + " => " + str(v) for i, v in enumerate(self.__ids)]
        return "\nCount: {}\nMarked: {}\nConnections: {}".format(self.__count, ", ".join(market_list), ", ".join(ids_list))


def main():
    d = Graph(13)
    d.add_edge(0, 5)
    d.add_edge(2, 4)
    d.add_edge(2, 3)
    d.add_edge(1, 2)
    d.add_edge(0, 1)
    d.add_edge(3, 4)
    d.add_edge(3, 5)
    d.add_edge(0, 2)
    d.add_edge(11, 12)
    d.add_edge(9, 10)
    d.add_edge(0, 6)
    d.add_edge(7, 8)
    d.add_edge(9, 11)
    d.add_edge(5, 3)

    print(repr(d))

    dfp = CC(d)
    print(repr(dfp))
    print("count {}".format(dfp.count()))
    print("Id for {} is {}".format(5, dfp.id(5)))

if __name__ == "__main__":
    main()
