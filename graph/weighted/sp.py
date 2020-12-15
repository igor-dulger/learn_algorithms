from graph.weighted.basic import EdgeWeightedDigraph
from dequeue.priority_queue import MinIndexPriorityQueue
from dequeue.deque import Deque
import math


class SP(object):
    def __init__(self, graph):
        pass

    def __relax(self, e):
        pass

    def dist_to(self, v):
        return self._dist_to[v]

    def has_path_to(self, v):
        return self._from[v] is not None

    def path_to(self, v):
        path = Deque()
        while self._from[v] is not None:
            path.add_first(self._from[v])
            v = self._from[v].from_v()
        return path

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        from_list = [str(i) + " => " + str(v) for i, v in enumerate(self._from)]
        dist_to_list = [str(i) + " => " + str(v) for i, v in enumerate(self._dist_to)]
        return "\nStart: {}\nFrom: {}\nDist: {}".format(self.__s, ", ".join(from_list), ", ".join(dist_to_list))


class DijkstraSP(SP):
    def __init__(self, graph, s):
        self._from = [None] * graph.v()
        self._dist_to = [math.inf] * graph.v()
        self.__pq = MinIndexPriorityQueue()

        self. _dist_to[s] = 0
        self.__pq.push(s, self. _dist_to[s])

        while not self.__pq.is_empty():
            v = self.__pq.pop()
            for e in graph.adj(v):
                self.__relax(e)

    def __relax(self, e):
        v = e.from_v()
        w = e.to_v()
        if self.dist_to(w) > self.dist_to(v) + e.weight():
            self. _from[w] = e
            self. _dist_to[w] = self. _dist_to[v] + e.weight()
            if w in self.__pq:
                self.__pq.decrease_key(w, self. _dist_to[w])
            else:
                self.__pq.push(w, self. _dist_to[w])


class DijkstraMonoSP(SP):
    def __init__(self, graph, s):
        self._from = [None] * graph.v()
        self._dist_to = [math.inf] * graph.v()
        self.__pq = MinIndexPriorityQueue()

        self. _dist_to[s] = 0
        self.__pq.push(s, self. _dist_to[s])

        while not self.__pq.is_empty():
            v = self.__pq.pop()
            for e in graph.adj(v):
                self.__relax(e)

    def __relax(self, e):
        v = e.from_v()
        w = e.to_v()
        prev_weight = self._from[v].weight() if self._from[v] is not None else 0
        if e.weight() > prev_weight and self.dist_to(w) > self.dist_to(v) + e.weight():
            self. _from[w] = e
            self. _dist_to[w] = self. _dist_to[v] + e.weight()
            if w in self.__pq:
                self.__pq.decrease_key(w, self. _dist_to[w])
            else:
                self.__pq.push(w, self. _dist_to[w])


class BellmanFordSP(SP):
    def __init__(self, graph, s):
        self. _from = [None] * graph.v()
        self. _dist_to = [math.inf] * graph.v()

        self. _dist_to[s] = 0
        for i in range(graph.v()):
            for v in range(graph.v()):
                for e in graph.adj(v):
                    self.__relax(e)

    def __relax(self, e):
        v = e.from_v()
        w = e.to_v()
        if self.dist_to(w) > self.dist_to(v) + e.weight():
            self. _from[w] = e
            self. _dist_to[w] = self. _dist_to[v] + e.weight()
