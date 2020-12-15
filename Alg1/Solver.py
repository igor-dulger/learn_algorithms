# public class Solver {
#     public Solver(Board initial)           // find a solution to the initial board (using the A* algorithm)
#     public boolean isSolvable()            // is the initial board solvable?
#     public int moves()                     // min number of moves to solve initial board; -1 if unsolvable
#     public Iterable<Board> solution()      // sequence of boards in a shortest solution; null if unsolvable
#     public static void main(String[] args) // solve a slider puzzle (given below)
# }
from Board import Board
from PriorityQueue import MinPriorityQueue
import sys
from helpers import timer


class Solver(object):

    def __init__(self, initial):
        self.__board = initial
        self.__empty_row = None
        self.__solvable = None
        if self.is_solvable():
            self.__solution = self.__solve()

    def __count_inversions(self):
        result = 0
        matrix = self.__board.blocks
        size = len(matrix)
        for i in range(size*size):
            left = matrix[i // size][i % size]
            if left == 0:
                self.__empty_row = i // size
                continue
            for j in range(i+1, size*size):
                right = matrix[j // size][j % size]
                if right == 0:
                    continue
                if left > right:
                    result += 1
        return result

    def is_solvable(self):
        if self.__solvable is None:
            inversions = self.__count_inversions()
            if self.__board.dimension() % 2 == 1:
                self.__solvable = (inversions % 2) == 0
            else:
                if (self.__board.dimension() - self.__empty_row) % 2 == 0:
                    self.__solvable = (inversions % 2) != 0
                else:
                    self.__solvable = (inversions % 2) == 0
        return self.__solvable

    def moves(self):
        if self.is_solvable():
            return self.__solution.moves
        else:
            return -1

    def solution(self):
        if not self.is_solvable():
            return
        move = 0
        while move <= self.__solution.moves:
            item = self.__solution
            while move < item.moves:
                item = item.predecessor
            move += 1
            yield item

    @timer
    def __solve(self):
        mpq = MinPriorityQueue()
        step = self.__board
        steps = 0
        while not step.is_goal():
            steps += 1
            for move in step.neighbors():
                # print(repr(move))
                mpq.push(move)
            step = mpq.pop()
        print("Steps:", steps)
        return step

    def __repr__(self):
        result = list()
        result.append("------Solver------")
        result.append("Initial:")
        result.append(repr(self.__board))
        result.append("Solution:")
        result.append(repr(self.__solution))
        result.append("-----------------")
        return "\n".join(result)


def main():

    args = sys.argv[1:]

    if not args:
        print('usage: Solver.py filename')
        sys.exit(1)
    else:
        filename = args[0]

    fd = open(filename, "r")
    fd.readline()
    matrix = []
    for line in [i.strip() for i in fd]:
        if line:
            matrix.append([int(chunk) for chunk in line.split()])

    print(matrix)
    solver = Solver(Board(matrix))

    if not solver.is_solvable():
        print("No solution possible")
    else:
        print("Minimum number of moves = " + str(solver.moves()))

    # for i in solver.solution():
    #     print(i)
    #     print()

if __name__ == "__main__":
    main()

