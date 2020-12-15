class CircularSuffixArray(object):

    def __init__(self, s):
        if s is None or s == '':
            raise ValueError('none empty string expected')
        self.__string = s
        self.__index = []
        self.__len = len(self.__string)

        for i in range(self.__len):
            self.__index.append(i)

        self.__qsort(self.__index, 0, self.__len-1)

    def __qsort(self, a, lo, hi):
        if hi <= lo:
            return
        lt, i, gt = lo, lo + 1, hi
        v = a[lo]
        while i <= gt:
            cmp = self.__cmp_suffix(a[i], v)
            if cmp < 0:
                a[lt], a[i] = a[i], a[lt]
                lt += 1
                i += 1
            elif cmp > 0:
                a[gt], a[i] = a[i], a[gt]
                gt -= 1
            else: i += 1

        self.__qsort(a, lo, lt-1)
        self.__qsort(a, gt+1, hi)

    def __cmp_suffix(self, a, b):
        for i in range(self.__len):
            left = (a+i) % self.__len
            right = (b+i) % self.__len
            if self.__string[left] > self.__string[right]:
                return 1
            elif self.__string[left] < self.__string[right]:
                return -1
        return 0

    def index(self, i):
        if 0 > i or i >= self.__len:
            raise ValueError('Invalid index')
        return self.__index[i]

    def length(self):
        return self.__len

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        index = [str(i) + " => " + str(v) for i, v in enumerate(self.__index)]
        return "Index:\n{}\nLength:{}".format("\n".join(index), self.__len)


def main():
    text = "ABRACADABRA!"
    cfa = CircularSuffixArray(text)
    print(cfa)
    print(cfa.length())
    print(cfa.index(11))


if __name__ == "__main__":
    main()

