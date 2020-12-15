class KMP(object):
    ALPHABET_SIZE = 256

    def __init__(self, pattern):
        self.__pattern = pattern
        self.__m = len(self.__pattern)
        self.__dfa = [[0]*self.__m for i in range(self.ALPHABET_SIZE)]
        self.__dfa[ord(self.__pattern[0])][0] = 1
        x = 0
        for j in range(1, self.__m):
            for c in range(0, self.ALPHABET_SIZE):
                self.__dfa[c][j] = self.__dfa[c][x]

            self.__dfa[ord(self.__pattern[j])][j] = j+1
            x = self.__dfa[ord(self.__pattern[j])][x]

    def search(self, text):
        i, j, n = 0, 0, len(text)
        while i < n and j < self.__m:
            j = self.__dfa[ord(text[i])][j]
            i += 1

        return i - self.__m if j == self.__m else n

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "\n".join([str(x) for x in self.__dfa])


def main():
    text = "AABACAABABACAA"
    pattern = "ABABAC"
    kmp = KMP(pattern)
    res = kmp.search(text)
    stop = res+len(pattern)
    print(res, text[:res]+"_"+text[res:stop]+"_"+text[stop:], pattern)


if __name__ == "__main__":
    main()

