from graph.weighted.flow.basic import FlowNetwork
import math
from dequeue.deque import Deque


class FordFulkerson(object):
    def __init__(self, graph, s, t):
        self.__marked = None
        self.__edge_to = None
        self.__flow = 0

        while self.__has_augmenting_path(graph, s, t):
            v = t
            bottle = math.inf
            while self.__edge_to[v] is not None:
                bottle = min(bottle, self.__edge_to[v].residual_capacity_to(v))
                v = self.__edge_to[v].other(v)

            v = t
            while self.__edge_to[v] is not None:
                self.__edge_to[v].add_residual_flow_to(v, bottle)
                v = self.__edge_to[v].other(v)

            self.__flow += bottle

    def flow(self):
        return self.__flow

    def in_cut(self, v):
        return self.__marked[v]

    def __has_augmenting_path(self, graph, s, t):
        self.__marked = [False]*graph.v()
        self.__edge_to = [None]*graph.v()
        queue = Deque()
        queue.add_last(s)
        self.__marked[s] = True
        while not queue.is_empty():
            v = queue.remove_first()
            for e in graph.adj(v):
                w = e.other(v)
                if not self.__marked[w] and e.residual_capacity_to(w) > 0:
                    queue.add_last(w)
                    self.__marked[w] = True
                    self.__edge_to[w] = e

        return self.__marked[t]

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "Marked: {}\nEdgeTo:{}\nFlow:{}\n".format(
            self.__marked,
            self.__edge_to,
            self.__flow
        )
