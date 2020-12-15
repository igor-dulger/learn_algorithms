# Board and Solver data types. Organize your program by creating an immutable data type Board with the following API:
#
# public class Board {
#     public Board(int[][] blocks)           // construct a board from an n-by-n array of blocks
#                                            // (where blocks[i][j] = block in row i, column j)
#     public int dimension()                 // board dimension n
#     public int hamming()                   // number of blocks out of place
#     public int manhattan()                 // sum of Manhattan distances between blocks and goal
#     public boolean isGoal()                // is this board the goal board?
#     public Board twin()                    // a board that is obtained by exchanging any pair of blocks
#     public boolean equals(Object y)        // does this board equal y?
#     public Iterable<Board> neighbors()     // all neighboring boards
#     public String toString()               // string representation of this board (in the output format specified
# below)
#
#     public static void main(String[] args) // unit tests (not graded)
# }
# Corner cases.  You may assume that the constructor receives an n-by-n array containing the n2 integers between 0
# and n2 − 1, where 0 represents the blank square.
#
# Performance requirements.  Your implementation should support all Board methods in time proportional to n2
# (or better) in the worst case.
from PriorityQueue import MinPriorityQueue


class Board(object):

    empty_block = 0

    def __init__(self, blocks):
        self.__blocks = blocks

        self.__predecessor = None
        self.__empty_index = self.__find_empty()
        self.__hamming = None
        self.__manhattan = None
        self.__moves = 0

    def __find_empty(self):
        for i in range(self.__size()):
            if self.__block(i) == self.empty_block:
                return i
        raise BaseException("Invalid matrix, can't find an empty block")

    def __get_indexes(self, i):
        return i//self.dimension(), i % self.dimension()

    def __size(self):
        return self.dimension()*self.dimension()

    def __count_wrong_positions(self):
        result = 0
        for i in range(self.__size()-1):
            if self.__block(i) != i+1:
                result += 1
        return result

    def __get_distance(self, x, y, value):
        if value == self.empty_block:
            return 0
        goal_x, goal_y = self.__get_indexes(value-1)
        return abs(goal_x - x) + abs(goal_y - y)

    def dimension(self):
        return len(self.__blocks)

    def hamming(self):
        if self.__hamming is None:
            self.__hamming = self.__count_wrong_positions() + self.moves
        return self.__hamming

    def manhattan(self):
        if self.__manhattan is None:
            self.__manhattan = self.moves
            for i in range(self.__size()):
                x, y = self.__get_indexes(i)
                self.__manhattan += self.__get_distance(x, y, self.__block(i))
        return self.__manhattan

    @property
    def predecessor(self):
        return self.__predecessor

    @property
    def empty_index(self):
        return self.__empty_index

    @predecessor.setter
    def predecessor(self, board):
        self.__predecessor = board
        if board is not None:
            self.__moves = board.moves + 1

    def is_goal(self):
        return self.__count_wrong_positions() == 0

    def twin(self):
        pass

    def equals(self, y):
        if y is None:
            return False
        return self.__blocks == y.blocks

    def __block(*args):
        self = args[0]
        if len(args[1:]) == 1:
            x, y = self.__get_indexes(args[1])
        else:
            x, y = args[1:]
        return self.__blocks[x][y]

    @staticmethod
    def __swap_block(matrix, x, y, x1, y1):
        t = matrix[x][y]
        matrix[x][y] = matrix[x1][y1]
        matrix[x1][y1] = t
        return matrix

    @property
    def blocks(self):
        return self.__blocks

    @property
    def moves(self):
        return self.__moves

    def neighbors(self):
        x, y = self.__get_indexes(self.__empty_index)

        if x - 1 >= 0:
            res = self.__class__(self.__swap_block([row[:] for row in self.blocks], x, y, x-1, y))
            res.predecessor = self
            if not res.equals(self.predecessor):
                yield res
        if x + 1 <= self.dimension()-1:
            res = self.__class__(self.__swap_block([row[:] for row in self.blocks], x, y, x + 1, y))
            res.predecessor = self
            if not res.equals(self.predecessor):
                yield res
        if y - 1 >= 0:
            res = self.__class__(self.__swap_block([row[:] for row in self.blocks], x, y, x, y - 1))
            res.predecessor = self
            if not res.equals(self.predecessor):
                yield res
        if y + 1 <= self.dimension()-1:
            res = self.__class__(self.__swap_block([row[:] for row in self.blocks], x, y, x, y + 1))
            res.predecessor = self
            if not res.equals(self.predecessor):
                yield res

    def __compare_to(self, other):
        if self.manhattan() < other.manhattan():
            return -1
        elif self.manhattan() > other.manhattan():
            return 1
        else:
            return 0

    def __cmp__(self, other):
        self.__compare_to(other)

    def __lt__(self, other):
        return self.__compare_to(other) < 0

    def __gt__(self, other):
        return self.__compare_to(other) > 0

    def __eq__(self, other):
        return self.__compare_to(other) == 0

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        res = ''
        for i in range(self.__size()):
            res += str(self.__block(i))
        return hash(res)

    def __make_printable_matrix(self, matrix):
        blocks = ['']*len(matrix)
        for i in range(len(matrix)*len(matrix)):
            x, y = self.__get_indexes(i)
            if matrix[x][y] == self.empty_block:
                output = '-'
            else:
                output = str(matrix[x][y])
            blocks[x] += output + ' '
        return "\n".join(blocks)

    def __repr__(self):
        result = list()
        result.append("------Board------")
        result.append("Moves:" + str(self.moves))
        # result.append("Hamming:" + str(self.hamming()))
        result.append("Manhattan:" + str(self.manhattan()))
        # result.append("Dimension:" + str(self.dimension()))
        # result.append("Empty block:" + str(self.__empty_index))
        result.append("State:")
        result.append(self.__make_printable_matrix(self.__blocks))
        if self.predecessor is not None:
            result.append("Predecessor:")
            result.append(self.__make_printable_matrix(self.predecessor.blocks))
        result.append("-----------------")
        return "\n".join(result)

    def __str__(self):
        result = list()
        result.append(self.__make_printable_matrix(self.__blocks))
        return "\n".join(result)


def main():
    a = Board([[8, 1, 3], [4, 0, 2], [7, 6, 5]])
    print(repr(a))
    b = Board([[0, 1, 3], [4, 8, 2], [7, 5, 6]])
    print(repr(b))

    #
    # for n in b.neighbors():
    #     print(repr(n))
    #     for k in n.neighbors():
    #         print(repr(k))


if __name__ == "__main__":
    main()
