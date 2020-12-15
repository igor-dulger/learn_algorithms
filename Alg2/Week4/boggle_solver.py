from tree.tries.trie import Trie
from graph.basic import Digraph
from helpers.basic import timer


class BoggleBoard(object):
    @timer
    def __init__(self, filename):
        self.__rows = 0
        self.__cols = 0
        self.__board = []

        file = open(filename, "r")
        self.__rows, self.__cols = [int(i) for i in file.readline().split()]

        for line in [i.strip().split() for i in file]:
            if not len(line):
                continue
            if len(line) == self.__cols:
                self.__board.append(["Q" if len(i) == 2 else i for i in line])
            else:
                raise ValueError("Invalid number of columns {}, {} expected".format(len(line), self.__cols))

        if len(self.__board) != self.__rows:
            raise ValueError("Invalid number of rows {}, {} expected".format(j, self.__rows))

        file.close()

    def rows(self):
        return self.__rows

    def cols(self):
        return self.__cols

    def get_letter(self, i, j):
        return self.__board[i][j]

    def __str__(self):
        return "\n".join([" ".join(i) for i in self.__board])


class BoggleSolver(object):
    @timer
    def __init__(self, dictionary):
        self.__dict = Trie(26)
        self.__board = None
        self.__marked = []
        for word in dictionary:
            self.__dict.put(word, 1)

    @timer
    def get_all_valid_words(self, board):
        size = board.cols() * board.rows()
        graph = Digraph(size)
        self.__fill_in(graph, board)
        result = []
        self.__marked = [False] * size

        for i in range(size):
            node, char = self.__get_next_char(self.__dict.root, board, i)
            self.__find_words(node, board, graph, char, i, result)
        return result

    def __get_next_char(self, node, board, i):
        char = board.get_letter(*self.__get_indexes(i, board))
        node = node.nodes[self.__dict.char_at(char, 0)]
        if char == 'Q':
            if node is not None:
                node = node.nodes[self.__dict.char_at("U", 0)]
                char += 'U'
        return node, char

    def __find_words(self, node, board, graph, prefix, position, result):
        if node is None:
            return

        if node.value is not None and node.value == 1:
            result.append(prefix)
            self.__dict.put(prefix, 2)

        self.__marked[position] = True
        for i in graph.adj(position):
            next_node, next_char = self.__get_next_char(node, board, i)
            if not self.__marked[i] and next_node is not None:
                self.__find_words(next_node, board, graph, prefix + next_char, i, result)
        self.__marked[position] = False

    def __fill_in(self, graph, board):
        cols = board.cols()
        rows = board.rows()
        for i in range(cols * rows):
            x, y = self.__get_indexes(i, board)
            # print(i, x, y, self.__get_index(x, y))
            if x - 1 >= 0:
                graph.add_edge(i, self.__get_index(x - 1, y, board))
            if x + 1 < cols:
                graph.add_edge(i, self.__get_index(x + 1, y, board))
            if y - 1 >= 0:
                graph.add_edge(i, self.__get_index(x, y - 1, board))
            if y + 1 < rows:
                graph.add_edge(i, self.__get_index(x, y + 1, board))
            if x - 1 >= 0 and y - 1 >= 0:
                graph.add_edge(i, self.__get_index(x - 1, y - 1, board))
            if x + 1 < cols and y + 1 < rows:
                graph.add_edge(i, self.__get_index(x + 1, y + 1, board))
            if y - 1 >= 0 and x + 1 < cols:
                graph.add_edge(i, self.__get_index(x + 1, y - 1, board))
            if y + 1 < rows and x - 1 >= 0:
                graph.add_edge(i, self.__get_index(x - 1, y + 1, board))

    @staticmethod
    def score_of(word):
        wl = len(word)
        if 0 <= wl <= 2:
            return 0
        elif 3 <= wl <= 4:
            return 1
        elif wl == 5:
            return 2
        elif wl == 6:
            return 3
        elif wl == 7:
            return 5
        elif wl >= 8:
            return 11

    @staticmethod
    def __get_indexes(i, board):
        return i // board.cols(), i % board.cols()

    @staticmethod
    def __get_index(x, y, board):
        return board.cols() * x + y


def main():
    bb = BoggleBoard("../../data/boggle/board-points26539.txt")
    print(bb)

    words = []
    file = open("../../data/boggle/dictionary-yawl.txt", "r")
    for word in [i.strip() for i in file]:
        words.append(word)
    file.close()

    bs = BoggleSolver(words)
    words = bs.get_all_valid_words(bb)

    sum = 0
    for i in words:
        sum += bs.score_of(i)

    print("Score", sum, len(words))
    print(words)


if __name__ == "__main__":
    main()
