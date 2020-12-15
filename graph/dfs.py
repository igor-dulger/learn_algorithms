from graph.graph import Graph
from dequeue.deque import Deque


class DFS(object):
    def __init__(self, graph, s):
        self.__marked = [False for x in range(graph.v())]
        self.__edge_to = [None for x in range(graph.v())]
        self.__s = s
        self.__dfp(graph, s)

    def __dfp(self, graph, v):
        self.__marked[v] = True
        for i in graph.adj(v):
            if not self.__marked[i]:
                self.__dfp(graph, i)
                self.__edge_to[i] = v

    def has_path_to(self, v):
        return self.__marked[v]

    def path_to(self, v):
        result = Deque()

        if not self.has_path_to(v):
            return []

        result.add_first(v)

        while self.__edge_to[v] is not None:
            result.add_first(self.__edge_to[v])
            v = self.__edge_to[v]

        return result

    def __repr__(self):
        market_list = [str(i) + " => " + str(v) for i, v in enumerate(self.__marked)]
        edge_to_list = [str(i) + " => " + str(v) for i, v in enumerate(self.__edge_to)]
        return "\nStart: {}\nMarked: {}\nFrom: {}".format(self.__s, ", ".join(market_list), ", ".join(edge_to_list))


def main():
    d = Graph(6)
    d.add_edge(0, 1)
    d.add_edge(0, 2)
    d.add_edge(1, 3)
    d.add_edge(2, 1)
    d.add_edge(4, 5)

    print(repr(d))

    dfp = DFS(d, 0)
    print(repr(dfp))
    print("Has path to {} {}".format(2, dfp.has_path_to(2)))
    print("Has path to {} {}".format(5, dfp.has_path_to(5)))

    for i in dfp.path_to(5):
        print(i)

if __name__ == "__main__":
    main()
