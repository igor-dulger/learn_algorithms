class BoyerMoore(object):
    ALPHABET_SIZE = 256

    def __init__(self, pattern):
        self.__right = [-1] * self.ALPHABET_SIZE
        self.__pattern = pattern
        self.__m = len(pattern)
        for i in range(self.__m):
            self.__right[ord(pattern[i])] = i

    def search(self, text):
        n, m = len(text), len(self.__pattern)
        i = 0
        while i <= n-m:
            skip = 0
            for j in range(m-1, 0, -1):
                if self.__pattern[j] != text[i+j]:
                    skip = max(1, j - self.__right[ord(text[i+j])])
                    break
            if skip == 0:
                return i
            i += skip
        return n

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.__right)


def main():
    text = "FINDINAHAYSTACKNEEDLEINA"
    pattern = "NEEDLE"
    bm = BoyerMoore(pattern)
    # print(bm)
    res = bm.search(text)
    stop = res+len(pattern)
    print(res, text[:res]+"_"+text[res:stop]+"_"+text[stop:], pattern)


if __name__ == "__main__":
    main()

