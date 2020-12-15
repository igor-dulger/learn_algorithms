class Simplex(object):
    """
    Solves system of linear equations
    A[][] - list of coefficients
    b[] - constraints
    c[] - cost function coefficients
    """
    def __init__(self, A, b, c):
        self._matrix = []
        self._m = len(b)  # number of constrains
        self._n = len(c)  # number of variables

        for i in range(self._m+1):
            self._matrix.append([])
            for j in range(self._m+self._n+1):
                self._matrix[i].append(0)

        for i in range(self._m):
            self._matrix[i][self._n+self._m] = b[i]
        for i in range(self._n):
            self._matrix[self._m][i] = c[i]
        for i in range(len(A)):
            for j in range(len(c)):
                self._matrix[i][j] = A[i][j]
        for i in range(self._m):
            self._matrix[i][self._n+i] = 1

    def bland(self):
        for i in range(self._n + self._m):
            if self._matrix[self._m][i] > 0: return i
        return -1

    def min_ratio_rule(self, q):
        result = -1
        for i in range(self._m):
            if self._matrix[i][q] < 0:
                continue
            elif result == -1:
                result = i
            else:
                if self._matrix[i][self._m+self._n] / self._matrix[i][q] < self._matrix[result][self._m+self._n] / self._matrix[result][q]:
                    result = i
        return result

    def pivot(self, row, col):
        coeff = self._matrix[row][col]

        for i in range(self._m+self._n+1):
            self._matrix[row][i] /= coeff

        for i in range(self._m+1):
            row_coeff = self._matrix[i][col]
            for j in range(self._m+self._n+1):
                if i != row:
                    self._matrix[i][j] -= self._matrix[row][j]*row_coeff

    def solve(self):
        while True:
            col = self.bland()
            if col == -1: break
            row = self.min_ratio_rule(col)
            if row == -1: break
            self.pivot(row, col)

    def results(self):
        result = [round(self._matrix[self._m][self._m+self._n]*-1)]
        for j in range(self._n):
            for i in range(self._m):
                if self._matrix[i][j] == 1:
                    result.append(round(self._matrix[i][self._n+self._m], 2))
        return result

    def __str__(self):
        return "\n".join([" ".join(["{: >8.4f}".format(el) for el in line]) for line in self._matrix])


def __main__():
    s = Simplex(
        [
            [5, 15],
            [4, 4],
            [35, 20]
        ],
        [480, 160, 1190],
        [13, 23])
    print("Bland", s.bland())
    print("min ration rule for 0 =>", s.min_ratio_rule(0))
    print("min ration rule for 1 =>", s.min_ratio_rule(1))
    s.solve()
    print(s.results())


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    __main__()

