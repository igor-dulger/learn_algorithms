# Percolation data type. To model a percolation system, create a data type Percolation with the following API:
#
# public class Percolation {
#    public Percolation(int n)                // create n-by-n grid, with all sites blocked
#    public    void open(int row, int col)    // open site (row, col) if it is not open already
#    public boolean isOpen(int row, int col)  // is site (row, col) open?
#    public boolean isFull(int row, int col)  // is site (row, col) full?
#    public     int numberOfOpenSites()       // number of open sites
#    public boolean percolates()              // does the system percolate?
#
#    public static void main(String[] args)   // test client (optional)
# }
# Corner cases.  By convention, the row and column indices are integers between 1 and n, where (1, 1) is the upper-left site:
# Throw a java.lang.IllegalArgumentException if any argument to open(), isOpen(), or isFull() is outside its prescribed range.
# The constructor should throw a java.lang.IllegalArgumentException if n ≤ 0.
#
# Performance requirements.  The constructor should take time proportional to n2; all methods should take constant time
# plus a constant number of calls to the union–find methods union(), find(), connected(), and count().
from WeightedQuickUnionUF import WeightedQuickUnionUF


class Percolation(object):
    __open = 'WW'
    __full = '--'

    def __init__(self, n):
        if n < 0:
            raise ValueError("N must be positive integer")

        self.__size = n
        self.__open_sites = 0
        self.__matrix = [self.__full] * n * n
        self.__top = self.__get_vector_index(n, n) + 1
        self.__bottom = self.__get_vector_index(n, n) + 2
        self.__uf = WeightedQuickUnionUF(n*n + 2)
        for i in range(1, self.__size+1):
            self.__uf.union(self.__top, self.__get_vector_index(1, i))
            self.__uf.union(self.__bottom, self.__get_vector_index(n, i))

    def __get_vector_index(self, row, col):
        if 0 >= row or row > self.__size or col <= 0 or col > self.__size:
            return False
        else:
            return (row - 1) * self.__size + (col - 1)

    def __get_vector_index_with_check(self, row, col):
        i = self.__get_vector_index(row, col)
        if i is False:
            raise ValueError("Invalid {}, {} points out of allowed range".format(row, col))
        else:
            return i

    def __connect(self, current_i, row, col):
        target_i = self.__get_vector_index(row, col)

        if target_i is False or self.is_full(row, col):
            return False
        else:
            self.__uf.union(current_i, target_i)

    def open(self, row, col):
        i = self.__get_vector_index_with_check(row, col)
        if self.is_full(row, col):
            self.__matrix[i] = self.__open
            self.__connect(i, row-1, col)
            self.__connect(i, row, col-1)
            self.__connect(i, row, col+1)
            self.__connect(i, row+1, col)
            self.__open_sites += 1
            return True
        else:
            return False

    def is_open(self, row, col):
        return self.__matrix[self.__get_vector_index_with_check(row, col)] == self.__open

    def is_full(self, row, col):
        return self.__matrix[self.__get_vector_index_with_check(row, col)] == self.__full

    @property
    def number_of_open_sites(self):
        return self.__open_sites

    def percolates(self):
        # print(self.__uf)
        if self.__size == 1:
            return self.is_open(1, 1)
        else:
            return self.__uf.connected(self.__top, self.__bottom)

    def __str__(self):
        result = ["N: {} \n".format(self.__size), "Open sites: {} \n".format(self.number_of_open_sites)]
        for row in range(1, self.__size+1):
            for col in range(1, self.__size+1):
                result.append(str(self.__matrix[self.__get_vector_index(row, col)]))
            result.append("\n")
        return ''.join(result)


def main():

    def test(name, actual, expected):
        if actual != expected:
            print("Test {} FAILED get {} Expected {} ".format(name, actual, expected))
        else:
            print("Test {} OK".format(name))

    from os import listdir
    from os.path import isfile, join
    import re

    datadir = 'data/percolation/'
    onlyfiles = [f for f in listdir(datadir) if isfile(join(datadir, f))]

    for file in [join(datadir, name) for name in sorted(onlyfiles) if re.search('\.txt$', name)]:
        fd = open(file, "r")
        num = int(fd.readline())
        # if file != 'data/percolation/input8.txt':
        #     continue
        print(file)
        p = Percolation(num)
        for line in [line.strip() for line in fd if line.strip()]:
            row, col = [int(chunk) for chunk in line.split()]
            # print("Open {} {}".format(row, col))
            p.open(row, col)
        test("Percolate", p.percolates(), re.search(r'\-no\.txt$', file) is None)
        # print(p)


if __name__ == "__main__":
    main()

