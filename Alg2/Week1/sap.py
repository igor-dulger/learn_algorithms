from graph.digraph import Digraph
from graph.bfs import Bfs
import math


# public class SAP {
#
#    // constructor takes a digraph (not necessarily a DAG)
#    public SAP(Digraph G)
#
#    // length of shortest ancestral path between v and w; -1 if no such path
#    public int length(int v, int w)
#
#    // a common ancestor of v and w that participates in a shortest ancestral path; -1 if no such path
#    public int ancestor(int v, int w)
#
#    // length of shortest ancestral path between any vertex in v and any vertex in w; -1 if no such path
#    public int length(Iterable<Integer> v, Iterable<Integer> w)
#
#    // a common ancestor that participates in shortest ancestral path; -1 if no such path
#    public int ancestor(Iterable<Integer> v, Iterable<Integer> w)
#
#    // do unit testing of this class
#    public static void main(String[] args)
# }

class Sap(object):
    def __init__(self, graph):
        self.__graph = graph

    def length(self, v, w):
        g1 = Bfs(self.__graph, v)
        g2 = Bfs(self.__graph, w)
        length = math.inf
        for i in range(self.__graph.v()):
            if g1.has_path_to(i) and g2.has_path_to(i):
                temp = len(g1.path_to(i)) - 1 + len(g2.path_to(i)) - 1
                if length > temp:
                    length = temp
        return length if length < math.inf else -1

    def ancestor(self, v, w):
        g1 = Bfs(self.__graph, v)
        g2 = Bfs(self.__graph, w)
        result = None
        length = math.inf
        for i in range(self.__graph.v()):
            if g1.has_path_to(i) and g2.has_path_to(i):
                temp = len(g1.path_to(i)) + len(g2.path_to(i))
                if length > temp:
                    length = temp
                    result = i
        return result if length < math.inf else -1

    def __str__(self):
        return str(self.__graph)

    def __repr__(self):
        result_list = []
        for v in range(self.__graph.v()):
            bag = [i for i in self.__graph.adj(v)]
            result_list.append(str(v) + "=>(" + str(bag) + ")")
        return "Sap\nGraph:{}".format(repr(self.__graph))


def main():
    graph = Digraph(open("../data/word_net/digraph1.txt", "r"))
    sap = Sap(graph)
    print(repr(sap))
    print(sap.ancestor(3, 11), sap.length(3, 11))
    print(sap.ancestor(9, 12), sap.length(9, 12))
    print(sap.ancestor(7, 2), sap.length(7, 2))
    print(sap.ancestor(1, 6), sap.length(1, 6))


if __name__ == "__main__":
    main()
