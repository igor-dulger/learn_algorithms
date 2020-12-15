from graph.graph import Graph
from dequeue.deque import Deque


class Bfs(object):
    def __init__(self, graph, s):
        self.__marked = [False for x in range(graph.v())]
        self.__edge_to = [None for x in range(graph.v())]
        self.__distance = [0 for x in range(graph.v())]
        self.__s = s
        self.__bfp(graph, s)

    def __bfp(self, graph, v):
        queue = Deque()

        try:
            for el in v:
                queue.add_last(el)
                self.__marked[el] = True
        except TypeError:
            queue.add_last(v)
            self.__marked[v] = True

        while not queue.is_empty():
            v = queue.remove_first()
            if self.__edge_to[v] is not None:
                self.__distance[v] = self.__distance[self.__edge_to[v]]+1
            for i in graph.adj(v):
                if not self.__marked[i]:
                    queue.add_last(i)
                    self.__marked[i] = True
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
        distance_list = [str(i) + " => " + str(v) for i, v in enumerate(self.__distance)]
        return "\nStart: {}\nMarked: {}\nFrom: {}\nDistance: {}".format(self.__s, ", ".join(market_list), ", ".join(edge_to_list), ", ".join(distance_list))


def main():
    d = Graph(6)
    d.add_edge(0, 5)
    d.add_edge(2, 4)
    d.add_edge(2, 3)
    d.add_edge(1, 2)
    d.add_edge(0, 1)
    d.add_edge(3, 4)
    d.add_edge(3, 5)
    d.add_edge(0, 2)

    print(repr(d))

    path = Bfs(d, [0, 3])
    print(repr(path))
    print("Has path to {} {}".format(2, path.has_path_to(2)))
    print("Has path to {} {}".format(5, path.has_path_to(5)))

    for i in path.path_to(4):
        print(i)

if __name__ == "__main__":
    main()
