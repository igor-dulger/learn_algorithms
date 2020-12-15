from dequeue.deque import Deque


class TopologicalOrder(object):
    def __init__(self, graph):
        self.__marked = [False for x in range(graph.v())]
        self.__order = Deque()

        for v in range(graph.v()):
            if not self.__marked[v]:
                self.__dfp(graph, v)

    def __dfp(self, graph, v):
        self.__marked[v] = True
        for i in graph.adj(v):
            if not self.__marked[i]:
                self.__dfp(graph, i)
        self.__order.add_first(v)

    def order(self, v):
        return self.__order

    def __repr__(self):
        return "\nOrder: {}".format("->".join([str(i) for i in self.__order]))