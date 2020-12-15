import math
from dequeue.deque import Deque


class NegativeCircle(object):
    def __init__(self, graph):
        self. _from = [None] * graph.v()
        self. _dist_to = [math.inf] * graph.v()
        self.__circle = None

        self. _dist_to[0] = 0
        for i in range(graph.v()):
            self.__iteration = i
            for v in range(graph.v()):
                for e in graph.adj(v):
                    self.__relax(e)
                    if self.__circle is not None:
                        break
                if self.__circle is not None:
                    break
            if self.__circle is not None:
                break

    def __relax(self, e):
        v = e.from_v()
        w = e.to_v()
        if self.dist_to(w) > self.dist_to(v) + e.weight():
            self. _from[w] = e
            self. _dist_to[w] = self. _dist_to[v] + e.weight()
            if w == self.__iteration:
                self.__circle = w

    def dist_to(self, v):
        return self._dist_to[v]

    def has_negative_circle(self):
        return self.__circle is not None

    def negative_circle(self):
        result = Deque()
        t = self._from[self.__circle]
        while t.from_v() != self.__circle:
            result.add_first(t)
            t = self._from[t.from_v()]
        result.add_first(t)
        return result

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        from_list = [str(i) + " => " + str(v) for i, v in enumerate(self._from)]
        return "From: {}\nCircle: {}".format(", ".join(from_list), self.__circle)
