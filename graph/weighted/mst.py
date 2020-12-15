from dequeue.priority_queue import MinPriorityQueue
from dequeue.bag_list import BagList
from graph.weighted.basic import EdgeWeightedGraph
from uf.union_find import UnionFind


class KruskalMST(object):
    def __init__(self, graph):
        self.__edges = BagList()
        min_pq = MinPriorityQueue()
        uf = UnionFind(graph.v())

        for e in graph.edges():
            min_pq.push(e)

        while not min_pq.is_empty() and len(self.__edges) < graph.v() - 1:
            e = min_pq.pop()
            v = e.either()
            w = e.other(v)
            if not uf.connected(v, w):
                uf.union(v, w)
                self.__edges.add(e)

    def edges(self):
        return self.__edges


class PrimLazyMST(object):
    def __init__(self, graph):
        self.__edges = BagList()
        self._in_tree = [False] * graph.v()
        self.__min_pq = MinPriorityQueue()

        self.__visit(graph, 0)

        while not self.__min_pq.is_empty() and len(self.__edges) < graph.v() - 1:
            e = self.__min_pq.pop()
            v = e.either()
            w = e.other(v)
            if self._in_tree[v] and self._in_tree[w]:
                continue
            if not self._in_tree[v]:
                self.__visit(graph, v)
            if not self._in_tree[w]:
                self.__visit(graph, w)
            self.__edges.add(e)

    def __visit(self, graph, v):
        for e in graph.adj(v):
            if not self._in_tree[e.other(v)]:
                self.__min_pq.push(e)
        self._in_tree[v] = True

    def edges(self):
        return self.__edges


def main():
    ewg = EdgeWeightedGraph(open("data/tinyEWG.txt", "r"))

    mst = KruskalMST(ewg)
    for e in mst.edges():
        print(e)

    mst = PrimLazyMST(ewg)
    for e in mst.edges():
        print(e)

if __name__ == "__main__":
    main()
